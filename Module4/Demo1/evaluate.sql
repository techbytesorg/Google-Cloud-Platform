-- Check how the model trained
SELECT * FROM ML.TRAINING_INFO(MODEL `ga4_data.pageview_forecast_model`);


-- Get evaluation metrics
SELECT * FROM ML.EVALUATE(MODEL `ga4_data.pageview_forecast_model`);