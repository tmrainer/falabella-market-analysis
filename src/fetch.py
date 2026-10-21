import gzip
import logging
import random
import time
from datetime import date
from pathlib import Path

import requests

from src import config

log = logging.getLogger(__name__)


class BloqueoDetectado(Exception):
    """HTTP 403 o 429: se detiene toda la corrida."""


def pausa_aleatoria() -> None:
    time.sleep(random.uniform(config.PAUSA_MIN_S, config.PAUSA_MAX_S))


def descargar(sesion: requests.Session, url: str) -> str:
    for intento in range(1, config.MAX_INTENTOS + 1):
        try:
            resp = sesion.get(url, headers=config.CABECERAS, timeout=config.TIMEOUT_S)
        except requests.RequestException as exc:
            log.warning("intento %d/%d fallo (%s): %s", intento, config.MAX_INTENTOS, type(exc).__name__, url)
            resp = None

        if resp is not None:
            if resp.status_code in (403, 429):
                raise BloqueoDetectado(f"HTTP {resp.status_code} en {url}")
            if resp.status_code == 200:
                return resp.text
            log.warning("intento %d/%d HTTP %d: %s", intento, config.MAX_INTENTOS, resp.status_code, url)

        if intento < config.MAX_INTENTOS:
            time.sleep(config.ESPERA_BASE_S * 2 ** (intento - 1))

    raise RuntimeError(f"sin respuesta valida tras {config.MAX_INTENTOS} intentos: {url}")


def ruta_raw(fecha: date, categoria: str, pagina: int) -> Path:
    return config.DIR_RAW / fecha.isoformat() / f"{categoria}_p{pagina}.html.gz"


def guardar_raw(ruta: Path, html: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(ruta, "wt", encoding="utf-8") as f:
        f.write(html)


def leer_raw(ruta: Path) -> str:
    with gzip.open(ruta, "rt", encoding="utf-8") as f:
        return f.read()


def descargar_categoria(sesion: requests.Session, categoria: str, fecha: date, paginas: int) -> list[Path]:
    """Devuelve las rutas raw. Si una pagina ya existe para esa fecha, no vuelve a pedirla."""
    rutas = []
    for pagina in range(1, paginas + 1):
        ruta = ruta_raw(fecha, categoria, pagina)
        if ruta.exists():
            log.info("%s p%d ya descargada, se omite", categoria, pagina)
            rutas.append(ruta)
            continue
        url = config.url_categoria(categoria, pagina)
        inicio = time.monotonic()
        html = descargar(sesion, url)
        guardar_raw(ruta, html)
        log.info("%s p%d OK %.1f s %d KB -> %s", categoria, pagina, time.monotonic() - inicio, len(html) // 1024, ruta.name)
        rutas.append(ruta)
        pausa_aleatoria()
    return rutas
