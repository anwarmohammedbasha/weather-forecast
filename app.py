import pandas as pd
from  statsmodels.tsa.arima.model import ARIMA
from datetime import date
import streamlit as st 


st.write("""
# Tamil Nadu Weather Forecast 
Team Project
""")

city =  st.selectbox('City',
        ('Ariyalur',  'Chennai',  'Coimbatore',  'Cuddalore',  'Dharmapuri',  'Dindigul',  'Erode',  'Kancheepuram',  'Kanyakumari',  'Karur',  'Krishnagiri',  'Madurai',  'Nagapattinam',  'Namakkal',  'Perambalur',  'Pudukkottai',  'Ramanathapuram',  'Salem',  'Sivaganga',  'Thanjavur',  'Thiruvarur',  'Tiruchirappalli',   'Tirunelveli',  'Tirupur',  'Tiruvallur',  'Tiruvannamalai',  'Vellore',  'Villupuram'))

st.write('You selected:', city)

cols = ['name', 'localtime', 'temp_c']
df = pd.read_csv('weather_data.csv', usecols=cols, parse_dates=True)
df = df.loc[df['name'] == city, ['localtime', 'temp_c']]
df.set_index(['localtime'], inplace=True)
df.dropna(inplace=True)
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit()
forecast = int(model_fit.forecast(steps=2)[1:])




if st.button('Predict'):
    today = date.today()
    st.write('Date: ', today , 'Weather: ', forecast, '°C')
else: pass
