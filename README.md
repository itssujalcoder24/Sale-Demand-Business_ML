## Sales & Demand Forecasting for Businesses
<br>

### Project Overview
Accurate sales forecasting is a critical component of business planning, inventory management, and revenue optimization.
This project focuses on analyzing historical sales data and predicting future demand using time-series forecasting techniques.
<br>

- Using the Superstore sales dataset as reference data, this project:
- Aggregates daily sales
- Visualizes historical sales trends
- Builds a forecasting model using Facebook Prophet
- Predicts future sales for the next 180 days
- Exports forecast results for further business analysis
<br>
The final forecast is saved as a structured CSV file (sales_forecast.csv) that can be used by decision-makers, analysts, or integrated into downstream systems.
<br>

### Objectives

- Understand historical sales behavior
- Identify long-term sales trends
- Forecast future sales demand
- Provide actionable insights for business planning
- Demonstrate practical use of time-series forecasting in real-world datasets
<br>

### Dataset Description
Dataset Used: Superstore.csv
<br>
Source: Sample Superstore Sales Dataset
<br>
Encoding: ISO-8859-1
<br>
The dataset contains transactional-level data, which is resampled into daily sales totals for forecasting.
<br>

### Technologies & Libraries
Python
Pandas – Data cleaning & manipulation
Matplotlib – Data visualization
Prophet – Time-series forecasting model
<br>

### Project Workflow
# 1. Data Loading & Preprocessing
CSV file is loaded with the correct encoding
Order Date is parsed as a datetime column
Dataset index is set to Order Date
Sales data is resampled on a daily basis
<br>

# 2. Exploratory Data Analysis
Daily sales trends are visualized using line plots
Helps identify overall growth, seasonality, and fluctuations
<br>

# 3. Time-Series Forecasting
Data is reformatted for Prophet (ds, y)
Prophet model is trained on historical sales
Future sales are predicted for 180 days
Upper and lower confidence intervals are generated
<br>

# 4. Output Generation
Forecast results are saved to a CSV file
Includes predicted values and uncertainty bounds
<br>

## Visualizations
# Daily Sales Trend
- Shows historical sales performance over time, helping identify:
- Business growth
- Seasonal patterns
- Demand volatility
<br>

# Sales Forecast Plot
- Displays:
Predicted future sales
Confidence intervals
Trend continuation beyond historical data
<br>

### Output Files
sales_forecast.csv
<br>

## This file can be used for:
- Inventory planning
- Revenue forecasting
- Business intelligence dashboards
<br>

# How to Run the Project
## 1. Install Dependencies
```bash
pip install pandas matplotlib prophet
```
<br>

# Note: Prophet may require additional build tools depending on your operating system.
<br>

## 2. Place Dataset
Ensure Superstore.csv is present in the project root directory.
<br>

## 3. Run the Script
python sales_forecast.py
<br>

## 4. View Results
- Sales trend plot
- Forecast visualization
- Generated sales_forecast.csv file
<br>

## Business Use Cases
- Retail Demand Forecasting
- Inventory Optimization
- Sales Strategy Planning
- Budget Forecasting
- Trend Analysis
<br>

## Future Enhancements
- Monthly & weekly forecasting views
- Product or category-level forecasting
- Incorporating external factors (holidays, promotions)
- Model performance evaluation (MAE, RMSE)
- Dashboard integration using Streamlit or Power BI
<br>

### Author
Sujal Das
<br>
Engineering Student | Aspiring Data Scientist & ML Engineer