CREATE OR REPLACE MODEL `ga4_data.sales_regression_model`
OPTIONS(
 model_type = 'linear_reg',
 input_label_cols = ['total_sales']
) AS
SELECT
 item_sold,
 store_size,
 ad_spend,
 total_sales
FROM
 `ga4_data.sales_data`;