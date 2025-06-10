import streamlit as st
import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("seoul_card_sales.csv", encoding="cp949")

# 🔍 열 이름 확인
st.write("CSV 열 이름 보기:", df.columns.tolist())
