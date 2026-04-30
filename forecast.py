import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 1. Load your Excel data
df = pd.read_excel("ICICI_Financials.xlsx")

# -------------------------------
# Net Profit Scenario Forecasting
# -------------------------------
series = df["Net Profit"]
model = ARIMA(series, order=(1,1,1))
model_fit = model.fit()

# Base forecast
base_forecast = model_fit.forecast(steps=5)

# Scenario adjustments
optimistic_forecast = base_forecast * 1.10   # +10% growth
pessimistic_forecast = base_forecast * 0.90  # -10% stress

future_years = list(range(df["Year"].iloc[-1]+1, df["Year"].iloc[-1]+6))

# Plot scenarios
plt.figure(figsize=(8,5))
plt.plot(df["Year"], series, label="Historical Net Profit", color="blue")
plt.plot(future_years, base_forecast, marker="o", color="red", label="Base Forecast")
plt.plot(future_years, optimistic_forecast, marker="o", color="green", label="Optimistic (+10%)")
plt.plot(future_years, pessimistic_forecast, marker="o", color="orange", label="Pessimistic (-10%)")
plt.xlabel("Year")
plt.ylabel("Net Profit")
plt.title("Scenario Forecasting Net Profit (ARIMA)")
plt.legend()
plt.savefig("scenario_forecast_net_profit.png")
plt.show()

# -------------------------------
# CAR% Scenario Forecasting
# -------------------------------
series = df["CAR%"]
model = ARIMA(series, order=(1,1,1))
model_fit = model.fit()

# Base forecast
base_forecast = model_fit.forecast(steps=5)

# Scenario adjustments
optimistic_forecast = base_forecast * 1.05   # +5% improvement
pessimistic_forecast = base_forecast * 0.95  # -5% stress

future_years = list(range(df["Year"].iloc[-1]+1, df["Year"].iloc[-1]+6))

# Plot scenarios
plt.figure(figsize=(8,5))
plt.plot(df["Year"], series, label="Historical CAR%", color="blue")
plt.plot(future_years, base_forecast, marker="o", color="red", label="Base Forecast")
plt.plot(future_years, optimistic_forecast, marker="o", color="green", label="Optimistic (+5%)")
plt.plot(future_years, pessimistic_forecast, marker="o", color="orange", label="Pessimistic (-5%)")
plt.xlabel("Year")
plt.ylabel("CAR%")
plt.title("Scenario Forecasting CAR% (ARIMA)")
plt.legend()
plt.savefig("scenario_forecast_car.png")
plt.show()
