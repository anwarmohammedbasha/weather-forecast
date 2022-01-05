import pandas as pd
from pyspark.sql import SparkSession
from  statsmodels.tsa.arima.model import ARIMA
from datetime import date, timedelta
import streamlit as st 

spark = SparkSession.builder.appName('forecast').getOrCreate()

st.write("""# Tamil Nadu Weather Forecast""")
city =  st.selectbox('City', ('Ariyalur', 'Chennai', 'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode', 'Kancheepuram', 'Kanyakumari', 'Karur',
                              'Krishnagiri', 'Madurai', 'Nagapattinam', 'Namakkal', 'Perambalur', 'Pudukkottai', 'Ramanathapuram', 'Salem', 'Sivaganga',
                              'Thanjavur', 'Thiruvarur', 'Tiruchirappalli', 'Tirunelveli', 'Tirupur', 'Tiruvallur', 'Tiruvannamalai', 'Vellore', 'Villupuram'))

df = spark.read.csv("weatherData.csv", header=True)
df = df[df.city == city]['date', 'temp_c']
df = pd.DataFrame(df.toPandas()).set_index(['date'])
df = df['temp_c'].apply(lambda x: int(float(x)))

model = ARIMA(df, order=(5,1,0)).fit()

st.write('Todays Weather in ', city ,int(model.forecast(steps=9)[1:2]), '°C')
if st.button('Forecast'): 
  for i in range(1, 7):
    st.write('Date: ', date.today() + timedelta(i), 'Weather: ', int(model.forecast(steps=10)[i+1:i+2]), '°C')
else: pass
