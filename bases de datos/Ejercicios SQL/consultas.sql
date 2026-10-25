-- SELECT pedidos en el ejercicio

-- 1. Todos los productos almacenados
SELECT * FROM Products;

-- 2. Productos con precio mayor a 50000
SELECT * FROM Products
WHERE price > 50000;

-- 3. Todas las compras de un mismo producto por id
--    (cambiar el 2 por el código del producto que se quiera ver)
SELECT * FROM Products_Per_Invoice
WHERE product_code = 2;

-- 4. Compras agrupadas por producto, mostrando el total comprado
SELECT product_code,
       SUM(quantity)     AS total_cantidad,
       SUM(total_amount) AS total_dinero
FROM Products_Per_Invoice
GROUP BY product_code;

-- 5. Todas las facturas del mismo comprador
SELECT * FROM Invoices
WHERE buyer_email = 'maria@example.com';

-- 6. Facturas ordenadas por monto total, de mayor a menor
SELECT * FROM Invoices
ORDER BY total_amount DESC;

-- 7. Una sola factura por número de factura
SELECT * FROM Invoices
WHERE invoice_number = 3;
