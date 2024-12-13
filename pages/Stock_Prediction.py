import streamlit as st
from pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, scaling, evaluate_model, get_forecast, inverse_scaling
import pandas as pd
from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

# Set page configuration
st.set_page_config(
    page_title="Stock Prediction",
    page_icon="chart_with_downwards_trend",
    layout="wide",
)

st.title("Stock Prediction")

# Dropdown for stock ticker selection
ticker_list = ['TSLA', 'AAPL','NFLX','MGM','MSFT','AMZN','NVDA','GOOGL','TGLS', 'AMAT', 'HRB', 'POWL', 'DDOG', 'HOOD', 'PLTR', 'WBA', 'UBER', 'RDDT' 'META','LULU', 'GTLS', 'FLNC', 'NOW', 'ZS', 'SHOP', 'HRB','RELY', 'ACVA', 'NVMI', 'MPWR', 'ABNB', 'DUOL', 'MELI', 'COST', 'YUM', 'CMG', 'WING', 'MNST', 'CL', 'VITL', 'TTD', 'MNDY', 'GTLB', 'TH', 'DECK', 'NSSC', 'FIX', 'BYRN', 'AVGO', 'QCOM', 'STX', 'WDC', 'MU', 'PI', 'OLED', 'KLAC', 'SGH', 'INTC', 'QRVO', 'LSCC', 'ALGM', 'AMD', 'FLNC', 'APLD', 'APP', 'BHC', 'BLCO', 'SOUN', 'AI', 'SMCI', 'SOUN', 'BLCO', 'PDCO', 'CRK', 'ORCL', 'MRVL', 'KO', 'SNAP', 'AAL', 'BAC', 'SOFI', 'GOOG', 'INTC', 'ASAN', 'EQT', 'ASO', 'HWKN', 'VST', 'DJTWW', 'SQ', 'ESTC', 'ICUI', 'KKR', 'MDB', 'RGLD', 'FWONA', 'SOFI', 'MTZ', 'OSW', 'PONY', 'CABO', 'HALO']  # Add more stock tickers as needed
ticker = st.selectbox('Select Stock Ticker', ticker_list, index=0)

rmse = 0

st.subheader('Predicting Next 30 days Close Price for: ' + ticker)

# Fetch and process the stock data
close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)

# Differencing order, scaling, and model evaluation
differencing_order = get_differencing_order(rolling_price)
scaled_data, scaler = scaling(rolling_price)
rmse = evaluate_model(scaled_data, differencing_order)

# Display the RMSE score
st.write("**Model RMSE Score:**", rmse)

# Generate and display forecast for the next 30 days
forecast = get_forecast(scaled_data, differencing_order)
forecast['Close'] = inverse_scaling(scaler, forecast['Close'])

# Show forecast data in a table
st.write('##### Forecast Data (Next 30 days)')
fig_tail = plotly_table(forecast.sort_index(ascending=True).round(3))
fig_tail.update_layout(height=220)
st.plotly_chart(fig_tail, use_container_width=True)

# Concatenate rolling price and forecast data for visualization
forecast = pd.concat([rolling_price, forecast])

# Show the moving average forecast plot
st.plotly_chart(Moving_average_forecast(forecast.iloc[150:]), use_container_width=True)
