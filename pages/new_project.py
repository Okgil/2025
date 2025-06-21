
import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="지하철 하차 인원 시각화", layout="wide")

st.title("🚇 17시-18시 지하철 하차 인원 비교")
st.markdown("CSV 파일을 업로드하면 역별 하차 인원을 시각화합니다.")

# 📁 CSV 업로드 받기
uploaded_file = st.file_uploader("📂 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # CSV 읽기
        df = pd.read_csv(uploaded_file)

        # 필수 열 확인
        if '지하철역' not in df.columns or '17시-18시 하차인원' not in df.columns:
            st.error("❌ CSV 파일에 '지하철역' 또는 '17시-18시 하차인원' 열이 없습니다.")
        else:
            # 숫자형으로 변환 (혹시 문자열로 되어 있다면)
            df['17시-18시 하차인원'] = pd.to_numeric(df['17시-18시 하차인원'], errors='coerce')

            # 결측값 제거 및 정렬
            df = df.dropna(subset=['17시-18시 하차인원'])
            df_sorted = df.sort_values(by='17시-18시 하차인원', ascending=False)

            # 시각화
            st.subheader("📊 하차 인원 많은 순서대로 보기")
            fig = px.bar(
                df_sorted,
                x='지하철역',
                y='17시-18시 하차인원',
                color='17시-18시 하차인원',
                color_continuous_scale='Blues',
                title='🚇 지하철역별 17시-18시 하차 인원',
                labels={'17시-18시 하차인원': '하차 인원'}
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"파일을 처리하는 중 오류 발생: {e}")
else:
    st.info("⬆️ 위에 CSV 파일을 업로드하세요.")
