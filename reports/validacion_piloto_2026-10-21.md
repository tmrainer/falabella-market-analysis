# Validación del piloto – 2026-10-21

Productos distintos capturados: **1752** en 7 categorías (5 páginas por categoría).

## Resumen por categoría

`pct_con_resena` = % de productos con ≥1 reseña; `pct_10_o_mas` = % con ≥10. La mediana se calcula sobre productos (no SKU). Patrocinados cuentan una vez por producto.

| categoria | productos | pct_con_resena | pct_10_o_mas | patrocinados | mediana_resenas |
| --- | --- | --- | --- | --- | --- |
| laptops | 246 | 52.8 | 15.9 | 27 | 1.0 |
| smartphones | 250 | 76.4 | 32.4 | 18 | 5.0 |
| televisores | 242 | 68.6 | 40.5 | 6 | 3.5 |
| zapatillas_deportivas_hombre | 254 | 79.5 | 44.1 | 20 | 7.0 |
| zapatillas_deportivas_mujer | 256 | 78.1 | 32.8 | 19 | 5.0 |
| zapatillas_urbanas_hombre | 253 | 88.1 | 50.6 | 20 | 10.0 |
| zapatillas_urbanas_mujer | 251 | 89.2 | 61.8 | 23 | 16.0 |

## Posibles reseñas compartidas

Grupos de productos distintos, misma marca, mismo `n_resenas` y `rating`, vendidos por más de un vendedor (umbral n_resenas ≥ 5). Indica que el conteo se agrega por modelo y no por listado; en Fase 2 habría que deduplicar por modelo antes de medir crecimiento.

| categoria | marca | n_resenas | rating | n_productos | n_vendedores | vendedores | ejemplo_nombre |
| --- | --- | --- | --- | --- | --- | --- | --- |
| televisores | SAMSUNG | 980 | 4.8204 | 2 | 2 | Sodimac,Electrodom | Televisor 55" Miniled M70HAGXPE TIZEN. |
| smartphones | SAMSUNG | 512 | 4.6738 | 3 | 3 | Millennials,Technoworld.,Falabella | Celular Galaxy A16 128gb Black |
| televisores | TCL | 185 | 4.6865 | 2 | 2 | Sodimac,Falabella | Televisor 55" Qled 4k 55t6c Google Tv |
| laptops | HP | 175 | 4.0971 | 2 | 2 | Dm Computo,Discount Tech Pe | LAPTOP OMNIBOOK X FLIP 16-AS0023DX - INTEL ULTRA 7 256V 16GB 1TBSSD 16″ 2K TACTIL W11 |
| televisores | SAMSUNG | 164 | 4.8598 | 3 | 3 | Sodimac,Tottus,Falabella | Televisor 55" NEO QLED 4K Qn70F Vision Ai Smart Tv (2025) |
| smartphones | SAMSUNG | 142 | 4.6408 | 2 | 2 | Tottus,Falabella | Celular Galaxy A17 8GB 256GB Negro |
| smartphones | SAMSUNG | 96 | 4.5208 | 2 | 2 | Tottus,Millennials | Celular Galaxy A07 4GB 64GB Negro |
| televisores | TCL | 41 | 4.439 | 2 | 2 | Sodimac,Falabella | Televisor 55" Qd Miniled 4k 55c6k Google Tv |
| televisores | TCL | 40 | 4.55 | 2 | 2 | Sodimac,Falabella | Televisor 65" Qd Miniled 4k 65c6k Google Tv |
| televisores | LG | 23 | 4.6087 | 4 | 4 | Tottus,Sodimac,City Tec Peru,Belogar | Televisor 50'' Nano UHD 4K Smart Thinkq AI |
| laptops | LENOVO | 8 | 4.75 | 2 | 2 | A & I Real Colors,Falabella | Laptop Gamer LOQ Essential Serie 7000 AMD Ryzen 7 7735HS RTX 4050 16GB RAM 512GB SSD 15.6" FHD 144Hz |
| zapatillas_urbanas_hombre | PUMA | 7 | 4.7143 | 2 | 2 | Punto Sportivo.,Falabella | Zapatilla Rebound Retro 400197 02 Negro para Hombre |
| smartphones | SAMSUNG | 6 | 4.3333 | 3 | 2 | Miami Import,Usatec Import | GALAXY S25 ULTRA 512GB - BLACK TITANIUM |
| smartphones | SAMSUNG | 6 | 4.6667 | 2 | 2 | Miami Import,Fox Móviles Sac | Galaxy S26 Ultra 256GB 12GB RAM + REGALOS. |
| smartphones | XIAOMI | 6 | 4.8333 | 2 | 2 | Mia Phone,Marketcellperu | 17T PRO 5G 12GB RAM NEGRO 512GB |
| televisores | SAMSUNG | 6 | 4.8333 | 2 | 2 | Electrohogar,Falabella | Televisor 32" HD Smart TV UN32H5000F - Nuevo 2025 |
| zapatillas_deportivas_hombre | PUMA | 6 | 4.8333 | 3 | 2 | Punto Sportivo.,Falabella | Chimpunes Attacanto Ii Tt 108494 01 Negro para Hombre |
| zapatillas_deportivas_mujer | NIKE | 6 | 5.0 | 2 | 2 | Triathlon,Jnk Sport | Zapatillas Football Unisex Tiempo Maestro |
| laptops | LENOVO | 5 | 4.8 | 2 | 2 | Charatec,Tottus | Laptop LOQ Essential AMD Ryzen 7 16GB RAM 512GB SSD RTX 4050 6GB 15.6" FHD 144Hz |
| televisores | LG | 5 | 4.8 | 2 | 2 | Electrohogar,Falabella | Televisor 100" QNED evo MiniLED AI 4K Smart TV 2026 100QNED85BS |
