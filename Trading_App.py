import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Trading App",
    page_icon=":heavy_dollar_sign:",
    layout="wide",
)

# Title with custom color styling using markdown
st.markdown("<h1 style='color:#ff6347;'>Trading Guide App :</h1>", unsafe_allow_html=True)

# Subtitle with more color and emphasis
st.markdown("<h3 style='color:#333333;'>We provide the Greatest platform for you to collect all information prior to investing in stocks.</h3>", unsafe_allow_html=True)

# Displayi ng an image (if available in the directory)
st.image("images.png", use_container_width=True)  # Updated to use_container_width

# Adding a heading with color
st.markdown("<h3 style='color:#ff6347;'>We provide the following services:</h3>", unsafe_allow_html=True)

# Service 1: Stock Information
st.markdown("#### :one: **Stock Information**")
st.write("Through this page, you can see all the information about stock. Stay updated with real-time stock data, including price trends, historical data, and stock performance.")

# Service 2: Stock Prediction
st.markdown("#### :two: **Stock Prediction**")
st.write("Explore predicted closing prices for the next 30 days based on advanced forecasting models such as ARIMA. This feature helps you analyze potential market trends and make informed investment decisions.")

# Service 3: CAPM Return
st.markdown("#### :three: **CAPM Return**")
st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stocks based on its risk and market performance. Understand how risk factors influence investment returns.")

# Service 4: CAPM Beta
st.markdown("#### :four: **CAPM Beta**")
st.write("Calculates Beta and Expected Return for Individual Stocks. Understand how a stock reacts to market movements and assess its risk in comparison to the market.")

# Adding more content (New sections for additional services)

# Additional Services Section
st.markdown("<h3 style='color:#ff6347;'>Additional Resources:</h3>", unsafe_allow_html=True)

# Service 5: Trading Strategies
st.markdown("#### :five: **Trading Strategies**")
st.write("Access expert trading strategies to improve your investment approach. Learn about risk management, portfolio diversification, and tactical decision-making to maximize your returns.")



# Footer with updated background and text
st.markdown("""
    <div style="background-color:orange; padding: 20px; text-align:center; border-radius: 10px;">
    <h2 style="color:white;">Built with ❤️ using Streamlit, Python, and Plotly</h2>
    </div>
    """, unsafe_allow_html=True)

