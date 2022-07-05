import yfinance as yf
import pandas as pd
import streamlit as st 
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


st.write("""
# Aplikasi Yahoo Finance
## Data Saham XL AXIATA

Berikut ini adalah data closing price dan volume dari XL AXIATA. 
""")

ticker = st.selectbox(
    "Ticker Perusahaan",
    options = [ "EXCL.JK", "BMRI.JK"]
) 
tickerData = yf.Ticker(ticker)

jumlah_hari = timedelta(days=-30)


tgl_mulai = st.date_input(
    "Mulai dari tanggal"
    value=data.today()+jumlah_hari
)

tgl_akhir = st.date_input(
    "Hingga"
    value=date.today()
)


# hard coded
tickerDF = tickerData.history(
    period='1d',
    start=str(tgl_mulai)',
    end=str(tgl_akhir)
)

elif ticker =='EXCL.JK' :
    nama_perusahaan = "XL AXIATA"
    
elif ticker =='BMRI.JK' :
    nama_perusahaan == "BANK MANDIRI"

# F-string
st.markdown(f"Harga penutupan **{nama_perusahaan}**")
St.plotly_chart(
    px.line(ticker.DF.Close)
)
st.line_chart(tickerDF.Close)

st.markdown(f"Volume Transaksi Saham **{nama_perusahaan}**")
St.plotly_chart(
    px.line(ticker.DF.Volume)
)
st.line_chart(tickerDF.Volume)



