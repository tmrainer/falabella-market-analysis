-- vistas de fase 1 sobre la ultima captura

-- una fila por (categoria, producto); sku representativo = el de menor precio_online
CREATE VIEW IF NOT EXISTS v_catalogo AS
WITH ultima AS (
    SELECT MAX(fecha_captura) AS fecha FROM capturas
),
skus AS (
    SELECT c.*,
           ROW_NUMBER() OVER (PARTITION BY c.categoria, c.product_id ORDER BY c.precio_online, c.sku_id) AS rn,
           MAX(COALESCE(c.n_resenas, 0)) OVER (PARTITION BY c.categoria, c.product_id) AS n_resenas_prod,
           MAX(c.es_patrocinado) OVER (PARTITION BY c.categoria, c.product_id) AS patrocinado_prod,
           MIN(c.pagina) OVER (PARTITION BY c.categoria, c.product_id) AS pagina_prod
    FROM capturas c
    JOIN ultima u ON c.fecha_captura = u.fecha
)
SELECT
    s.fecha_captura,
    s.categoria,
    s.product_id,
    p.nombre,
    p.marca,
    s.vendedor,
    CASE WHEN s.vendedor IN ('Falabella', 'Sodimac', 'Tottus') THEN '1P' ELSE '3P' END AS tipo_vendedor,
    s.precio_online,
    s.precio_lista,
    s.precio_cmr,
    CASE WHEN s.precio_lista > 0
         THEN ROUND(100.0 * (1 - s.precio_online / s.precio_lista), 1) END AS descuento_pct,
    s.precio_cmr IS NOT NULL AS tiene_cmr,
    s.rating,
    s.n_resenas_prod   AS n_resenas,
    s.patrocinado_prod AS es_patrocinado,
    s.pagina_prod      AS pagina,
    NTILE(4) OVER (PARTITION BY s.categoria ORDER BY s.precio_online) AS cuartil_precio,
    s.url
FROM skus s
JOIN productos p ON p.product_id = s.product_id
WHERE s.rn = 1;

CREATE VIEW IF NOT EXISTS v_marcas AS
SELECT
    categoria,
    marca,
    COUNT(*)                                                                      AS productos,
    SUM(n_resenas)                                                                AS resenas,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY categoria), 1)      AS pct_productos,
    ROUND(100.0 * SUM(n_resenas)
          / NULLIF(SUM(SUM(n_resenas)) OVER (PARTITION BY categoria), 0), 1)      AS pct_resenas,
    ROUND(AVG(precio_online), 0)                                                  AS precio_promedio,
    ROUND(AVG(rating), 2)                                                         AS rating_promedio
FROM v_catalogo
GROUP BY categoria, marca;

CREATE VIEW IF NOT EXISTS v_pareto AS
SELECT
    categoria,
    product_id,
    nombre,
    marca,
    n_resenas,
    ROW_NUMBER() OVER w AS ranking,
    ROUND(100.0 * ROW_NUMBER() OVER w / COUNT(*) OVER (PARTITION BY categoria), 1) AS pct_productos_acum,
    ROUND(100.0 * SUM(n_resenas) OVER (w ROWS UNBOUNDED PRECEDING)
          / NULLIF(SUM(n_resenas) OVER (PARTITION BY categoria), 0), 1)            AS pct_resenas_acum
FROM v_catalogo
WINDOW w AS (PARTITION BY categoria ORDER BY n_resenas DESC, product_id);
