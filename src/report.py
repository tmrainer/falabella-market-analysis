import re
import sqlite3
from pathlib import Path

import pandas as pd

from src import config

_RE_BLOQUE = re.compile(r"^-- @(\w+)\s*$", re.M)


def cargar_consultas(ruta: Path = config.DIR_SQL / "validacion.sql") -> dict[str, str]:
    """{nombre: sql} a partir de los marcadores '-- @nombre'."""
    partes = _RE_BLOQUE.split(ruta.read_text(encoding="utf-8"))
    return {partes[i]: partes[i + 1].strip() for i in range(1, len(partes), 2)}


def a_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_sin filas_"
    cols = list(df.columns)
    filas = [" | ".join(cols), " | ".join("---" for _ in cols)]
    for _, r in df.iterrows():
        filas.append(" | ".join("" if pd.isna(v) else str(v) for v in r))
    return "\n".join(f"| {f} |" for f in filas)


def resumen(con: sqlite3.Connection, fecha: str) -> pd.DataFrame:
    q = cargar_consultas()
    base = pd.read_sql_query(q["resumen_categoria"], con, params={"fecha": fecha})
    por_producto = pd.read_sql_query(q["productos_por_categoria"], con, params={"fecha": fecha})
    mediana = por_producto.groupby("categoria")["n_resenas"].median().rename("mediana_resenas")
    return base.merge(mediana, on="categoria")


def resenas_compartidas(con: sqlite3.Connection, fecha: str) -> pd.DataFrame:
    return pd.read_sql_query(cargar_consultas()["resenas_compartidas"], con, params={"fecha": fecha})


def generar(con: sqlite3.Connection, fecha: str) -> Path:
    df_resumen = resumen(con, fecha)
    df_comp = resenas_compartidas(con, fecha)
    total = int(df_resumen["productos"].sum()) if not df_resumen.empty else 0

    md = [
        f"# Validacion del piloto - {fecha}",
        "",
        f"Productos distintos capturados: **{total}** en {len(df_resumen)} categorias "
        f"({config.PAGINAS_POR_CATEGORIA} paginas por categoria).",
        "",
        "## Resumen por categoria",
        "",
        "`pct_con_resena` = % de productos con >=1 resena; `pct_10_o_mas` = % con >=10. "
        "La mediana se calcula sobre productos (no SKU).",
        "",
        a_markdown(df_resumen),
        "",
        "## Posibles resenas compartidas",
        "",
        "Productos distintos, misma marca, mismo `n_resenas` y `rating`, vendidos por mas de un "
        "vendedor (umbral n_resenas >= 5). Indica que el conteo se agrega por modelo.",
        "",
        a_markdown(df_comp),
        "",
    ]
    config.DIR_REPORTES.mkdir(exist_ok=True)
    ruta = config.DIR_REPORTES / f"validacion_piloto_{fecha}.md"
    ruta.write_text("\n".join(md), encoding="utf-8")
    return ruta
