# importing essential libraries

def setupSpark():
  #apt-get install openjdk-8-jdk-headless > /dev/null
  #echo 2 | update-alternatives --config java > /dev/null
  import os
  os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-8-openjdk-amd64'
  echo JAVA_HOME=$JAVA_HOME
  #findspark.init(spark_home='/usr/local/lib/python3.7/dist-packages/pyspark')
  
setupSpark()

from pyspark.sql import SparkSession
import pandas as pd
from  statsmodels.tsa.arima.model import ARIMA
from datetime import date, timedelta
import streamlit as st 

spark = SparkSession.builder.appName('forecast').getOrCreate()

st.write("""# Tamil Nadu Weather Forecast""")
city =  st.selectbox('City', ('Ariyalur', 'Chennai', 'Coimbatore', 'Cuddalore',
                              'Dharmapuri', 'Dindigul', 'Erode', 'Kancheepuram',
                              'Kanyakumari', 'Karur', 'Krishnagiri', 'Madurai',
                              'Nagapattinam', 'Namakkal', 'Perambalur', 
                              'Pudukkottai', 'Ramanathapuram', 'Salem', 
                              'Sivaganga', 'Thanjavur', 'Thiruvarur', 
                              'Tiruchirappalli', 'Tirunelveli', 'Tirupur',
                              'Tiruvallur', 'Tiruvannamalai', 'Vellore',
                              'Villupuram'))

# data preprocessing

df = spark.read.csv("weatherData.csv", header=True)
df = df[df.city == "Chennai"]['date', 'temp_c']
df = pd.DataFrame(df.toPandas()).set_index(['date'])
df = df['temp_c'].apply(lambda x: int(float(x)))

#df = pd.read_csv('weatherData.csv', parse_dates=True)
#df = df.loc[df['city'] == city, ['date', 'temp_c']]
#df.set_index(['date'], inplace=True)
#df.dropna(inplace=True)

# model development

model = ARIMA(df, order=(5,1,0)).fit()

# forecasting

#st.write('Todays Weather in ', city ,int(model.forecast(steps=9)[1:2]), '°C')

if st.button('Forecast'): 
  for i in range(2, 9):
    st.write('Date: ', date.today() + timedelta(i),
             'Weather: ', int(model.forecast(steps=10)[i+1:i+2]), '°C')
else: pass
