import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="지하철 시간대별 하차 인원 지도", layout="wide")
st.title("🗺️ 지하철 시간대별 하차 인원 지도 시각화")

# 파일 업로드
st.subheader("① 📂 시간대별 하차 인원 파일 업로드")
stat_file = st.file_uploader("▶️ '지하철역', 시간대별 하차 인원 열이 포함된 파일", type=["csv"], key="stat")

st.subheader("② 📂 지하철역 위치 정보 파일 업로드")
loc_file = st.file_uploader("▶️ '지하철역', '위도', '경도' 열이 포함된 파일", type=["csv"], key="loc")

if stat_file and loc_file:
    try:
        # 파일 읽기
        stat_df = pd.read_csv(stat_file, encoding='cp949')
        loc_df = pd.read_csv(loc_file, encoding='cp949')

        # 🔧 열 이름과 문자열 정리
        stat_df.columns = stat_df.columns.str.strip()
        loc_df.columns = loc_df.columns.str.strip()
        stat_df['지하철역'] = stat_df['지하철역'].str.strip()
        loc_df['지하철역'] = loc_df['지하철역'].str.strip()

        # 🎯 시간대 열 목록 가져오기 (3번째 열부터)
        time_columns = stat_df.columns[1:]  # 지하철역 제외한 열만
        selected_time = st.selectbox("⏰ 시각 선택 (하차 인원)", time_columns)

        # 병합
        merged_df = pd.merge(stat_df[['지하철역', selected_time]], loc_df, on="지하철역", how="inner")

        # 숫자 변환
        merged_df[selected_time] = pd.to_numeric(merged_df[selected_time], errors='coerce')
        merged_df = merged_df.dropna(subset=['위도', '경도', selected_time])

        # 지도 시각화
        st.subheader(f"📍 선택한 시간대 하차 인원 지도: {selected_time}")
        fig = px.scatter_mapbox(
            merged_df,
            lat="위도",
            lon="경도",
            size=selected_time,
            color=selected_time,
            hover_name="지하철역",
            color_continuous_scale="Viridis",
            size_max=30,
            zoom=10,
            title=f"📌 {selected_time} 기준 지하철 하차 인원"
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
