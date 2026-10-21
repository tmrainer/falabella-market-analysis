CREATE TABLE IF NOT EXISTS productos (
    product_id        TEXT PRIMARY KEY,
    nombre            TEXT,
    marca             TEXT,
    url               TEXT,
    categoria_origen  TEXT,
    primera_captura   TEXT NOT NULL,
    ultima_captura    TEXT NOT NULL
);

-- una fila por producto/sku por fecha; la fecha en la PK permite comparar capturas
CREATE TABLE IF NOT EXISTS capturas (
    fecha_captura      TEXT    NOT NULL,
    categoria          TEXT    NOT NULL,
    product_id         TEXT    NOT NULL,
    sku_id             TEXT    NOT NULL,
    vendedor           TEXT,
    vendedor_id        TEXT,
    precio_cmr         REAL,
    precio_online      REAL,
    precio_lista       REAL,
    rating             REAL,
    n_resenas          INTEGER,
    posicion_en_pagina INTEGER NOT NULL,
    pagina             INTEGER NOT NULL,
    es_patrocinado     INTEGER NOT NULL DEFAULT 0,
    url                TEXT,
    PRIMARY KEY (fecha_captura, categoria, product_id, sku_id),
    FOREIGN KEY (product_id) REFERENCES productos(product_id)
);

CREATE INDEX IF NOT EXISTS idx_capturas_producto ON capturas(product_id, fecha_captura);
CREATE INDEX IF NOT EXISTS idx_capturas_categoria_fecha ON capturas(categoria, fecha_captura);

CREATE TABLE IF NOT EXISTS corridas (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_captura   TEXT NOT NULL,
    inicio          TEXT NOT NULL,
    fin             TEXT,
    paginas_ok      INTEGER DEFAULT 0,
    filas_cargadas  INTEGER DEFAULT 0,
    estado          TEXT,
    detalle         TEXT
);
