import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import numpy as np
# fig, ax = plt.subplots()

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
alt.data_transformers.enable('default', max_rows=6000)

df = pd.read_csv('michigan_vaccinations.csv')

st.subheader('Chart 4 - Dosage coverage by Race/Ethnicity')

df_dosage = df.groupby(['Race/Ethnicity', 'Dose']
                       )['Residents Vaccinated'].sum().reset_index()

# Select the options
chart_type2  = st.selectbox(
    label='Chart 4 - Filter by Race/Ethnicity:',
    options=['Select All', 'Hispanic', 'NH White', 'NH Black',
             'NH Asian/Native Hawaiian/Other Pacific Islands', 'NH American Indian/Alaska Native']
)

if chart_type2 == 'Select All':
    all_fig = px.pie(df, values='Residents Vaccinated', names='Dose',
             color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(all_fig)
else:
    plt.title(f'Dosage coverage for {chart_type2}')
    selected_df = df_dosage[df_dosage["Race/Ethnicity"] == f"{chart_type2}"]

    fig3 = px.pie(selected_df, values='Residents Vaccinated', names='Dose',
                color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig3)

st.markdown('''
**Observations**
- Among the vaccinated population, only 21.7% have completed their vaccination regimen.

*Please choose to view the statistics for individual racial groups.*
''')
