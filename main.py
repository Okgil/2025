import streamlit as st

# ----- 🎨 웹앱 스타일 설정 -----
st.set_page_config(
    page_title="MBTI 직업 추천 🎯",
    page_icon="🧠",
    layout="wide"
)

st.markdown(
    """
    <style>
        body {
            background-color: #f7f4ff;
        }
        .big-title {
            font-size: 48px;
            text-align: center;
            color: #6a0dad;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .mbti-card {
            background-color: #ffffffcc;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        }
        .job {
            font-size: 24px;
            margin: 0.5rem 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- 🎉 타이틀 -----
st.markdown('<div class="big-title">🧬 MBTI로 알아보는 진로 추천 💼</div>', unsafe_allow_html=True)
st.markdown("### 💡 MBTI 유형을 선택하면 ✨ 어울리는 직업 ✨을 추천해줄게요!")
st.markdown("---")

# ----- 🎯 MBTI 직업 매핑 -----
mbti_jobs = {
    "INTJ 🧠🎯": ["전략 컨설턴트 📊", "과학자 🔬", "AI 엔지니어 🤖", "기획자 📈"],
    "INFP 🎨🌱": ["작가 ✍️", "심리상담가 🧘", "예술가 🎭", "사회복지사 ❤️"],
    "ENFP 💥🎉": ["마케터 📣", "방송인 🎤", "여행가 ✈️", "크리에이터 🎬"],
    "ISTJ 📏🛠️": ["회계사 🧾", "공무원 🏛️", "데이터 분석가 📊", "엔지니어 ⚙️"],
    "ESTP ⚡🏎️": ["기업가 💼", "트레이더 💹", "스턴트맨 🎢", "운동선수 🏅"],
    "ESFJ 🤝💖": ["교사 🏫", "간호사 🏥", "HR 매니저 👥", "이벤트 플래너 🎪"],
    "INFJ 🔮📚": ["철학자 📜", "카운슬러 🧘", "작가 ✒️", "NGO 활동가 🌍"],
    "ENTP 🧨🗣️": ["스타트업 CEO 🚀", "정치인 🎙️", "방송작가 📺", "혁신가 💡"],
    # 나머지 유형도 추가 가능!
}

# ----- 🎯 사용자 선택 -----
mbti_choice = st.selectbox("🔍 당신의 MBTI 유형을 선택하세요:", list(mbti_jobs.keys()))

# ----- 💼 추천 결과 -----
st.markdown("## 📌 추천 직업 목록")

st.markdown('<div class="mbti-card">', unsafe_allow_html=True)

for job in mbti_jobs[mbti_choice]:
    st.markdown(f"<div class='job'>👉 {job}</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ----- 🎉 마무리 -----
st.markdown("---")
st.markdown("🎁 **당신의 개성과 잘 어울리는 직업을 탐색해보세요!**")
st.markdown("💡 MBTI는 참고용! 당신의 진짜 가능성은 무한해요 🌌")
