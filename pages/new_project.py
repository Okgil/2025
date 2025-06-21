import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="지하철 하차 인원 지도 시각화", layout="wide")
st.title("🗺️ 지하철 하차 인원 지도 시각화 (17시-18시)")

# 파일 업로드 받기
st.subheader("① 📂 시간대별 하차 인원 파일 업로드")
stat_file = st.file_uploader("▶️ '지하철역', '17시-18시 하차인원' 열이 포함된 파일", type=["csv"], key="stat")

st.subheader("② 📂 지하철역 위치 정보 파일 업로드")
loc_file = st.file_uploader("▶️ '지하철역', '위도', '경도' 열이 포함된 파일", type=["csv"], key="loc")

if stat_file and loc_file:
    try:
        # 두 CSV 파일 읽기 (인코딩 자동 감지 또는 cp949)
        stat_df = pd.read_csv(stat_file, encoding='cp949')
        loc_df = pd.read_csv(loc_file, encoding='cp949')

        # 병합
        merged_df = pd.merge(stat_df, loc_df, on="지하철역", how="inner")

        # 데이터 전처리
        merged_df['17시-18시 하차인원'] = pd.to_numeric(merged_df['17시-18시 하차인원'], errors='coerce')
        merged_df = merged_df.dropna(subset=['위도', '경도', '17시-18시 하차인원'])

        # 시각화
        st.subheader("📍 하차 인원 지도 시각화")
        fig = px.scatter_mapbox(
            merged_df,
            lat="위도",
            lon="경도",
            size="17시-18시 하차인원",
            color="17시-18시 하차인원",
            hover_name="지하철역",
            color_continuous_scale="Viridis",
            size_max=30,
            zoom=10,
            title="📌 17시-18시 지하철 하차 인원 (지도로 보기)"
        )

        fig.update_layout(
            mapbox_style="open-street-map",
            margin={"r": 0, "t": 40, "l": 0, "b": 0}
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"🚨 오류 발생: {e}")

else:
    st.info("두 개의 파일을 모두 업로드해 주세요.")
