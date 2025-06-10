import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 불러오기
df = pd.read_csv("seoul_card_sales.csv", encoding="cp949", header=None)

# 주요 열만 선택하고 이름 붙이기
df = df[[0, 4, 7]]
df.columns = ["연월", "지역", "카드사용금액"]

# Streamlit 앱 제목
st.title("서울 소비 트렌드 분석 대시보드")
st.markdown("서울 주요 지역의 카드 소비 데이터를 시각화한 웹 앱입니다.")

# 지역 선택
area_list = df["지역"].unique()
selected_area = st.selectbox("지역을 선택하세요", area_list)

# 선택한 지역의 데이터 필터링
filtered = df[df["지역"] == selected_area]

# 월별 소비 금액 그래프 출력
fig = px.line(filtered, x="연월", y="카드사용금액", title=f"{selected_area} 월별 소비 금액 추이")
st.plotly_chart(fig)
