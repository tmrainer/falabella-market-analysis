# Validación del piloto – 2026-10-21

Productos distintos capturados: **13164** en 7 categorías (50 páginas por categoría).

## Resumen por categoría

`pct_con_resena` = % de productos con ≥1 reseña; `pct_10_o_mas` = % con ≥10. La mediana se calcula sobre productos (no SKU). Patrocinados cuentan una vez por producto.

| categoria | productos | pct_con_resena | pct_10_o_mas | patrocinados | mediana_resenas |
| --- | --- | --- | --- | --- | --- |
| laptops | 1814 | 10.9 | 2.9 | 33 | 0.0 |
| smartphones | 1979 | 25.5 | 7.6 | 26 | 0.0 |
| televisores | 1954 | 17.9 | 6.2 | 5 | 0.0 |
| zapatillas_deportivas_hombre | 1889 | 44.5 | 15.9 | 20 | 0.0 |
| zapatillas_deportivas_mujer | 1804 | 35.3 | 11.6 | 25 | 0.0 |
| zapatillas_urbanas_hombre | 1811 | 49.6 | 18.1 | 24 | 0.0 |
| zapatillas_urbanas_mujer | 1913 | 40.6 | 14.5 | 24 | 0.0 |

## Posibles reseñas compartidas

Grupos de productos distintos, misma marca, mismo `n_resenas` y `rating`, vendidos por más de un vendedor (umbral n_resenas ≥ 5). Indica que el conteo se agrega por modelo y no por listado; en Fase 2 habría que deduplicar por modelo antes de medir crecimiento.

| categoria | marca | n_resenas | rating | n_productos | n_vendedores | vendedores | ejemplo_nombre |
| --- | --- | --- | --- | --- | --- | --- | --- |
| televisores | SAMSUNG | 980 | 4.8204 | 3 | 3 | Sodimac,Importaciones Huankita,Electrodom | Televisor 50 Smart Tv Mini Led UN50M70HAG UHD 4K M70H Vision AI - Negro |
| zapatillas_deportivas_mujer | ADIDAS | 746 | 4.4129 | 2 | 2 | Triathlon,Falabella | Zapatillas Correr Mujer Questar 3 W |
| zapatillas_urbanas_hombre | ADIDAS | 691 | 4.7033 | 2 | 2 | Sport Life Peru,Falabella | Zapatillas RUN 70s 2.0 Hombre JS0117 |
| zapatillas_deportivas_hombre | ADIDAS | 620 | 4.6 | 2 | 2 | Boutique Boys,Sport Life Peru | Zapatilla Hombre VL Court Base - ID3712 |
| zapatillas_deportivas_hombre | ADIDAS | 557 | 4.7307 | 2 | 2 | Boutique Boys,Triathlon | Zapatilla Hombre Futbol Predator Club Tf - HP9975 |
| smartphones | SAMSUNG | 533 | 4.863 | 2 | 2 | Moviles Telcel,Megacel Peru | Celular Galaxy A37 5G 8GB 256GB Lavanda. |
| smartphones | SAMSUNG | 512 | 4.6738 | 3 | 3 | Millennials,Technoworld.,Falabella | Celular Galaxy A16 128gb Black |
| zapatillas_deportivas_hombre | ADIDAS | 403 | 4.8015 | 2 | 2 | Triathlon,Boutique Boys | Zapatilla Hombre Ownthegame 3.0 - JR6670 |
| zapatillas_deportivas_hombre | ADIDAS | 390 | 4.6744 | 2 | 2 | Triathlon,Falabella | Zapatillas Correr Hombre Ultrarun 5 |
| zapatillas_urbanas_hombre | ADIDAS | 362 | 4.7624 | 2 | 2 | Sport Life Peru,Falabella | Zapatillas BREAK START Hombre KI1252 |
| zapatillas_deportivas_mujer | ADIDAS | 320 | 4.7313 | 2 | 2 | Triathlon,Falabella | Zapatillas Running Mujer Adizero Evo Sl W |
| zapatillas_deportivas_hombre | ADIDAS | 279 | 4.7885 | 2 | 2 | Triathlon,Falabella | Zapatillas Training Hombre Dropset Base |
| zapatillas_deportivas_hombre | ADIDAS | 273 | 4.7912 | 2 | 2 | Boutique Boys,Falabella | Zapatilla Hombre Tenis Dropset Base Trainer M - KJ9169 |
| zapatillas_deportivas_hombre | ADIDAS | 245 | 4.7633 | 2 | 2 | Triathlon,Falabella | Zapatillas Running Hombre Runblaze |
| zapatillas_urbanas_mujer | ADIDAS | 216 | 4.8472 | 2 | 2 | Triathlon,Falabella | Zapatillas Urbanas Mujer Lightblaze |
| zapatillas_urbanas_hombre | ADIDAS | 186 | 4.7419 | 2 | 2 | Triathlon,Falabella | Zapatillas Urbanas Hombre Astrastar |
| televisores | TCL | 185 | 4.6865 | 3 | 3 | Sodimac,Comercial Dylan,Falabella | Televisor 55" Qled 4k 55t6c Google Tv |
| zapatillas_deportivas_hombre | ADIDAS | 179 | 4.4134 | 2 | 2 | Triathlon,Falabella | Zapatillas Football Unisex Predator League Ft tf |
| zapatillas_deportivas_mujer | ADIDAS | 179 | 4.4134 | 2 | 2 | Triathlon,Falabella | Zapatillas Football Unisex Predator League Ft tf |
| laptops | HP | 175 | 4.0971 | 2 | 2 | Dm Computo,Discount Tech Pe | LAPTOP OMNIBOOK X FLIP 16-AS0023DX - INTEL ULTRA 7 256V 16GB 1TBSSD 16″ 2K TACTIL W11 |
| televisores | SAMSUNG | 164 | 4.8598 | 3 | 3 | Sodimac,Tottus,Falabella | Televisor 55" NEO QLED 4K Qn70F Vision Ai Smart Tv (2025) |
| smartphones | APPLE | 152 | 4.9013 | 2 | 2 | Telcel Peru Moviles,Apple Distribuidor Oficial | IPHONE 17 PRO MAX 256GB AZUL INTENSO CHIP FISICO |
| smartphones | APPLE | 151 | 4.9007 | 3 | 3 | Moviles Telcel,Abm Soluciones Tecnologicas,Apple Distribuidor Oficial | IPHONE 17 PRO MAX 256GB AZUL INTENSO CHIP FISICO. |
| smartphones | APPLE | 142 | 4.7817 | 2 | 2 | Abm Soluciones Tecnologicas,Electrogo By Credivargas | IPHONE 16 128GB 6.1” BLACK NANO SIM |
| smartphones | SAMSUNG | 142 | 4.6408 | 2 | 2 | Tottus,Falabella | Celular Galaxy A17 8GB 256GB Negro |
| zapatillas_deportivas_mujer | ADIDAS | 109 | 4.7706 | 2 | 2 | Triathlon,Falabella | Zapatillas Running Mujer Response 2 |
| smartphones | SAMSUNG | 102 | 4.8725 | 4 | 4 | Want,Millennials,Megacel Peru,Carsa Tienda Oficial | Celular Galaxy A37 256GB Gray |
| smartphones | XIAOMI | 100 | 4.34 | 2 | 2 | Global Cel,Newphone | NUEVO 17T PRO 5G 12RAM 512GB REGISTRADO - COLOR NEGRO |
| smartphones | SAMSUNG | 96 | 4.5208 | 2 | 2 | Tottus,Millennials | Celular Galaxy A07 4GB 64GB Negro |
| laptops | HP | 93 | 3.8602 | 2 | 2 | Rois Computer S.a.c.,Grupo R & Q S.a.c | Laptop 15-FD0260LA Intel Core 5 120U, 16Gb Ram, 512Gb SSD 15.6"-B9TX9LA |
| laptops | HP | 84 | 3.9167 | 2 | 2 | Dm Computo,Coolbox | Laptop Victus 15-FB3019LA - Ryzen 7 7445HS RTX 3050 6GB 8GB 512GB SSD 15.6” FHD Windows 11. |
| laptops | HP | 75 | 4.48 | 2 | 2 | Rois Computer S.a.c.,Ix Comercio | Laptop 15-fd0276la Core i7-1355U 16Gb Ram 512Gb SSD 15.6” FHD - B9TZ2LA. |
| televisores | SAMSUNG | 73 | 4.726 | 2 | 2 | Sodimac,Carsa Tienda Oficial | Televisor 65'' UHD U8000H Vision AI Smart TV (2026) |
| zapatillas_deportivas_hombre | ADIDAS | 67 | 4.6716 | 2 | 2 | Triathlon,Falabella | Zapatillas Running Hombre Runblaze |
| zapatillas_deportivas_hombre | PUMA | 63 | 4.6032 | 2 | 2 | Boutique Boys,Treps Sport Peru Srl | ZAPATILLAS CABALLERO CLUB II ERA 397447-02 |
| smartphones | APPLE | 59 | 4.8983 | 2 | 2 | Tottus,Falabella | IPhone 16e 128GB |
| televisores | SAMSUNG | 58 | 4.3276 | 3 | 3 | Sodimac,Comercial Ledd's,Danlu Import | TELEVISOR 32 UN32H5000FG SMART TV 2025 + Antena Digital |
| zapatillas_urbanas_hombre | NEW BALANCE | 57 | 4.7368 | 2 | 2 | Gretel,Triathlon | Zapatillas 2000 Unisex |
| smartphones | SAMSUNG | 53 | 4.7736 | 2 | 2 | Telcel Peru Moviles,Zync Peru | GALAXY A17 4G 256GB 8 BLACK 1SIM |
| televisores | TCL | 41 | 4.439 | 2 | 2 | Sodimac,Falabella | Televisor 55" Qd Miniled 4k 55c6k Google Tv |
