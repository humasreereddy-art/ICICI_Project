import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
df = pd.read_excel("ICICI_Financials.xlsx")
summary_df = pd.read_csv("executive_summary.csv")

# Dashboard title
st.title("ICICI Financial Analysis Dashboard")


# KPI banner
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Net Profit (₹ Cr)", value="5200", delta="+8.5%")
with col2:
    st.metric(label="ROA (%)", value="1.6%", delta="+0.2%")
with col3:
    st.metric(label="CAR (%)", value="16.5%", delta="-0.3%")


# --- Overview ---
st.markdown("""
### 📊 Overview
This dashboard presents ICICI's financial performance across profitability, lending, risk, capital efficiency, and forecasting.
Use the tabs to explore interactive charts, scenario analysis, and executive summary metrics.
""")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Profitability", 
    "Digital Lending", 
    "Risk Management", 
    "Capital Efficiency", 
    "Forecasting", 
    "Scenario Forecasting", 
    "Risk Heatmap", 
    "Executive Summary",
    "Key Insights"
])

# --- Profitability ---
with tab1:
    st.header("ROA vs ROE")
    year_filter = st.slider("Select Year Range", int(df["Year"].min()), int(df["Year"].max()), (2015, 2025))
    filtered = df[(df["Year"] >= year_filter[0]) & (df["Year"] <= year_filter[1])]
    fig, ax = plt.subplots()
    ax.plot(filtered["Year"], filtered["ROA"], marker="o", label="ROA")
    ax.plot(filtered["Year"], filtered["ROE"], marker="o", label="ROE")
    ax.set_xlabel("Year")
    ax.set_ylabel("Ratio")
    ax.legend()
    st.pyplot(fig)

# --- Digital Lending ---
with tab2:
    st.header("Loan Growth vs Net NPA")
    fig, ax = plt.subplots()
    ax.scatter(df["Loan Growth %"], df["Net NPA %"], color="orange")
    ax.set_xlabel("Loan Growth %")
    ax.set_ylabel("Net NPA %")
    st.pyplot(fig)

# --- Risk Management ---
with tab3:
    st.header("Stress Test & Monte Carlo")
    st.image("risk_stress_test.png")
    st.image("monte_carlo_net_profit.png")

# --- Capital Efficiency ---
with tab4:
    st.header("CAR% Trend")
    st.image("car_trend.png")

# --- Forecasting ---
with tab5:
    st.header("Forecasts")
    st.image("forecast_net_profit.png")
    st.image("forecast_car.png")

# --- Scenario Forecasting ---
with tab6:
    st.header("Scenario Selector")
    scenario = st.selectbox("Choose Scenario", ["Base", "Optimistic", "Pessimistic"])
    if scenario == "Base":
        st.image("scenario_forecast_net_profit.png")
        st.image("scenario_forecast_car.png")
    elif scenario == "Optimistic":
        st.image("scenario_forecast_net_profit.png")  # Replace with optimistic chart
    else:
        st.image("scenario_forecast_net_profit.png")  # Replace with pessimistic chart

# --- Risk Heatmap ---
with tab7:
    st.header("Risk Heatmap")
    st.image("risk_heatmap.png")

# --- Executive Summary ---
with tab8:
    st.header("Executive Summary Metrics")
    # Show KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg ROA", f"{summary_df.loc[0,'Value']}")
    col2.metric("Avg ROE", f"{summary_df.loc[1,'Value']}")
    col3.metric("Worst-case Profit", f"{summary_df.loc[2,'Value']}")
    col4.metric("Forecasted CAR% 2030", f"{summary_df.loc[3,'Value']}")
    # Show full table
    st.table(summary_df)

# --- Key Insights ---
with tab9:
    st.header("Key Insights")
    st.markdown("""
    - 📈 **Profitability**: ROA and ROE show consistent upward trends.
    - ⚠️ **Risk**: Net Profit is sensitive to NPA increases; heatmap highlights risk zones.
    - 💰 **Capital Efficiency**: CAR% remains stable in base case but dips under stress.
    - 🔮 **Forecasts**: Net Profit expected to grow steadily; CAR% forecast ~16.5% by 2030.
    """)

import streamlit as st
import pandas as pd

st.header("📥 Export Data")

# Combine all your datasets into one dictionary
loan_book_data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "Loan Book (₹ Cr)": [350000, 370000, 390000, 410000, 430000, 460000, 500000, 540000, 580000, 620000, 660000],
    "YoY Growth (%)": [5.7, 5.4, 5.3, 5.1, 4.9, 7.0, 8.7, 8.0, 7.4, 6.9, 6.5]
}
df_loan = pd.DataFrame(loan_book_data)

# You can add other DataFrames here (NPA, ROA, CAR, etc.)
# For now, just one example

# Convert to CSV
csv = df_loan.to_csv(index=False).encode('utf-8')

# Central download button
st.download_button(
    label="Download All Data (CSV)",
    data=csv,
    file_name="icici_dashboard_data.csv",
    mime="text/csv"
)
