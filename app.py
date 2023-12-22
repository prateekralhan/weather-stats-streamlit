import streamlit as st
import pandas as pd
import numpy as np
import pytz
from datetime import datetime
from datetime import date
from PIL import Image
from app_funcs import *
from streamlit_autorefresh import st_autorefresh

st.set_page_config(layout="wide", page_title="Realtime Weather ☁")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

count = st_autorefresh(interval=5000, limit=100, key="fizzbuzzcounter")

IST = pytz.timezone('Asia/Kolkata')
nowTime = datetime.now(IST)
current_time = nowTime.strftime("%H:%M:%S")
timeMetric, = st.columns(1)
timeMetric.metric("",nowTime.strftime("%B %e, %Y"))

a1, a2, a3, a4 = st.columns(4)
a1.metric("Bangalore's Temperature 🌳", f"{get_temp()}", f"{temp_difference()}"+"%")
a2.metric("Bangalore's time 🕗", current_time)
a3.metric("Humidity 💧", f"{get_humidity()}"+"%")
a4.metric("AQI 🍃", f"{get_aqi()}")

b1, b2, b3, b4 = st.columns(4)
b1.metric("Feels like ❕❗", f"{get_feel()}")
b2.metric("Highest temperature 🥵", f"{get_temp_max()}")
b3.metric("Lowest temperature 🥶", f"{get_temp_min()}")
b4.metric("Visibility 😵", f"{get_visibility()}")

c1, c2 = st.columns((7,3))

with c1:

    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['Low', 'High', 'Close'])
    st.line_chart(chart_data)

with c2:
    df = pd.DataFrame(
        np.random.randn(7, 5),
        columns=('Bangalore','Delhi','Noida','Chennai','Jammu')
    )

    st.table(df)

st.button("Run me manually")
