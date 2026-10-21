import json
import re
from datetime import date

_RE_NEXT_DATA = re.compile(
    r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', re.S
)

CAMPOS = [
    "fecha_captura", "categoria", "product_id", "sku_id", "nombre", "marca",
    "vendedor", "vendedor_id", "precio_cmr", "precio_online", "precio_lista",
    "rating", "n_resenas", "posicion_en_pagina", "pagina", "es_patrocinado", "url",
]


def extraer_next_data(html: str) -> dict:
    m = _RE_NEXT_DATA.search(html)
    if not m:
        raise ValueError("no se encontro __NEXT_DATA__ en el HTML")
    return json.loads(m.group(1))["props"]["pageProps"]


def _a_float(texto) -> float | None:
    if texto in (None, ""):
        return None
    return float(str(texto).replace(",", ""))


def _a_int(texto) -> int | None:
    if texto in (None, ""):
        return None
    return int(float(texto))


def extraer_precios(prices: list[dict]) -> tuple[float | None, float | None, float | None]:
    """(cmr, online, lista). online = eventPrice si existe, si no internetPrice."""
    por_tipo = {p["type"]: _a_float(p["price"][0]) for p in prices if p.get("price")}
    online = por_tipo.get("eventPrice", por_tipo.get("internetPrice"))
    return por_tipo.get("cmrPrice"), online, por_tipo.get("normalPrice")


def parsear_producto(p: dict, fecha: date, categoria: str, pagina: int, posicion: int) -> dict:
    cmr, online, lista = extraer_precios(p.get("prices", []))
    return {
        "fecha_captura": fecha.isoformat(),
        "categoria": categoria,
        "product_id": p["productId"],
        "sku_id": p.get("skuId"),
        "nombre": p.get("displayName"),
        "marca": p.get("brand"),
        "vendedor": p.get("sellerName"),
        "vendedor_id": p.get("sellerId"),
        "precio_cmr": cmr,
        "precio_online": online,
        "precio_lista": lista,
        "rating": _a_float(p.get("rating")),
        "n_resenas": _a_int(p.get("totalReviews")),  # NULL si el listado no trae el campo
        "posicion_en_pagina": posicion,
        "pagina": pagina,
        "es_patrocinado": 1 if p.get("isSponsored") else 0,
        "url": p.get("url"),
    }


def parsear_pagina(html: str, fecha: date, categoria: str, pagina: int) -> tuple[list[dict], dict]:
    props = extraer_next_data(html)
    filas = [
        parsear_producto(p, fecha, categoria, pagina, pos)
        for pos, p in enumerate(props.get("results", []), start=1)
    ]
    return filas, props.get("pagination", {})
