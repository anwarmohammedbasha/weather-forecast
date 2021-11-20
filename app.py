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
st.write('Todays Weather in ', city ,int(model_fit.forecast(steps=9)[1:2]), '°C')

if st.button('Forecast'):
    for i in range(1, 7):
        st.write('Date: ', date.today() + timedelta(i)  , 'Weather: ', int(model_fit.forecast(steps=9)[i+1:i+2]), '°C')
else: pass
