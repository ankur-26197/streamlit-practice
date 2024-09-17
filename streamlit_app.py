import streamlit as st
import pandas as pd

st.title('Machine Learning app')

st.info('This app builds a ML model')

with st.expander('Data'):
  st.write('Raw data')
  
with st.expander('Data visualisation'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

