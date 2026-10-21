from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIR_RAW = RAIZ / "data" / "raw"
DIR_DB = RAIZ / "data" / "db"
DIR_LOGS = RAIZ / "logs"
DIR_REPORTES = RAIZ / "reports"
DIR_SQL = RAIZ / "sql"
RUTA_DB = DIR_DB / "falabella.db"

BASE_URL = "https://www.falabella.com.pe/falabella-pe/category"

# clave interna -> (id de categoria, slug)
CATEGORIAS = {
    "smartphones": ("CATG15605", "Smartphones"),
    "televisores": ("cat6370551", "Televisores-Smart-TV"),
    "laptops": ("cat40712", "Laptops"),
    "zapatillas_urbanas_hombre": ("cat1480500", "Zapatillas-urbanas-hombre"),
    "zapatillas_urbanas_mujer": ("cat1470534", "Zapatillas-urbanas-mujer"),
    "zapatillas_deportivas_hombre": ("CATG15651", "Zapatillas-deportivas-hombre"),
    "zapatillas_deportivas_mujer": ("cat16200461", "Zapatillas-deportivas-mujer"),
}

PAGINAS_POR_CATEGORIA = 5

PAUSA_MIN_S = 3.0
PAUSA_MAX_S = 5.0
MAX_INTENTOS = 3
ESPERA_BASE_S = 5.0
TIMEOUT_S = 30

CABECERAS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "es-PE,es;q=0.9",
}


def url_categoria(clave: str, pagina: int) -> str:
    cat_id, slug = CATEGORIAS[clave]
    url = f"{BASE_URL}/{cat_id}/{slug}"
    return url if pagina == 1 else f"{url}?page={pagina}"
