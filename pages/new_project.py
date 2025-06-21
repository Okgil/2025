import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="지하철 하차 인원 시각화", layout="wide")
st.title("🚇 17시-18시 지하철 하차 인원 비교")

uploaded_file = st.file_uploader("📂 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # 🔍 인코딩 지정
        df = pd.read_csv(uploaded_file, encoding='cp949')  # 또는 encoding='euc-kr'

        # 필수 열 확인
        if '지하철역' not in df.columns or '17시-18시 하차인원' not in df.columns:
            st.error("❌ CSV 파일에 '지하철역' 또는 '17시-18시 하차인원' 열이 없습니다.")
        else:
            df['17시-18시 하차인원'] = pd.to_numeric(df['17시-18시 하차인원'], errors='coerce')
            df = df.dropna(subset=['17시-18시 하차인원'])
            df_sorted = df.sort_values(by='17시-18시 하차인원', ascending=False)

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

    except UnicodeDecodeError:
        st.error("❗ 파일 인코딩 오류: utf-8이 아닌 cp949 (또는 euc-kr)로 저장된 파일일 수 있습니다.")
    except Exception as e:
        st.error(f"파일을 처리하는 중 오류 발생: {e}")
else:
    st.info("⬆️ 위에 CSV 파일을 업로드하세요.")
