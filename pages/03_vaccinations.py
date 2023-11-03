import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import numpy as np

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
alt.data_transformers.enable('default', max_rows=6000)

df = pd.read_csv('michigan_vaccinations.csv')


# Chart 2 - Vaccination Rates by Race.

st.subheader('Vaccinations by Race')
st.write('The graphs show the number of people vaccinated classified by race.')

administered_by_race = df.groupby(
    'Race/Ethnicity')['Residents Vaccinated'].sum().reset_index()

# Plot:
fig2 = px.pie(administered_by_race, values='Residents Vaccinated', names='Race/Ethnicity',
              color_discrete_sequence=px.colors.sequential.Plasma_r)
st.plotly_chart(fig2)

st.markdown('''
*of course this would make sense: considering the census statistics outlined at the beginning*
            
- A better comparison would be comparing the specific races against people vaccinated in that race. 
''')

st.subheader("Total Coverage by Race")

st.write('The chart displays the percentage of a certain ethnicity that got the vaccine. ')

df_dosage = df.groupby(['Race/Ethnicity', 'Dose']
                       )['Residents Vaccinated'].sum().reset_index()
df_dosage_grouped = df_dosage.groupby(
    'Race/Ethnicity')['Residents Vaccinated'].sum().reset_index()
df_dosage_grouped = df_dosage_grouped.assign(
    Population=[571944, 70238, 371262, 1414810, 7906881, 0])

# CHART 4
df_dosage_grouped['Percentage vaccinated'] = df_dosage_grouped['Residents Vaccinated'] / \
    df_dosage_grouped['Population'] * 100
df_dosage_grouped = df_dosage_grouped.drop(5)

# All vaccinated people
plt.figure(figsize=(8, 6))
plt.title('Dose Coverage by Race')
plt4 = sns.barplot(df_dosage_grouped, x="Race/Ethnicity",
                   y="Percentage vaccinated", errorbar=None, color='pink')
plt4.bar_label(plt4.containers[0], fontsize=8)
plt4.set_xticklabels(plt4.get_xticklabels(),
                     rotation=20, ha="right", fontsize=8)
plt4.set_ylim(0, 100)
st.pyplot(plt4.get_figure())

st.markdown('''
    ###### Observations
    - The Native Asian and Native Hawaiian populations exhibited the highest vaccination rates, 
        with approximately 72% of the total population in these groups having received the vaccine.
    - Approximately 67.8% of the White and Hispanic population have been vaccinated.
    - In contrast, only about 45.1% of the American Indian population and 52.4% of the total
         Black population in Michigan have received the vaccine.
    ''')

