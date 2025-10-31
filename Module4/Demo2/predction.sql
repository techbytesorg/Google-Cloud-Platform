SELECT
 *
FROM
 ML.PREDICT(
   MODEL `ga4_data.sales_regression_model`,
   (
     SELECT
       110 AS item_sold,
       1000 AS store_size,
       600 AS ad_spend
   )
 );