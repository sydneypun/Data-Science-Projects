import yfinance as yf
import streamlit as st
import pandas as pd

# Markdown for the application
st.write( """
	# Simple Stock Analysis Application

	Here we can see the stock closing price and volume for FANG (Facebook, Amazon, Netflix, Google) and Tesla!
	""")


# FACEBOOK STOCK
# ticker symbol is defined here
ticker_symbol = 'FB'
# get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)
# get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d', start='2010-9-20', end='2020-9-20')

st.write(""" ## Facebook Stock Closing Price """)
st.line_chart(ticker_df.Close)
st.write(""" ## Facebook Stock Volume """)
st.line_chart(ticker_df.Volume)


# AMAZON STOCK
# ticker symbol is defined here
ticker_symbol1 = 'AMZN'
# get data on this ticker
ticker_data1 = yf.Ticker(ticker_symbol1)
# get the historical prices for this ticker
ticker_df1 = ticker_data1.history(period='1d', start='2010-9-20', end='2020-9-20')

st.write(""" ## Amazon Stock Closing Price """)
st.line_chart(ticker_df1.Close)
st.write(""" ## Amazon Stock Volume """)
st.line_chart(ticker_df1.Volume)


# APPLE STOCK
# ticker symbol is defined here
ticker_symbol2 = 'AAPL'
# get data on this ticker
ticker_data2 = yf.Ticker(ticker_symbol2)
# get the historical prices for this ticker
ticker_df2 = ticker_data2.history(period='1d', start='2010-9-20', end='2020-9-20')

st.write(""" ## Apple Stock Closing Price """)
st.line_chart(ticker_df2.Close)
st.write(""" ## Apple Stock Volume """)
st.line_chart(ticker_df2.Volume)


# NETFLIX STOCK
# ticker symbol is defined here
ticker_symbol3 = 'NFLX'
# get data on this ticker
ticker_data3 = yf.Ticker(ticker_symbol3)
# get the historical prices for this ticker
ticker_df3 = ticker_data3.history(period='1d', start='2010-9-20', end='2020-9-20')

st.write(""" ## Netflix Stock Closing Price """)
st.line_chart(ticker_df3.Close)
st.write(""" ## Netflix Stock Volume """)
st.line_chart(ticker_df3.Volume)


# GOOGLE STOCK
# ticker symbol is defined here
ticker_symbol4 = 'GOOGL'
# get data on this ticker
ticker_data4 = yf.Ticker(ticker_symbol4)
# get the historical prices for this ticker
ticker_df4 = ticker_data4.history(period='1d', start='2010-9-20', end='2020-9-20')

st.write(""" ## Google Stock Closing Price """)
st.line_chart(ticker_df4.Close)
st.write(""" ## Google Stock Volume """)
st.line_chart(ticker_df4.Volume)
