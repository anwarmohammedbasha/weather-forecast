import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import streamlit as st 


st.write("""
# weather forcast
still in progress
""")

def user_input_var():
    city =  st.selectbox('City',
             ('Chennai', 'x'))
    st.write('You selected:', city)
    cols = ['name', 'localtime', 'temp_c']
    df = pd.read_csv('weather_data.csv', usecols=cols, parse_dates=True)
    city_list = list(df.name.unique())
    df = df.loc[df['name'] == city, ['localtime', 'temp_c']]
    df.set_index(['localtime'], inplace=True)
    df.dropna(inplace=True)
    model = ARIMA(df, order=(5,1,0))
    model_fit = model.fit()
    forecast = round(model_fit.forecast(steps=1)[0][0],0)
    return st.write('date: ', pd.to_datetime("today"), 'weather:', forecast)


