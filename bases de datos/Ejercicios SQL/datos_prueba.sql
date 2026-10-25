-- Datos de prueba para poder correr los SELECT

PRAGMA foreign_keys = ON;

INSERT INTO Products (name, price, entry_date, brand, stock_available) VALUES
    ('Laptop 14"',        450000, '2026-09-01', 'Lenovo',   12),
    ('Mouse inalámbrico',  12000, '2026-09-02', 'Logitech', 80),
    ('Teclado mecánico',   25000, '2026-09-05', 'Redragon', 45),
    ('Monitor 24"',       180000, '2026-09-10', 'Samsung',  18),
    ('Audífonos',          60000, '2026-09-12', 'Sony',     30),
    ('Webcam HD',          55000, '2026-09-15', 'Logitech', 22),
    ('Silla ergonómica',   95000, '2026-09-20', 'Herman',    9);

INSERT INTO Invoices (purchase_date, buyer_email, total_amount, buyer_phone, employee_code) VALUES
    ('2026-10-01', 'maria@example.com',  474000, '8888-1111', 1),
    ('2026-10-05', 'juan@example.com',   180000, '7777-2222', 2),
    ('2026-10-12', 'carlos@example.com', 135000, '6666-3333', 3),
    ('2026-10-20', 'maria@example.com',  155000, '8888-1111', 2);

INSERT INTO Products_Per_Invoice (invoice_number, product_code, quantity, total_amount) VALUES
    (1, 1, 1, 450000),
    (1, 2, 2,  24000),
    (2, 4, 1, 180000),
    (3, 6, 2, 110000),
    (3, 3, 1,  25000),
    (4, 5, 1,  60000),
    (4, 7, 1,  95000);

INSERT INTO Shopping_Cart (buyer_email) VALUES
    ('maria@example.com'),
    ('carlos@example.com');

INSERT INTO Shopping_Cart_Products (cart_id, product_code, quantity) VALUES
    (1, 2, 1),
    (1, 5, 2),
    (2, 4, 1);
