# Análisis de mercado – falabella.com.pe

Proyecto de portafolio (analista de datos, Perú). Captura diariamente el listado de productos de
7 categorías de falabella.com.pe y lo guarda en SQLite para analizar catálogo, demanda (crecimiento
de reseñas) y descuentos en campañas (Cyber WOW, Black Friday).

Estado: **Fase 0 completada (2026-10-21)** – piloto de recolección validado.

## Resultados del piloto (5 páginas × 7 categorías, 35 requests, 3.5 min)

| categoría | productos | % con ≥1 reseña | % con ≥10 | mediana | patrocinados |
|---|---:|---:|---:|---:|---:|
| smartphones | 250 | 76.4 | 32.4 | 5 | 18 |
| televisores | 242 | 68.6 | 40.5 | 3.5 | 6 |
| laptops | 246 | 52.8 | 15.9 | 1 | 27 |
| zapatillas urbanas hombre | 253 | 88.1 | 50.6 | 10 | 20 |
| zapatillas urbanas mujer | 251 | 89.2 | 61.8 | 16 | 23 |
| zapatillas deportivas hombre | 254 | 79.5 | 44.1 | 7 | 20 |
| zapatillas deportivas mujer | 256 | 78.1 | 32.8 | 5 | 19 |

Hay reseñas suficientes para la Fase 2 en todas las categorías; laptops es la más débil.
Se confirmó que algunos productos comparten el conteo de reseñas entre vendedores
(ej. Galaxy A16: 512 reseñas en 3 vendedores). Detalle en `reports/validacion_piloto_2026-10-21.md`.

## Fases
0. Piloto de recolección ✔ (`reports/exploracion_fase0.md`)
1. Catálogo: concentración de demanda, participación por marca, rangos de precio.
2. Crecimiento semanal de reseñas como proxy de demanda (requiere capturas diarias).
3. Descuentos en Cyber WOW y Black Friday.

## Instalación y uso

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python -m src.run_pilot                                  # descarga + carga + reporte de hoy
python -m src.run_pilot --solo-parsear --fecha 2026-10-21 # re-procesa data/raw sin descargar
python -m src.run_pilot --paginas 1 --categorias laptops  # prueba rápida
```

Cada corrida escribe `logs/piloto_YYYY-MM-DD.log`, guarda el HTML crudo en
`data/raw/YYYY-MM-DD/*.html.gz` y registra la ejecución en la tabla `corridas`.

## Ejecución diaria (Linux)

```bash
scripts/instalar_timer.sh          # systemd --user timer, 08:30 ± 10 min, Persistent=true
systemctl --user list-timers       # ver próxima ejecución
journalctl --user -u falabella-piloto.service -n 50   # ver salida
```
Alternativa con cron en `scripts/crontab_ejemplo.txt`.

## Decisiones técnicas (resumen para entrevistas)

- **Fuente de datos**: el sitio es Next.js con SSR; el JSON `__NEXT_DATA__` embebido trae los
  productos. Se parsea JSON en vez del DOM porque las clases CSS cambian, el contrato de datos no.
  No hay API pública de categorías (el BFF es interno).
- **Ética**: `robots.txt` permite categorías. 3–5 s aleatorios entre requests, 35 requests/día,
  abortar ante 403/429, sin datos personales (solo conteo y promedio de reseñas).
- **Raw primero**: se guarda el HTML en gzip (~250 KB/página). Si cambia el parser se reprocesa
  con `--solo-parsear` sin volver a descargar.
- **Esquema**: `productos` (estable) + `capturas` con PK `(fecha, categoria, product_id, sku_id)`.
  La fecha en la clave permite comparar fotos; `INSERT OR REPLACE` hace la carga idempotente.
  Los patrocinados se repiten en varias páginas: la clave colapsa esos duplicados (queda la
  última posición vista), por eso 1,952 filas parseadas → 1,780 en la tabla.
- **NULL en `n_resenas`**: el listado omite el campo cuando no hay reseñas; se guarda NULL y el
  reporte usa `COALESCE(n_resenas, 0)`.
- **SQL en archivos `.sql`** con bloques `-- @nombre`; pandas solo para la mediana y las tablas.

## Estructura

```
src/        config, fetch, parse, db, report, run_pilot
sql/        schema.sql, validacion.sql
notebooks/  análisis (fases siguientes)
data/raw/   HTML crudo por fecha (NO va a git)
data/db/    falabella.db (NO va a git)
reports/    exploración y validaciones en Markdown
logs/       un log por corrida (NO va a git)
scripts/    systemd timer y cron
```
