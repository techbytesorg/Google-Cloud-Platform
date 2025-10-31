CREATE OR REPLACE TABLE `ga4_data.sales_data` AS
SELECT * FROM UNNEST([
  STRUCT(1 AS store_id, 100 AS item_sold, 1200 AS store_size, 500 AS ad_spend, 15000 AS total_sales),
  STRUCT(2 AS store_id, 80  AS item_sold, 900  AS store_size, 400 AS ad_spend, 12000 AS total_sales),
  STRUCT(3 AS store_id, 150 AS item_sold, 1500 AS store_size, 900 AS ad_spend, 22000 AS total_sales),
  STRUCT(4 AS store_id, 50  AS item_sold, 600  AS store_size, 200 AS ad_spend, 8000  AS total_sales),
  STRUCT(5 AS store_id, 120 AS item_sold, 1300 AS store_size, 700 AS ad_spend, 18000 AS total_sales),
  STRUCT(6 AS store_id, 130 AS item_sold, 1400 AS store_size, 800 AS ad_spend, 19500 AS total_sales),
  STRUCT(7 AS store_id, 70  AS item_sold, 700  AS store_size, 300 AS ad_spend, 10000 AS total_sales)
]);