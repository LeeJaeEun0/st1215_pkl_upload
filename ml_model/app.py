import streamlit as st
import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv")

if st.checkbox('원본 데이터 보기'):
    st.subheader('Raw data')
    st.write(df)

