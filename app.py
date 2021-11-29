from pandas.core.indexes.base import Index
import streamlit as st
import pandas as pd
import plotly.express as px

base="C:/Users/Adarsh/Desktop/all_projects/Fantasy-Premier-League/data"
st.text('FPL Visualization app BASIC.')

years=["2016-17","2017-18","2018-19","2019-20","2020-21","2021-22"]
game_weeks=[str(i) for i in range(1,39)]

option=st.selectbox("select your year",years)
gws=st.selectbox("select the gameweek:",game_weeks)

players_df=pd.read_csv(base+"/"+option+"/player_idlist.csv")

players_df["Name"]=players_df["first_name"]+"_"+players_df["second_name"]
players_df=players_df.drop(columns=["first_name","second_name"])
players=list(players_df["Name"])
player=st.selectbox("select your player",players)
id=int(players_df.loc[players_df["Name"]==player]["id"])
id=str(id)


gw="gw"+gws
link=base+"/"+option+"/gws/"+gw+".csv"
try:
    player_stats=pd.read_csv(base+"/"+option+"/players/"+player+"/gw.csv")
except:
    player_stats=pd.read_csv(base+"/"+option+"/players/"+player+"_"+id+"/gw.csv")
    



df=pd.read_csv(link,encoding='ISO-8859-1',engine='python')
fig = px.line(player_stats,y='total_points',title=f'points vs gameweek')
st.plotly_chart(fig)
st.dataframe(df)

