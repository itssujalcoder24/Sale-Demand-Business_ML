import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

df = pd.read_csv('Superstore.csv', encoding='ISO-8859-1', parse_dates=['Order Date'])
df.set_index('Order Date', inplace=True)

daily_sales = df.resample('D').sum()['Sales'].reset_index()
daily_sales.columns = ['Date', 'Sales']

plt.figure(figsize=(12, 5))
plt.plot(daily_sales['Date'], daily_sales['Sales'], color='darkblue')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

df_prophet = daily_sales.rename(columns={'Date': 'ds', 'Sales': 'y'})

model = Prophet()
model.fit(df_prophet)

future = model.make_future_dataframe(periods=180)
forecast = model.predict(future)

model.plot(forecast)
plt.title("Sales Forecast (Prophet)")
plt.xlabel("Date")
plt.ylabel("Predicted Sales")
plt.tight_layout()
plt.show()

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("sales_forecast.csv", index=False)