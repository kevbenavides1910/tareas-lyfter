CREATE TABLE `Products`(
    `code` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` VARCHAR(100) NULL,
    `stock_available` INT NOT NULL
);
CREATE TABLE `Invoices`(
    `invoice_number` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `purchase_date` DATE NOT NULL,
    `buyer_email` VARCHAR(150) NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL
);
CREATE TABLE `Products_Per_Invoice`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` INT NOT NULL,
    `product_code` INT NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL
);
CREATE TABLE `Shopping_Cart`(
    `cart_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` VARCHAR(150) NOT NULL
);
CREATE TABLE `Shopping_Cart_Products`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cart_id` INT NOT NULL,
    `product_code` INT NOT NULL,
    `quantity` INT NOT NULL DEFAULT 1
);
ALTER TABLE
    `Products_Per_Invoice` ADD CONSTRAINT `products_per_invoice_invoice_number_foreign` FOREIGN KEY(`invoice_number`) REFERENCES `Invoices`(`invoice_number`);
ALTER TABLE
    `Shopping_Cart_Products` ADD CONSTRAINT `shopping_cart_products_cart_id_foreign` FOREIGN KEY(`cart_id`) REFERENCES `Shopping_Cart`(`cart_id`);
ALTER TABLE
    `Products_Per_Invoice` ADD CONSTRAINT `products_per_invoice_product_code_foreign` FOREIGN KEY(`product_code`) REFERENCES `Products`(`code`);
ALTER TABLE
    `Shopping_Cart_Products` ADD CONSTRAINT `shopping_cart_products_product_code_foreign` FOREIGN KEY(`product_code`) REFERENCES `Products`(`code`);