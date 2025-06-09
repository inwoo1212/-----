import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 불러오기
df = pd.read_csv("seoul_card_sales_compressed.csv")

# Streamlit 앱 제목
st.title("서울 소비 트렌드 분석 대시보드")
st.markdown("서울시 자치구별 카드 소비 데이터를 시각화한 웹 앱입니다.")

# 자치구 선택
gu_list = df['GU_NAME'].unique()
selected_gu = st.selectbox("자치구를 선택하세요", gu_list)

# 선택한 자치구의 데이터 필터링
filtered = df[df['GU_NAME'] == selected_gu]

# 월별 소비 금액 그래프 출력
fig = px.line(filtered, x="USE_MONTH", y="AMT", title=f"{selected_gu} 월별 소비 금액 추이")
st.plotly_chart(fig)
