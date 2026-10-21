import sqlite3
from pathlib import Path

from src import config
from src.parse import CAMPOS

COLS_CAPTURA = [c for c in CAMPOS if c not in ("nombre", "marca")]

_SQL_PRODUCTO = """
INSERT INTO productos (product_id, nombre, marca, url, categoria_origen, primera_captura, ultima_captura)
VALUES (:product_id, :nombre, :marca, :url, :categoria, :fecha_captura, :fecha_captura)
ON CONFLICT(product_id) DO UPDATE SET
    nombre = excluded.nombre,
    marca = excluded.marca,
    url = excluded.url,
    ultima_captura = MAX(ultima_captura, excluded.ultima_captura)
"""

_SQL_CAPTURA = f"""
INSERT OR REPLACE INTO capturas ({", ".join(COLS_CAPTURA)})
VALUES ({", ".join(":" + c for c in COLS_CAPTURA)})
"""


def conectar(ruta: Path = config.RUTA_DB) -> sqlite3.Connection:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(ruta)
    con.execute("PRAGMA foreign_keys = ON")
    return con


def crear_esquema(con: sqlite3.Connection) -> None:
    con.executescript((config.DIR_SQL / "schema.sql").read_text(encoding="utf-8"))


def cargar_filas(con: sqlite3.Connection, filas: list[dict]) -> int:
    with con:
        con.executemany(_SQL_PRODUCTO, filas)
        con.executemany(_SQL_CAPTURA, filas)
    return len(filas)


def registrar_corrida(con: sqlite3.Connection, fecha: str, inicio: str) -> int:
    with con:
        cur = con.execute("INSERT INTO corridas (fecha_captura, inicio) VALUES (?, ?)", (fecha, inicio))
    return cur.lastrowid


def cerrar_corrida(con, corrida_id: int, fin: str, paginas_ok: int, filas: int, estado: str, detalle: str = "") -> None:
    with con:
        con.execute(
            "UPDATE corridas SET fin=?, paginas_ok=?, filas_cargadas=?, estado=?, detalle=? WHERE id=?",
            (fin, paginas_ok, filas, estado, detalle, corrida_id),
        )
