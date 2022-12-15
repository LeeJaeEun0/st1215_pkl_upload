import streamlit as st
import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv")

st.title('데이터 모델 배포하기')

if st.checkbox('원본 데이터 보기'):
    st.subheader('Raw data')
    st.write(df)

import joblib
import os
# os.path... 파이썬 경로문제 해결
model_path = f"{os.path.dirname(os.path.abspath(__file__))}/model.pkl"
model = joblib.load(model_path)
st.write("## 선형 회귀 모델")
st.write(pd.Series(model.coef_, index=["age", "bmi", "children", "smoker", "sex_male", "region_northwest", "region_northeast", "region_southwest"]))
