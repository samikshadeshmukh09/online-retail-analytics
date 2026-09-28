CREATE DATABASE online_retail_analytics;
USE online_retail_analytics;
SELECT DATABASE();

CREATE TABLE sales (
    original_row_id BIGINT PRIMARY KEY,
    invoice VARCHAR(20),
    stockcode VARCHAR(30),
    description VARCHAR(255),
    quantity INT,
    invoice_date DATETIME,
    price DECIMAL(10,2),
    customer_id BIGINT NULL,
    country VARCHAR(100),
    year INT,
    month INT,
    month_name VARCHAR(20),
    day INT,
    day_name VARCHAR(20),
    hour INT,
    is_cancelled TINYINT,
    is_return TINYINT,
    is_invalid_price TINYINT,
    is_invalid_quantity TINYINT,
    transaction_type VARCHAR(20),
    revenue DECIMAL(15,2),
    customer_status VARCHAR(30)
);
SHOW TABLES;
SET GLOBAL local_infile = 1;
SHOW VARIABLES LIKE 'local_infile';

LOAD DATA LOCAL INFILE 'D:/online_retail_II project folder/output/dashboard_sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
DESCRIBE sales;
SELECT COUNT(*) AS total_rows
FROM sales;

SELECT
    MIN(invoice_date) AS first_transaction,
    MAX(invoice_date) AS last_transaction
FROM sales;

SELECT
    COUNT(DISTINCT customer_id) AS total_customers
FROM sales
WHERE customer_id IS NOT NULL;

SELECT
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales;

SELECT
    SUM(quantity) AS total_quantity_sold
FROM sales;

SELECT
    COUNT(DISTINCT invoice) AS total_orders
FROM sales;

SELECT
    ROUND(
        SUM(revenue) / COUNT(DISTINCT invoice),
        2
    ) AS average_order_value
FROM sales;

SELECT
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS total_quantity_sold,
    COUNT(DISTINCT invoice) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(
        SUM(revenue) / COUNT(DISTINCT invoice),
        2
    ) AS average_order_value
FROM sales;

3. DATA VALIDATION
-- ============================================================

-- Total number of records
SELECT COUNT(*) AS total_rows
FROM sales;

-- Check duplicate original row IDs
SELECT
    original_row_id,
    COUNT(*) AS duplicate_count
FROM sales
GROUP BY original_row_id
HAVING COUNT(*) > 1;

-- Check critical missing values
SELECT
    SUM(invoice IS NULL) AS missing_invoice,
    SUM(stockcode IS NULL) AS missing_stockcode,
    SUM(quantity IS NULL) AS missing_quantity,
    SUM(price IS NULL) AS missing_price,
    SUM(invoice_date IS NULL) AS missing_invoice_date
FROM sales;

-- Check date range
SELECT
    MIN(invoice_date) AS first_transaction,
    MAX(invoice_date) AS last_transaction
FROM sales;

-- ============================================================
-- 4. OVERALL BUSINESS KPIs
-- ============================================================

SELECT
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS total_quantity_sold,
    COUNT(DISTINCT invoice) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(
        SUM(revenue) / COUNT(DISTINCT invoice),
        2
    ) AS average_order_value
FROM sales;

-- ============================================================
-- 5. MONTHLY SALES ANALYSIS
-- ============================================================

-- Monthly revenue
SELECT
    year,
    month,
    month_name,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY year, month, month_name
ORDER BY year, month;

-- Monthly orders
SELECT
    year,
    month,
    month_name,
    COUNT(DISTINCT invoice) AS total_orders
FROM sales
GROUP BY year, month, month_name
ORDER BY year, month;

-- Monthly quantity
SELECT
    year,
    month,
    month_name,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY year, month, month_name
ORDER BY year, month;

-- Combined monthly performance
SELECT
    year,
    month,
    month_name,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoice) AS total_orders,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY year, month, month_name
ORDER BY year, month;

-- ============================================================
-- 6. PRODUCT ANALYSIS
-- ============================================================

-- Top 10 products by revenue
SELECT
    stockcode,
    description,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY stockcode, description
ORDER BY total_revenue DESC
LIMIT 10;

-- Top 10 products by quantity sold
SELECT
    stockcode,
    description,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY stockcode, description
ORDER BY total_quantity DESC
LIMIT 10;

-- Overall product performance
SELECT
    stockcode,
    description,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(AVG(price), 2) AS average_price
FROM sales
GROUP BY stockcode, description
ORDER BY total_revenue DESC
LIMIT 10;

-- Number of unique products
SELECT
    COUNT(DISTINCT stockcode) AS unique_products
FROM sales;

-- ============================================================
-- 7. CUSTOMER ANALYSIS
-- ============================================================

-- Top 10 customers by revenue
SELECT
    customer_id,
    COUNT(DISTINCT invoice) AS total_orders,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
WHERE customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;

-- Customers with the most orders
SELECT
    customer_id,
    COUNT(DISTINCT invoice) AS total_orders
FROM sales
WHERE customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY total_orders DESC
LIMIT 10;

-- Repeat customers
SELECT
    customer_id,
    COUNT(DISTINCT invoice) AS total_orders
FROM sales
WHERE customer_id IS NOT NULL
GROUP BY customer_id
HAVING COUNT(DISTINCT invoice) > 1
ORDER BY total_orders DESC;

-- Count repeat customers
SELECT
    COUNT(*) AS repeat_customers
FROM (
    SELECT
        customer_id
    FROM sales
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
    HAVING COUNT(DISTINCT invoice) > 1
) AS customer_orders;

-- Average revenue per customer
SELECT
    ROUND(
        SUM(revenue) / COUNT(DISTINCT customer_id),
        2
    ) AS average_customer_revenue
FROM sales
WHERE customer_id IS NOT NULL;

-- ============================================================
-- 8. COUNTRY / GEOGRAPHICAL ANALYSIS
-- ============================================================

-- Revenue by country
SELECT
    country,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY country
ORDER BY total_revenue DESC;

-- Top 10 countries
SELECT
    country,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoice) AS total_orders,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY country
ORDER BY total_revenue DESC
LIMIT 10;

-- United Kingdom vs other countries
SELECT
    CASE
        WHEN country = 'United Kingdom'
            THEN 'United Kingdom'
        ELSE 'Other Countries'
    END AS country_group,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY country_group
ORDER BY total_revenue DESC;

-- ============================================================
-- 9. TIME-BASED ANALYSIS
-- ============================================================

-- Sales by hour
SELECT
    hour,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoice) AS total_orders
FROM sales
GROUP BY hour
ORDER BY hour;

-- Sales by day of week
SELECT
    day_name,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoice) AS total_orders
FROM sales
GROUP BY day_name
ORDER BY total_revenue DESC;

-- ============================================================
-- 10. TRANSACTION ANALYSIS
-- ============================================================

-- Transaction type distribution
SELECT
    transaction_type,
    COUNT(*) AS transaction_rows,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY transaction_type
ORDER BY transaction_rows DESC;

-- Cancelled transactions
SELECT
    COUNT(*) AS cancelled_rows
FROM sales
WHERE is_cancelled = 1;

-- Return transactions
SELECT
    COUNT(*) AS return_rows
FROM sales
WHERE is_return = 1;

-- ============================================================
-- 11. CUSTOMER STATUS ANALYSIS
-- ============================================================

SELECT
    customer_status,
    COUNT(*) AS transaction_rows,
    COUNT(DISTINCT invoice) AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY customer_status
ORDER BY total_revenue DESC;

-- ============================================================
-- 12. USEFUL INTERVIEW QUERIES
-- ============================================================

-- WHERE vs HAVING example:
-- Find customers who placed more than one order
SELECT
    customer_id,
    COUNT(DISTINCT invoice) AS total_orders
FROM sales
WHERE customer_id IS NOT NULL
GROUP BY customer_id
HAVING COUNT(DISTINCT invoice) > 1
ORDER BY total_orders DESC;

-- Highest revenue-generating month
SELECT
    year,
    month,
    month_name,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY year, month, month_name
ORDER BY total_revenue DESC
LIMIT 1;

-- Highest revenue-generating product
SELECT
    stockcode,
    description,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY stockcode, description
ORDER BY total_revenue DESC
LIMIT 1;
