-- bloques "-- @nombre", parametro :fecha

-- @productos_por_categoria
SELECT
    categoria,
    product_id,
    MAX(COALESCE(n_resenas, 0)) AS n_resenas,
    MAX(es_patrocinado)         AS es_patrocinado
FROM capturas
WHERE fecha_captura = :fecha
GROUP BY categoria, product_id;

-- @resumen_categoria
SELECT
    categoria,
    COUNT(*)                                          AS productos,
    ROUND(100.0 * SUM(n_resenas >= 1)  / COUNT(*), 1) AS pct_con_resena,
    ROUND(100.0 * SUM(n_resenas >= 10) / COUNT(*), 1) AS pct_10_o_mas,
    SUM(es_patrocinado)                               AS patrocinados
FROM (
    SELECT categoria, product_id,
           MAX(COALESCE(n_resenas, 0)) AS n_resenas,
           MAX(es_patrocinado)         AS es_patrocinado
    FROM capturas
    WHERE fecha_captura = :fecha
    GROUP BY categoria, product_id
)
GROUP BY categoria
ORDER BY categoria;

-- @resenas_compartidas
-- productos distintos con misma marca, n_resenas y rating en mas de un vendedor
SELECT
    c.categoria,
    p.marca,
    c.n_resenas,
    c.rating,
    COUNT(DISTINCT c.product_id)      AS n_productos,
    COUNT(DISTINCT c.vendedor)        AS n_vendedores,
    GROUP_CONCAT(DISTINCT c.vendedor) AS vendedores,
    MIN(p.nombre)                     AS ejemplo_nombre
FROM capturas c
JOIN productos p ON p.product_id = c.product_id
WHERE c.fecha_captura = :fecha
  AND c.n_resenas >= 5
GROUP BY c.categoria, p.marca, c.n_resenas, c.rating
HAVING COUNT(DISTINCT c.vendedor) > 1
ORDER BY c.n_resenas DESC, c.categoria
LIMIT 40;
