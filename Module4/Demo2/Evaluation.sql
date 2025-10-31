SELECT
 mean_absolute_error,
 mean_squared_error,
 r2_score
FROM
 ML.EVALUATE(MODEL `ga4_data.sales_regression_model`);