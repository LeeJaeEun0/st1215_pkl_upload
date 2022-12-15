import streamlit as st
import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv")

st.title('데이터 모델 배포하기')

if st.checkbox('원본 데이터 보기'):
    st.subheader('Raw data')
    st.write(df)

