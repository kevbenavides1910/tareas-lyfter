-- Ejercicios de SQL - creación de la base de datos
-- Las tablas son las mismas del ejercicio anterior (tienda), pasadas de MySQL a SQLite.
--
-- Cosas que cambié respecto al export de MySQL:
--  * INT AUTO_INCREMENT  ->  INTEGER PRIMARY KEY AUTOINCREMENT  (así el código se genera solo)
--  * VARCHAR(n) / DECIMAL(10,2) / DATE -> text y numeric, porque SQLite no tiene esos tipos
--    exactos (solo afinidad). Las fechas se guardan como texto ISO: '2026-10-25'.
--  * En MySQL las FK se agregaban después con ALTER TABLE ... ADD CONSTRAINT.
--    SQLite no permite eso, así que las FK van declaradas dentro del CREATE TABLE.
--  * Las FK en SQLite no se validan por defecto: hay que ejecutar
--    PRAGMA foreign_keys = ON; en cada conexión (esto no queda guardado en el archivo).
--  * SQLite no tiene decimal exacto; numeric(10,2) se guarda como número flotante,
--    por eso le puse check para evitar precios negativos.

PRAGMA foreign_keys = ON;

CREATE TABLE Products (
    code            INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL,
    price           NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    entry_date      TEXT NOT NULL,
    brand           TEXT,
    stock_available INTEGER NOT NULL CHECK (stock_available >= 0)
);

CREATE TABLE Invoices (
    invoice_number  INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date   TEXT NOT NULL,
    buyer_email     TEXT NOT NULL,
    total_amount    NUMERIC(10,2) NOT NULL CHECK (total_amount >= 0)
);

CREATE TABLE Products_Per_Invoice (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number  INTEGER NOT NULL REFERENCES Invoices(invoice_number),
    product_code    INTEGER NOT NULL REFERENCES Products(code),
    quantity        INTEGER NOT NULL CHECK (quantity > 0),
    total_amount    NUMERIC(10,2) NOT NULL CHECK (total_amount >= 0)
);

CREATE TABLE Shopping_Cart (
    cart_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email     TEXT NOT NULL
);

CREATE TABLE Shopping_Cart_Products (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id         INTEGER NOT NULL REFERENCES Shopping_Cart(cart_id),
    product_code    INTEGER NOT NULL REFERENCES Products(code),
    quantity        INTEGER NOT NULL DEFAULT 1 CHECK (quantity > 0)
);

-- Punto del ALTER TABLE: teléfono del comprador y código del cajero.
-- Ojo: SQLite solo permite agregar columnas con ALTER, no agregarles PK ni CHECK
-- a una columna que ya existe, por eso las dos quedan sin restricciones.
-- El código de empleado no lleva FK porque en el diseño original no existe una
-- tabla de empleados; si la tuviera, sería REFERENCES Employees(code).
ALTER TABLE Invoices ADD COLUMN buyer_phone TEXT;
ALTER TABLE Invoices ADD COLUMN employee_code INTEGER;
