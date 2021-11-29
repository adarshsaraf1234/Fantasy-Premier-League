

import streamlit as st
import pandas as pd

st.text('FPL Visualization app BASIC.')
years=["2016-17","2017-18","2018-19","2019-20","2020-21","2021-22"]
option=st.multiselect("select your year",years)
print(option)
st.write("you selected",option)