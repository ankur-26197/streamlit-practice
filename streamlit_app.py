import streamlit as st

st.title('Machine Learning app')

st.info('This app builds a ML model')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df

