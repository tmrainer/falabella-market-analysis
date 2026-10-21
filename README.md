# Análisis de mercado – falabella.com.pe

Proyecto de portafolio (analista de datos). Recolecta diariamente el listado de productos de
categorías seleccionadas de falabella.com.pe y lo guarda en SQLite para analizar catálogo,
demanda (vía crecimiento de reseñas) y descuentos en campañas.

Estado: **Fase 0 – piloto de recolección** (ver `reports/exploracion_fase0.md`).

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Estructura

```
src/        código del scraper, carga y reporte
sql/        esquema SQLite y consultas de validación
notebooks/  análisis exploratorio (fases siguientes)
data/raw/   HTML crudo comprimido por fecha (NO va a git)
data/db/    falabella.db
reports/    reportes en Markdown
logs/       un log por corrida (NO va a git)
scripts/    automatización (systemd timer)
```
