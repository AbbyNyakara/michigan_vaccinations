import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import numpy as np

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
alt.data_transformers.enable('default', max_rows=6000)

st.header("Michigan State Covid Vaccinations Analysis")
st.markdown('''
    ### 1.0 Data
    
    - The project involves a comprehensive analysis of COVID-19 vaccination data specific to the state of Michigan. 
    - This dataset encompasses demographic information such as age, race, county of residence, 
       vaccination status (whether individuals are fully or partially vaccinated),
       and the total count of vaccinated individuals. 
    - All data utilized for this project is sourced from publicly available information 
      provided by [michigan.gov](https://www.michigan.gov/).
    -  Additionally, to enhance the analytical depth, this dataset has been integrated with the [Michigan census 
        data](https://www.census.gov/quickfacts/fact/table/MI/PST045222).    
            ''')

# Load the data
st.subheader('1. Michigan vaccination data overview: ')

df = pd.read_csv('michigan_vaccinations.csv')
st.write(df.head())

st.subheader('Michigan census data overview: ')
st.markdown('''
    - Total population: 10, 034, 113
    
    Breakdown by Race:
        
    - White/Caucasian: 78.8% 

    - Black/African-American: 14.1%

    - Asian/Native Hawaii/Pacific Island: 4%

    - Hispanic/Latino: 5.7%

    - Native Americans/Alaska Native: 0.7%

    *information on the breakdown by age was not sufficient for use in this analysis*
        ''')