import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import time

from datetime import datetime
from datetime import timedelta

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

#function to make chart
def make_chart(data,ticker,i):
    fig = px.line(data, x=data.index, y= data['Adj Close'])
    fig.update_layout(
        title = ticker + str(i),
        uirevision = True,
        xaxis = dict(autorange = True),
        yaxis = dict(autorange = True))
    st.write(fig)

def get_data(ticker, start_date, end_date, end_date_str):
    end_date_aux = datetime.strptime(end_date_str, "%Y-%m-%d")
    end_date_ = end_date_aux + timedelta(days=1)
    end_date = end_date_.strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start_date, end=end_date)
    return data, end_date


plot_spot = st.empty()
end_date_str = str(end_date)
for i in range(60):
    data,end_date_str = get_data(ticker, start_date, end_date, end_date_str)
    with plot_spot:
        make_chart(data, ticker, i)
    time.sleep(1)
