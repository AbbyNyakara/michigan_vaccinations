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

# Part 5
st.subheader('Chart 5- Residents Vaccinated Filtered by County')

#List the counties
counties = df['County'].unique()
#counties = np.insert(counties,0,'Select All')

age_group = df['Age Group'].unique()
race_ethnicity = df['Race/Ethnicity'].unique()
dose_administered = df['Dose'].unique()

st.write("Select county: ")
county_select  = st.selectbox(
    label = 'County:',
    options = counties
)

plt.figure(figsize=(10,6))

# User selected variables
selected_county = county_select

# Slice the df
sub_df = df[df['County'] == selected_county]
new_df = sub_df.groupby(['Age Group', 'Dose'])['Residents Vaccinated'].sum().reset_index()

#new_df

plt6 = sns.barplot(new_df, x="Age Group", y="Residents Vaccinated", width=0.6, errorbar=None)
plt6.bar_label(plt6.containers[0], fontsize=7)
plt6.set_xticklabels(plt6.get_xticklabels(),
                    rotation=20, ha="right", fontsize=7)
st.pyplot(plt6.get_figure())

st.markdown('''
**Graphs:**

*The graphs illustrate the vaccination counts for each county, classified by age-group.*
''')
