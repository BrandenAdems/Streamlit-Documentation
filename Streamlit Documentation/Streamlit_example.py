import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image

header = st.container()
dataset = st.container()

st.sidebar.title("Date Selector")
selectbox = st.sidebar.selectbox(
    "Please Select a Specific Month",
    ["January", "February", "March", "April", "May", "June", "July", "August"]
)

with header:
    st.title("Welcome To Malaysia Covid-19 Cases in 2021")
    st.markdown("In this Website, you get to look back on the past record of covid-19 in Malaysia in the year of 2021")
    st.image(Image.open('Covid-19_Malaysia.JPG'))

with dataset:
    st.header("Malaysia Covid-19 Cases Throughout 2021")
    st.markdown('''
- This data is obtained from [Statista](https://www.statista.com/statistics/1110785/malaysia-covid-19-daily-cases/)
- This App is built by Branden Adems
''')
    covid_data = pd.read_csv('data/NewCovid_2021.csv')
    st.write(covid_data.head(31))

if selectbox == "January":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-1'][:50], y=covid_data['Jan-21'][:50])
    ])
    st.plotly_chart(fig)

if selectbox == "February":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-2'][:50], y=covid_data['Feb-21'][:50])
    ])
    st.plotly_chart(fig)

if selectbox == "March":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-3'][:50], y=covid_data['Mar-21'][:50])
    ])
    st.plotly_chart(fig)

if selectbox == "April":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-4'][:50], y=covid_data['Apr-21'][:50])
    ])
    st.plotly_chart(fig)

if selectbox == "May":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-5'][:50], y=covid_data['May-21'][:50])
    ])
    st.plotly_chart(fig)

if selectbox == "June":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-6'][:50], y=covid_data['Jun-21'][:50])
    ])
    st.plotly_chart(fig)

if selectbox == "July":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-7'][:50], y=covid_data['Jul-21'][:50])
    ])
    st.plotly_chart(fig)

if selectbox == "August":
    st.title(f"Covid-19 Cases in {selectbox}")
    fig = go.Figure(data=[
        go.Bar(name='Total Cases', x=covid_data['Date-8'][:50], y=covid_data['Aug-21'][:50])
    ])
    st.plotly_chart(fig)

    