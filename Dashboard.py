# This is a stock market dashboard to show some charts and data on the FAANG stocks and the Tesla stock.

# DEPENDENCIES 
import streamlit as st
import pandas as pd 
from PIL import Image

# Add a title and an image
st.write(""" 
# Stock Market Dashboard
This is a visual representation of the FAANG companies' stocks and Tesla's stock. The date range is from 
January 1, 2010 - October 1, 2020. Date is subject to change. 
""")

image = Image.open("Images\stonks.jpg")
st.image(image, use_column_width=True)

# Create a sidebar header
st.sidebar.header('User Input')

# Create a function to get the user's input
def get_input(): 
    start_date = st.sidebar.text_input("Start Date", "2010-01-01")
    end_date = st.sidebar.text_input("End Date", "2020-10-01")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

# Create a function to get the company name
def get_company_name(): 
    if symbol=='AMZN':
        return 'Amazon'
    elif symbol=='AAPL':
        return 'Apple'
    elif symbol=='NFLX':
        return 'Netflix'
    elif symbol=='GOOG':
        return 'Alphabet'
    elif symbol=='FB':
        return 'Facebook'
    elif symbol=='TSLA': 
        return 'Tesla'
    else: 
        'None'

# Create a function to get the proper company data and time frame inputted by the user
def get_data(symbol, start, end): 
    # Load the data
    if symbol.upper() == 'AMZN': 
        df = pd.read_csv("Datasets/Amazon.csv")
    elif symbol.upper() == 'AAPL': 
        df = pd.read_csv("Datasetes/Apple.csv")
    elif symbol.upper() == 'FB': 
        df = pd.read_csv("Datasets/Facebook.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("Datasets/Google.csv")
    elif symbol.upper() == 'NFLX': 
        df = pd.read_csv("Datasets/Netflix.csv")
    else: 
        df = pd.DataFrame(columns = ['Date', 'Close','Open', 'Volume', 'Adj Close', 'High', 'Low'])

    # Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    # Start the date from the top of the data set and go down to see if there's a start date
    for i in range(0, len(df)): 
        if start <= pd.datetime(df['Date'][i]): 
            start_row = i 
            break 

    # Start the date from the bottom of the data set and go up
    for j in range(0, len(df)): 
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 - j
            break 
    
    # Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]

# Get the user's input
start, end, symbol = get_input()
# Get the data
df = get_data(symbol, start, end)
# Get the company name
company_name = get_company_name(symbol.upper())

# Display the close price
st.header(company_name + "Close Price\n")
st.line_chart(df['Close'])

# Display the volume
st.header(company_name + "Volume\n")
st.line_chart(df['Volume'])

# Get statistics on the data
st.header('Data Statistics')
st.write(df.describe())