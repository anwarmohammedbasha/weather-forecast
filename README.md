# Mini Project 

# Title: Tamil Nadu Weather Forecast
Email questions and comments to anwarmohamedbasha@gmail.com

### Team Members

 * [Micklin Steffy (20-PDS-004)](https://www.linkedin.com/in/micklinsteffyl/)
 * [Anwar (20-PDS-023)](https://www.linkedin.com/in/anwarmohamedbasha/)
 * [Nandhini (20-PDS-026)](https://www.linkedin.com/in/nandhini-p-b18aab1b4/)

### Summary

A weather forecast is a prediction of how the weather will be the following day or the following several days. Based on input information such as city, date, and temperature, [this](https://share.streamlit.io/anwarmohammedbasha/weather-forecast/main/app.py) application can forecast the weather for cities in Tamil Nadu for the next seven days.  

We gathered the weather data for Tamil Nadu with the help of [**WeatherAPI.com**](https://www.weatherapi.com/), a free weather API provider, and [**WayScript**](https://wayscript.com/), a scripting platform. We have been gathering data since Arpil 2021. We directly import the data into **Github** to ensure that the data is updated. We pre-processed the data with the help of *pandas*, a Python package, to make it suitable for modelling. We use *ARIMA*, a statistical analysis model, to foresee potential trends. For modelling, we utilise the *statsmodels* package. Finally, we build web apps with [**Streamlit**](https://streamlit.io/), a Python framework.

### How to Use This Application

#### Step 1: Clicking on the link below, or simply pasting the url into the address bar, will take you to the application page.
##### https://share.streamlit.io/anwarmohammedbasha/weather-forecast/main/app.py

#### Step 2: There will be a drop down list of cities in Tamil Nadu on the application screen. Choose the city for which you want to forecast weather from the dropdown menu, for example, Chennai.
![Screenshot](/images/Screenshot1.png)

![Screenshot](/images/Screenshot2.png)

#### Step 3: After selecting the cities, the current weather will be displayed. To forecast the weather for the next seven days, click the forcast button.
![Screenshot](/images/Screenshot3.png)

## Frequently Asked Questions (FAQ)

### 1. Is the data updated on a regular basis, and if so, is it done manually or automatically?
Yes, the data is automatically and daily updated.

### 2. What is API?
API is an acronym for Application Programming Interface that software uses to access data.

### 3. What is the data's origin? 
The weather data for Tamil Nadu with the help of [**WeatherAPI.com**](https://www.weatherapi.com/), a free weather API provider, and [**WayScript**](https://wayscript.com/), a scripting platform. <br />
**Link**: https://wayscript.com/script/F-Y0r1eb

### 4. What is Time series analysis ?
Time series analysis is a specific way of analyzing a sequence of data points collected over an interval of time. 

### 5. What is Weather forecast ?
Weather forecasting is the application of science and technology to predict the conditions of the atmosphere for a given location and time.

### 6. Why is ARIMA used?
Autoregressive integrated moving average (ARIMA) models predict future values based on past values. ARIMA makes use of lagged moving averages to smooth time series data. They are widely used in technical analysis to forecast future security prices.
