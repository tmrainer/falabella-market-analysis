# Fase 0 – Exploración técnica de falabella.com.pe (2026-10-21)

## 1. robots.txt

Copia guardada en `robots_falabella_2026-10-21.txt`.

- `User-agent: *` con `Disallow:` vacío → rastreo permitido en todo el sitio.
- Únicas rutas bloqueadas: `/cgi-bin/`, `/falabella-pe/basket*`, `/falabella-pe/myaccount*`,
  `/falabella-pe/checkout*`, `/falabella-pe/orders*`. Ninguna es una página de categoría.
- Publica sitemaps (categorías, marcas, productos, vendedores). El de categorías tiene 2,761 URLs.

Conclusión: las páginas `/falabella-pe/category/<id>/<slug>` son rastreables.
Igual aplicamos ritmo lento (3–5 s entre requests) y paramos ante 403/429.

## 2. Cómo entrega los datos una página de categoría

- El sitio es **Next.js con renderizado en servidor (SSR)**.
- El HTML (~2.1 MB) incluye `<script id="__NEXT_DATA__" type="application/json">` con el estado
  completo de la página. Los productos están en `props.pageProps.results` y la paginación en
  `props.pageProps.pagination` (`count`, `perPage`=48, `currentPage`).
- Paginación por query string: `?page=N`.
- **No existe API pública de listado de categorías.** El campo `listingUrl` apunta a un servicio
  interno (`*.svc.cluster.local`). El bundle JS solo expone `/s/browse/v1/search/` (buscador),
  `/s/browse/v3/product/` (detalle) y `typeahead`.

### Campos relevantes por producto (`results[i]`)

| campo JSON        | uso en el proyecto                         |
|-------------------|--------------------------------------------|
| `productId`       | `product_id` (identidad del producto)      |
| `skuId`           | `sku_id` (variante: color/talla)           |
| `displayName`     | `nombre`                                   |
| `brand`           | `marca`                                    |
| `sellerName`, `sellerId` | `vendedor`, `vendedor_id`           |
| `prices[]`        | lista con `type` ∈ {cmrPrice, internetPrice, eventPrice, normalPrice} |
| `rating`          | texto, ej. `"4.375"`, puede faltar          |
| `totalReviews`    | texto, ej. `"8"`, puede faltar              |
| `isSponsored`     | `es_patrocinado`                           |
| `url`             | `url`                                      |

### Mapeo de precios (verificado en ~1,000 productos)

- `precio_cmr`    ← `cmrPrice`
- `precio_online` ← `eventPrice` si existe, si no `internetPrice` (en campaña el evento reemplaza al internet)
- `precio_lista`  ← `normalPrice` (siempre viene con `crossed: true`, es el precio tachado)
- Los precios llegan como texto con separador de miles: `"1,029.90"` → `1029.90`.

### Patrocinados

`isSponsored: true` y un `adIdentifier`. Vienen **además** de los 48 orgánicos (p. ej. 51 = 48 + 3).
Ocupan las primeras posiciones. `posicion_en_pagina` se cuenta sobre la lista completa (con patrocinados)
porque es lo que ve el usuario.

### Datos personales

El listado NO incluye textos ni autores de reseñas; solo el conteo y el promedio. No se descargan
páginas de producto ni reseñas individuales.

## 3. Tamaño de catálogo y cobertura de reseñas (página 1, orden por relevancia)

| categoría                   | id          | catálogo | con ≥1 reseña | con ≥10 | patroc. | vendedores |
|-----------------------------|-------------|---------:|--------------:|--------:|--------:|-----------:|
| Smartphones                 | CATG15605   |    7,229 |         42/51 |      29 |       3 |         15 |
| Zapatillas urbanas hombre   | cat1480500  |    3,358 |         54/56 |      34 |       8 |          5 |
| Zapatillas urbanas mujer    | cat1470534  |    4,579 |         54/56 |      46 |       8 |          2 |
| Zapatillas deportivas mujer | cat16200461 |    3,069 |         51/56 |      30 |       8 |          5 |
| Televisores Smart TV        | cat6370551  |   10,711 |         46/48 |      42 |       0 |          7 |
| Laptops                     | cat40712    |   12,041 |         42/48 |      17 |       0 |         11 |
| Refrigerador (descartada)   | cat780530   |    3,201 |         49/49 |      30 |       1 |          5 |
| ZAPATILLAS MUJER (muerta)   | J1004       |        4 |             0 |       0 |       0 |          1 |

Decisión: 7 categorías = Smartphones, Televisores, Laptops + zapatillas urbanas/deportivas × hombre/mujer.
Las 4 de zapatillas son simétricas y permiten comparar género y tipo. `J1004` se descartó (4 productos).

## 4. Enfoque elegido

`requests` + extracción de `__NEXT_DATA__` con regex + `json`. Sin navegador headless (no hace falta
ejecutar JS) y sin parser de DOM (las clases CSS cambian; el contrato JSON es más estable).
Respuestas crudas guardadas en gzip (2.1 MB → ~256 KB por página) para re-parsear sin re-descargar.
