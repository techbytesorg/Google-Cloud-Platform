CREATE OR REPLACE VIEW `ga4_data.daily_pageviews` AS
SELECT
 PARSE_DATE('%Y%m%d', event_date) AS date,
 COUNT(*) AS pageviews
FROM `g4a-eda-example.ga4_data.events_*`
WHERE event_name = 'page_view'
GROUP BY date
ORDER BY date;


select * from `ga4_data.daily_pageviews`
