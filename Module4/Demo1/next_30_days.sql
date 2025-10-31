SELECT
 forecast_timestamp AS date,
 forecast_value AS predicted_pageviews,
 confidence_level,
 prediction_interval_lower_bound AS lower_bound,
 prediction_interval_upper_bound AS upper_bound
FROM ML.FORECAST(MODEL `ga4_data.pageview_forecast_model`,
                STRUCT(30 AS horizon, 0.95 AS confidence_level))
ORDER BY date;