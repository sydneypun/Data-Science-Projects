# This is a stock market dashboard to show some charts and data on the FAANG stocks and the Tesla stock.

# DEPENDENCIES 
import streamlit as st
import pandas as pd 
from PIL import Image

# Add a title and an image
st.write(""" 
# Stock Market Dashboard
This is a visual representation of the FAANG companies' stocks and Tesla's stock. The date range is from 
October 1, 2010 - October 1, 2020. Date is subject to change. 
""")

image = Image.open("Images\stonks.jpg")
st.image(image, use_column_width=True)

# Create a sidebar header
st.sidebar.header('User Input')

# Create a function to get the user's input
def get_input(): 
    start_date = st.sidebar.text_input("Start Date", "2010-01-01")
    end_date = st.sidebar.text_input("End Date", "2020-01-01")
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
#def get_data(symbol, start, end): 
    # Load the data

