# Streamlit 머신러닝
# 1-1. 머신러닝 라이브러리/패키지 requirements에 설치
# 1-2. 데이터, 패러미터들로 모델 훈련 -> 모델 사용
# 훈련에 많은 시간 안 걸리는 경우
# 2. Colab, Jupiter Notebook ... -> pkl 모델 파일 -> joblib 읽어들여와서 쓰는 방법
# 훈련 자체 시간이 많이 걸린다, 결과값만 빠르게 보여주고 싶다
# streamlit 라이브러리 호출

# with st.echo()를 통해서 코드를 어떻게 썼는지 확인가능
import streamlit as st
with st.echo(code_location="below"):
    import pandas as pd

    df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
    st.write(df)

with st.echo():
    import joblib # 사이킷런 import 안해도 model 객체 자체를 pkl로 불러옴
    import os
    # os.path... 파이썬 경로문제 해결
    model_path = f"{os.path.dirname(os.path.abspath(__file__))}/model.pkl"
    model = joblib.load(model_path)
    st.write("## 선형 회귀 모델")
    st.write(pd.Series(model.coef_, index=["age", "bmi", "children", "smoker", "sex_male", "region_northwest", "region_northeast", "region_southwest"]))


import streamlit as st
import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv")

st.title('데이터 모델 배포하기')

if st.checkbox('원본 데이터 보기'):
    st.subheader('Raw data')
    st.write(df)

import joblib #  사이킷런 import
import os
# os.path... 파이썬 경로문제 해결
model_path = f"{os.path.dirname(os.path.abspath(__file__))}/model.pkl"
model = joblib.load(model_path)
st.write("## 선형 회귀 모델")
st.write(pd.Series(model.coef_, index=["age", "bmi", "children", "smoker", "sex_male", "region_northwest", "region_northeast", "region_southwest"]))
#coef_로 잘불러왔는지 확인

# age : 나이
st.number_input(
    label="나이",
    step=1, 
    value=30,
    key='age'
)
# st.session_state['age']
# st.write(st.session_state['age'])

# sex : 성별
st.radio(
    label='성별',
    options=["남성", "여성"],
    index=0, # 기본 선택
    key='sex'
)
# st.write(st.session_state['sex'])

# bmi : 실수형
st.number_input(
    label="BMI",
    step=0.1, # 실수형으로 받을 수 있게
    value=25.0,
    key='bmi'
)
# st.write(st.session_state['bmi'])

# children : 자녀수
st.number_input(
    label="자녀수",
    step=1, 
    value=1,
    key='children'
)
# st.write(st.session_state['children'])

# smoker : 흡연여부
st.checkbox(
    label='흡연여부',
    value=False,
    key='smoker'
)
# st.write(st.session_state['smoker'])

# region : 지역
st.selectbox(
    label="지역",
    options=["북동", "북서", "남동", "남서"],
    index=2,
    key='region'
)
# st.write(st.session_state['region'])

if st.button('예측'):
    st.snow()
    # 예측
    # model.predict(X_test) -> 전처리한 데이터 형태로 들어간 행렬, df.
    # df X -> 이중 리스트 ([])
    # [ [age,bmi,children,smoker,sex_male,
    #    region_northwest,region_northeast,region_southwest] ]
    state = st.session_state
    st.write(st.session_state)
    # model.predict(...)
    # 예측에 쓰일 여러개의 행들
    # 행 -> (df -> 독립변수들을 담은 행들 - 1개~)
    # 한줄로 만듦
    row = [[
        state['age'], state['bmi'], state['children'], state['smoker'],
        state['sex'] == '남성', state['region'] == '북서',
        state['region'] == '북동', state['region'] == '남서'
    ]]
    pred = model.predict(row) # y값 하나만 나옴
    # ([row,row,row]) => 여러개 결과 ->  y값의 리스트
    #st.write(pred[0]) 우리가 한줄만 입력했으니까
    st.metric(label='예측값', value=pred[0]) # 예측값의 결과를 담은 것

    # 전처리하는 과정만 잘 정의할 수 있으면
    # 파일을 upload 