import pandas as pd
from  statsmodels.tsa.arima.model import ARIMA
from datetime import date, timedelta
import streamlit as st 

st.write("""
# Tamil Nadu Weather Forecast 
Team Project""")

city =  st.selectbox('City', ('Ariyalur',  'Chennai',  'Coimbatore',  'Cuddalore',  'Dharmapuri',  'Dindigul',  'Erode',  'Kancheepuram',  'Kanyakumari',  'Karur',  'Krishnagiri',  'Madurai',  'Nagapattinam',  'Namakkal',  'Perambalur',  'Pudukkottai',  'Ramanathapuram',  'Salem',  'Sivaganga',  'Thanjavur',  'Thiruvarur',  'Tiruchirappalli',   'Tirunelveli',  'Tirupur',  'Tiruvallur',  'Tiruvannamalai',  'Vellore',  'Villupuram'))
df = pd.read_csv('weather_data.csv', usecols=['name', 'localtime', 'temp_c'], parse_dates=True)
df = df.loc[df['name'] == city, ['localtime', 'temp_c']]
df.set_index(['localtime'], inplace=True)
df.dropna(inplace=True)
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit()

if st.button('Forecast'):
    st.write("Today", 'Date: ', date.today() , 'Weather: ', int(model_fit.forecast(steps=3)[1:2]), '°C')
    st.write("Tomorrow", 'Date: ', date.today() + timedelta(1)  , 'Weather: ', int(model_fit.forecast(steps=3)[2:]), '°C')
else: pass
