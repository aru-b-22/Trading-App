import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Trading Strategies & Stock Market News",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

# Title of the page
st.title("Trading Strategies :chart_with_upwards_trend:")

st.markdown("""
### 1. **Day Trading** :money_with_wings:  
Day trading involves buying and selling stocks within a single trading day. Traders aim to profit from short-term price fluctuations.  
**Pros**: High-frequency opportunities, quick profits.  
**Cons**: High risk, requires active involvement.  
**Best For**: Those with a lot of time to monitor markets.

### 2. **Swing Trading** :⛷️ 
Swing trading involves holding stocks for a few days to weeks to capitalize on expected upward or downward market shifts.  
**Pros**: Less time-intensive than day trading, opportunity for bigger moves.  
**Cons**: Market fluctuations, possible overnight risks.  
**Best For**: Traders with a bit more patience but still seek short-term profits.

### 3. **Scalping** :dart:  
Scalping is a strategy that involves making multiple trades over a day, each aiming to gain small profits. It's fast-paced and requires focus.  
**Pros**: Can lead to consistent profits, requires less risk exposure.  
**Cons**: Intense and demanding.  
**Best For**: Highly focused traders with fast reflexes.

### 4. **Position Trading** :rocket:  
Position traders hold stocks for months or years, aiming to benefit from long-term trends. This strategy requires patience and research.  
**Pros**: Potential for high returns, less time commitment.  
**Cons**: Requires patience, can experience long periods of drawdown.  
**Best For**: Long-term investors with the ability to withstand volatility.

### 5. **Momentum Trading** :fire:  
Momentum trading involves buying stocks that are trending upward and selling those that are trending downward.  
**Pros**: Captures large trends, often profitable.  
**Cons**: Hard to predict entry and exit points, can be volatile.  
**Best For**: Traders who are skilled at identifying trends and have quick execution.

### 6. **Contrarian Strategy** :thinking_face:  
Contrarian investors go against prevailing market trends by buying stocks that are underperforming or shorting those that are overvalued.  
**Pros**: Potential for high returns if timed correctly.  
**Cons**: Risk of betting against the market, requires deep analysis.  
**Best For**: Experienced investors who are comfortable taking risks.

### 7. **Value Investing** :moneybag:  
Value investing focuses on purchasing undervalued stocks with strong potential for growth.  
**Pros**: Historically successful, lower risk in the long term.  
**Cons**: Requires patience, sometimes undervalued stocks take time to recover.  
**Best For**: Long-term investors who have the ability to hold positions for extended periods.

### 8. **Algorithmic Trading** :🤖  
Algorithmic trading involves using computer algorithms to execute trading strategies automatically.  
**Pros**: Faster execution, no emotional bias.  
**Cons**: High technical skill required, costly infrastructure.  
**Best For**: Those who want to automate trading based on certain rules or patterns.

### 9. **Trend Following** :chart_with_upwards_trend:  
Trend following involves buying assets that are trending upwards and selling those trending downwards.  
**Pros**: Captures significant price movements.  
**Cons**: Can be risky if the trend reverses suddenly.  
**Best For**: Traders who prefer riding longer market movements.

### 10. **Pairs Trading** :two_women_holding_hands:  
Pairs trading involves identifying two correlated assets and taking long and short positions to capitalize on relative price movements.  
**Pros**: Market-neutral, reduces exposure to overall market movements.  
**Cons**: Complex analysis required, potential for small gains.  
**Best For**: Experienced traders looking for more sophisticated strategies.
""")

# Footer
st.markdown("""
    <div style="background-color:#4CAF50; padding: 20px; text-align:center; border-radius: 10px;">
    <h2 style="color:white;">Built with ❤️ using Streamlit, Python, and Plotly</h2>
    </div>
    """, unsafe_allow_html=True)
