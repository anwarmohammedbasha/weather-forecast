## Mini Project 

## Title: Tamil Nadu Weather Forecast

## Team Members

 * [Micklin Steffy (20-PDS-004)](https://www.linkedin.com/in/micklinsteffyl/)
 * [Anwar (20-PDS-023)](https://www.linkedin.com/in/anwarmohamedbasha/)
 * [Nandhini (20-PDS-026)](https://www.linkedin.com/in/nandhini-p-b18aab1b4/)

## Summary

A weather forecast is a prediction of how the weather will be the following day or the following several days. Based on input information such as city, date, and temperature, [this](https://share.streamlit.io/anwarmohammedbasha/weather-forecast/main/app.py) application can forecast the weather for cities in Tamil Nadu for the next seven days.  

We gathered the weather data for Tamil Nadu from [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/). We have data from January 2010 until the present. We directly import the data into **Github** to ensure that the data is updated. We pre-processed the data with the help of *pandas*, a Python package, to make it suitable for modelling. We use *ARIMA*, a statistical analysis model, to foresee potential trends. For modelling, we utilise the *statsmodels* package. Finally, we build web apps with [**Streamlit**](https://streamlit.io/), a Python framework.

## Pyspark Code

### Importing Essential Libraries & Creating Spark Session

```
import pandas as pd
from pyspark.sql import SparkSession
from  statsmodels.tsa.arima_model import ARIMA
spark = SparkSession.builder.appName('forecast').getOrCreate()
```

### Data Preprocessing & Model Development
```
df = spark.read.csv("weatherData.csv", header=True)
df = df[df.city == "Dindigul"]['date', 'temp_c']
df = pd.DataFrame(df.toPandas()).set_index(['date'])
df = df['temp_c'].apply(lambda x: int(float(x)))

model = ARIMA(df, order=(5,1,0)).fit()
```

## How to Use This Application

### Step 1: Clicking on the link below, or simply pasting the url into the address bar, will take you to the application page.
##### https://share.streamlit.io/anwarmohammedbasha/weather-forecast/main/app.py

### Step 2: There will be a drop down list of cities in Tamil Nadu on the application screen. Choose the city for which you want to forecast weather from the dropdown menu, for example, Chennai.
![Screenshot](/images/Screenshot1.png)

![Screenshot](/images/Screenshot2.png)

### Step 3: After selecting the cities, the current weather will be displayed. To forecast the weather for the next seven days, click the forcast button.
![Screenshot](/images/Screenshot3.png)

Email questions and comments to anwarmohamedbasha@gmail.com
