-- Train an ARIMA_PLUS model for forecasting
CREATE OR REPLACE MODEL `ga4_data.pageview_forecast_model`
OPTIONS(
 model_type='ARIMA_PLUS',
 time_series_timestamp_col='date',
 time_series_data_col='pageview',
 holiday_region='US'
) AS
SELECT
 date,
 pageviews
FROM `ga4_data.daily_pageviews`;


