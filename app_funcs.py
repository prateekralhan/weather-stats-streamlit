import requests
import json
import streamlit as st

openweather_api_key = st.secrets["OPENWEATHER_API_Key"]
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Bangalore"
complete_url = base_url + "appid=" + openweather_api_key + "&q=" + city_name + "&units=metric"
response = requests.get(complete_url)
x = response.json()


y = x["main"]
print(y)
current_temp = y["temp"]
max_temp = round((y["temp_max"]))
min_temp = round(y["temp_min"])
humidity = y["humidity"]
pressure = y["pressure"]
feels = y["feels_like"]
visibility = x["visibility"]
previous_temp = 23

def temp_difference():
    global previous_temp
    #Getting percentage of difference between old and new temp
    change_percent = ((float(current_temp) - max_temp) / max_temp) * 100
    change_percent = int(change_percent)
    print(change_percent)

    if previous_temp > current_temp:
        return str(change_percent)

    if previous_temp < current_temp:
        return "+" + str(change_percent)

    if change_percent == 0:
        return "0"

def get_temp():
    return(str(current_temp)+" °C")

def get_temp_min():
    return(str(min_temp)+" °C")

def get_temp_max():
    return(str(max_temp)+" °C")

def get_humidity():
    return(str(humidity))

def get_pressure():
    return(str(pressure))

def get_feel():
    return(str(feels)+"°C")

def get_visibility():
    return(str(visibility/1000)+" km")

def get_aqi():
    aqi_api_key = st.secrets["AQI_API_Key"]
    aqi_base_url = "https://api.waqi.info/feed/here/?token="
    response = requests.get(aqi_base_url + aqi_api_key)
    aqi_json_output = response.json()

    city_aqi_current = aqi_json_output["data"]["aqi"]
    return(str(city_aqi_current))
