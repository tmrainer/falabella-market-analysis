"""Uso: python -m src.export"""
import logging
import sys

import pandas as pd

from src import config, db

log = logging.getLogger("export")

VISTAS = ["v_catalogo", "v_marcas", "v_pareto"]


def crear_vistas(con) -> None:
    con.executescript((config.DIR_SQL / "catalogo.sql").read_text(encoding="utf-8"))


def exportar(con, vista: str) -> int:
    df = pd.read_sql_query(f"SELECT * FROM {vista}", con)
    ruta = config.DIR_EXPORT / f"{vista[2:]}.csv"
    df.to_csv(ruta, index=False, encoding="utf-8")
    log.info("%s -> %s (%d filas)", vista, ruta.name, len(df))
    return len(df)


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)-7s %(message)s", stream=sys.stdout)
    config.DIR_EXPORT.mkdir(parents=True, exist_ok=True)
    con = db.conectar()
    crear_vistas(con)
    for vista in VISTAS:
        exportar(con, vista)
    con.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
