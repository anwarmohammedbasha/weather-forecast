import pandas as pd
from  statsmodels.tsa.arima.model import ARIMA
import streamlit as st 


st.write("""
# weather forcast
still in progress
""")

cols = ['name', 'localtime', 'temp_c']
df = pd.read_csv('weather_data.csv', usecols=cols, parse_dates=True)
df = df.loc[df['name'] == "Chennai", ['localtime', 'temp_c']]
df.set_index(['localtime'], inplace=True)
df.dropna(inplace=True)
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=2)

city =  st.selectbox('City',
        ('Chennai', 'x'))
st.write('You selected:', city)

if st.button('Predict'):
    st.write('date: ', pd.to_datetime("today"), 'weather:', forecast)
else: pass
