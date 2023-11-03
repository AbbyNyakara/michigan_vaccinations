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

# chart 1 - Option 1
st.subheader('2.0 Data Exploration')
st.write('Chart 1 - Residents Vaccinated by age-group')

administered_doses = df.groupby(
    'Age Group')['Residents Vaccinated'].sum().reset_index()

chart_type1 = st.selectbox(
    label='Select the chart type:',
    options=['Bar Graph', 'Pie Chart']
)

if chart_type1 == 'Bar Graph':
    new_order = [9, 10, 5, 0, 1, 2, 3, 4, 6, 7, 8]
    administered_doses = administered_doses.iloc[new_order]
    residents_vaccinated = sns.barplot(x='Residents Vaccinated', y="Age Group",
                                       data=administered_doses, errwidth=0, palette="dark:#5A9_r")
    for i in residents_vaccinated.containers:
        residents_vaccinated.bar_label(i,)
    st.pyplot(residents_vaccinated.get_figure())
else:
    fig1 = px.pie(administered_doses, values='Residents Vaccinated', names='Age Group',
                  color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig1)

st.write("A larger proportion of older individuals have received vaccinations in comparison to their younger counterparts.")
