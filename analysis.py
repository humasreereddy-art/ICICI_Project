import pandas as pd
import matplotlib.pyplot as plt

# 1. Load your Excel file
df = pd.read_excel("ICICI_Financials.xlsx")

# 2. Print first few rows to confirm
print(df.head())

# 3. Plot ROA vs ROE
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["ROA"], label="ROA")
plt.plot(df["Year"], df["ROE"], label="ROE")
plt.xlabel("Year")
plt.ylabel("Ratio")
plt.title("ROA vs ROE")
plt.legend()
plt.savefig("roa_vs_roe.png")
plt.show()

# 4. Plot Loan Growth % vs Net Profit Growth %
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Loan Growth %"], label="Loan Growth %")
plt.plot(df["Year"], df["Net Profit Growth %"], label="Net Profit Growth %")
plt.xlabel("Year")
plt.ylabel("Growth %")
plt.title("Loan Growth vs Net Profit Growth")
plt.legend()
plt.savefig("loan_vs_profit_growth.png")
plt.show()

# 5. Plot Current Ratio vs Quick Ratio
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Current Ratio"], label="Current Ratio")
plt.plot(df["Year"], df["Quick Ratio"], label="Quick Ratio")
plt.xlabel("Year")
plt.ylabel("Ratio")
plt.title("Liquidity Ratios")
plt.legend()
plt.savefig("liquidity_ratios.png")
plt.show()

# 6. Plot Loan Growth % vs Net NPA % (Digital Lending Analysis)
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Loan Growth %"], label="Loan Growth %")
plt.plot(df["Year"], df["Net NPA %"], label="Net NPA %")
plt.xlabel("Year")
plt.ylabel("Percentage")
plt.title("Loan Growth vs Net NPA %")
plt.legend()
plt.savefig("loan_vs_npa.png")   # save graph
plt.show()

import numpy as np

# 7. Risk Management: Stress Testing Net Profit vs NPA
stress_levels = [0.01, 0.02, 0.05, 0.10]  # 1%, 2%, 5%, 10% stress scenarios
base_profit = df["Net Profit"].iloc[-1]   # latest year's profit

stress_results = []
for stress in stress_levels:
    stressed_profit = base_profit * (1 - stress*10)  # simple stress model
    stress_results.append((stress, stressed_profit))

stress_df = pd.DataFrame(stress_results, columns=["Stress Level (NPA)", "Stressed Net Profit"])
print(stress_df)

plt.figure(figsize=(8,5))
plt.bar(stress_df["Stress Level (NPA)"], stress_df["Stressed Net Profit"], color="tomato")
plt.xlabel("Stress Level (NPA)")
plt.ylabel("Stressed Net Profit")
plt.title("Risk Management: Stress Testing Net Profit vs NPA")
plt.savefig("risk_stress_test.png")   # save graph
plt.show()

# 8. Risk Management: Monte Carlo Simulation on Net Profit
simulations = 10000  # number of random runs
mean_npa = df["Net NPA %"].mean() / 100   # average NPA as probability
std_npa = df["Net NPA %"].std() / 100     # standard deviation

base_profit = df["Net Profit"].iloc[-1]   # latest year's profit

# Generate random NPA values
random_npa = np.random.normal(mean_npa, std_npa, simulations)

# Calculate simulated profits
simulated_profits = base_profit * (1 - random_npa*10)

# Plot histogram of simulated profits
plt.figure(figsize=(8,5))
plt.hist(simulated_profits, bins=50, color="skyblue", edgecolor="black")
plt.xlabel("Simulated Net Profit")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation: Net Profit under NPA Uncertainty")
plt.savefig("monte_carlo_net_profit.png")   # save graph
plt.show()

# Print probability of profit falling below a threshold
threshold = base_profit * 0.7  # e.g., 30% drop
probability = (simulated_profits < threshold).mean()
print(f"Probability Net Profit falls below {threshold:.2f}: {probability*100:.2f}%")

# 9. Capital Efficiency: CAR% Trend
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["CAR%"], marker="o", color="green", label="CAR%")
plt.xlabel("Year")
plt.ylabel("CAR%")
plt.title("Capital Efficiency: CAR% Trend")
plt.legend()
plt.savefig("car_trend.png")   # save graph
plt.show()

import seaborn as sns
import numpy as np

# Create bins for Loan Growth % and Net NPA %
loan_bins = pd.cut(df["Loan Growth %"], bins=5)
npa_bins = pd.cut(df["Net NPA %"], bins=5)

# Pivot table: average Net Profit for each bin combination
heatmap_data = df.pivot_table(values="Net Profit",
                              index=npa_bins,
                              columns=loan_bins,
                              aggfunc=np.mean)

plt.figure(figsize=(8,6))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlOrRd")
plt.title("Risk Heatmap: Net Profit vs Loan Growth & NPA")
plt.xlabel("Loan Growth % bins")
plt.ylabel("Net NPA % bins")
plt.savefig("risk_heatmap.png")
plt.show()

# Average ROA and ROE
avg_roa = df["ROA"].mean()
avg_roe = df["ROE"].mean()

# Worst-case Net Profit (from your Monte Carlo simulation results)
# For now, take the minimum historical Net Profit as a proxy
worst_case_profit = df["Net Profit"].min()

# Forecasted CAR% in 2030 (from your scenario forecast)
# For simplicity, take the last forecasted CAR% base value
forecasted_car_2030 = 0.1655  # Replace with your ARIMA forecast value

summary_data = {
    "Average ROA (2015–2025)": round(avg_roa, 2),
    "Average ROE (2015–2025)": round(avg_roe, 2),
    "Worst-case Net Profit": round(worst_case_profit, 2),
    "Forecasted CAR% in 2030": round(forecasted_car_2030, 4)
}

summary_df = pd.DataFrame(list(summary_data.items()), columns=["Metric", "Value"])
print(summary_df)

# --- Executive Summary Table ---
avg_roa = df["ROA"].mean()
avg_roe = df["ROE"].mean()
worst_case_profit = df["Net Profit"].min()
forecasted_car_2030 = 0.1655  # replace with your ARIMA forecast value

summary_data = {
    "Average ROA (2015–2025)": round(avg_roa, 2),
    "Average ROE (2015–2025)": round(avg_roe, 2),
    "Worst-case Net Profit": round(worst_case_profit, 2),
    "Forecasted CAR% in 2030": round(forecasted_car_2030, 4)
}

summary_df = pd.DataFrame(list(summary_data.items()), columns=["Metric", "Value"])

# Save as CSV for reuse
summary_df.to_csv("executive_summary.csv", index=False)

print("\nExecutive Summary Table:")
print(summary_df)
fig, ax = plt.subplots(figsize=(6,2))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=summary_df.values,
                 colLabels=summary_df.columns,
                 cellLoc='center',
                 loc='center')

plt.savefig("executive_summary.png", bbox_inches='tight')
plt.show()
