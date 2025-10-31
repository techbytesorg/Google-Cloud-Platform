WITH historical AS (
 SELECT
   date,
   pageview AS actual_pageviews,
   NULL AS predicted_pageviews
 FROM `ga4_data.daily_pageviews`
),
forecast AS (
 SELECT
   date(forecast_timestamp) AS date,
   NULL AS actual_pageviews,
   forecast_value AS predicted_pageviews
 FROM ML.FORECAST(MODEL `ga4_data.pageview_forecast_model`,
                  STRUCT(30 AS horizon))
)
SELECT * FROM historical
UNION ALL
SELECT * FROM forecast
ORDER BY date;


