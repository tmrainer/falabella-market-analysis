"""Uso:
    python -m src.run_pilot
    python -m src.run_pilot --solo-parsear --fecha 2026-10-21
    python -m src.run_pilot --paginas 2 --categorias laptops
"""
import argparse
import logging
import sys
from datetime import date, datetime

import requests

from src import config, db, fetch, parse, report

log = logging.getLogger("piloto")


def configurar_logging(fecha: date) -> None:
    config.DIR_LOGS.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(config.DIR_LOGS / f"piloto_{fecha.isoformat()}.log", encoding="utf-8"),
        ],
    )


def procesar_categoria(con, sesion, categoria: str, fecha: date, paginas: int, solo_parsear: bool) -> tuple[int, int]:
    """Devuelve (paginas procesadas, filas cargadas)."""
    if solo_parsear:
        rutas = [fetch.ruta_raw(fecha, categoria, p) for p in range(1, paginas + 1)]
        rutas = [r for r in rutas if r.exists()]
    else:
        rutas = fetch.descargar_categoria(sesion, categoria, fecha, paginas)

    total_filas = 0
    for pagina, ruta in enumerate(rutas, start=1):
        filas, paginacion = parse.parsear_pagina(fetch.leer_raw(ruta), fecha, categoria, pagina)
        n = db.cargar_filas(con, filas)
        total_filas += n
        log.info(
            "%s p%d: %d filas (catalogo total=%s, patrocinados=%d)",
            categoria, pagina, n, paginacion.get("count"), sum(f["es_patrocinado"] for f in filas),
        )
    return len(rutas), total_filas


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fecha", type=date.fromisoformat, default=date.today())
    ap.add_argument("--paginas", type=int, default=config.PAGINAS_POR_CATEGORIA)
    ap.add_argument("--categorias", nargs="*", default=list(config.CATEGORIAS))
    ap.add_argument("--solo-parsear", action="store_true")
    ap.add_argument("--sin-reporte", action="store_true")
    args = ap.parse_args(argv)

    configurar_logging(args.fecha)
    log.info("inicio | fecha=%s paginas=%d categorias=%s solo_parsear=%s", args.fecha, args.paginas, args.categorias, args.solo_parsear)

    con = db.conectar()
    db.crear_esquema(con)
    corrida_id = db.registrar_corrida(con, args.fecha.isoformat(), datetime.now().isoformat(timespec="seconds"))

    paginas_ok = filas_total = 0
    estado, detalle = "ok", ""
    try:
        with requests.Session() as sesion:
            for categoria in args.categorias:
                p, f = procesar_categoria(con, sesion, categoria, args.fecha, args.paginas, args.solo_parsear)
                paginas_ok += p
                filas_total += f
    except fetch.BloqueoDetectado as exc:
        estado, detalle = "bloqueado", str(exc)
        log.error("BLOQUEO: %s. Corrida detenida.", exc)
    except Exception as exc:  # noqa: BLE001
        estado, detalle = "error", f"{type(exc).__name__}: {exc}"
        log.exception("error inesperado")
    finally:
        db.cerrar_corrida(con, corrida_id, datetime.now().isoformat(timespec="seconds"), paginas_ok, filas_total, estado, detalle)
        log.info("fin | estado=%s paginas=%d filas=%d", estado, paginas_ok, filas_total)

    if estado == "ok" and not args.sin_reporte:
        log.info("reporte: %s", report.generar(con, args.fecha.isoformat()))

    con.close()
    return 0 if estado == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
