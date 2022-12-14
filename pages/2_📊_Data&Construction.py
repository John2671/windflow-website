import streamlit as st
import os
import numpy as np
import pandas as pd
import datetime
import requests
#from visions import Time
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.ibb.co/sHy0KCY/Foto-Jet-9.png);
                background-repeat: no-repeat;
                padding-top: 150px;
                background-position: 0px 15px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "WindFlow 1.0.2";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 15px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
#####
add_logo()

st.sidebar.markdown("# Data ๐")

st.markdown("""## Data: โ๐ผ
Real Data that we obtained is from a meteorological company in Chile, it is historical information of 05 years.
For each date and minute we have measurements of wind speed and direction as well as temperature and humidity. The data was delivered in an API, a dictionary with Json format that was converted into a Dataframe.""")

image = Image.open('appWindFlow/grafico.png')
st.image(image, caption='Historical data of the direction and force of the wind')

st.markdown("""## The model ๐ง๐ผโ๐ฌ
Two models were tested and metrics were evaluated to find the best model (Bidirectional LSTM, LSTM AR). The model that showed the best performance was the following, Bidirectional LSTM, which was the one used in the app.
## Application functionality ๐ฑ
It predicts the speed in (m/s) and the direction in (degreesยฐ) for the next 06 hours according to the station, date and time indicated
""")
