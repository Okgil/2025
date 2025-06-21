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
            font-size: 20px;
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
}

# 🔍 직업 설명 매핑
mbti_job_descriptions = {
    "INTJ 🧠🎯": {
        "전략 컨설턴트 📊": "기업의 문제를 진단하고 전략을 수립하는 역할. 분석력과 미래 예측력이 중요해요.",
        "과학자 🔬": "자연 현상과 이론을 탐구하고 실험을 통해 검증해요. 호기심이 많고 탐구적인 INTJ에게 적합!",
        "AI 엔지니어 🤖": "인공지능 시스템을 개발하고 데이터 기반 알고리즘을 설계하는 전문가예요.",
        "기획자 📈": "새로운 프로젝트나 상품을 기획하고 방향을 제시하는 두뇌파!"
    },
    "INFP 🎨🌱": {
        "작가 ✍️": "자신만의 세계를 글로 표현하는 예술가. 감수성이 풍부한 INFP에게 딱이에요.",
        "심리상담가 🧘": "사람의 마음을 듣고 치유하는 직업. 공감력 있는 INFP와 잘 맞아요.",
        "예술가 🎭": "그림, 음악, 연기 등 다양한 형태로 감정을 표현할 수 있어요.",
        "사회복지사 ❤️": "소외된 사람을 도우며 따뜻한 사회를 만드는 일. INFP의 이상과 맞닿아 있어요."
    },
    "ENFP 💥🎉": {
        "마케터 📣": "트렌드를 빠르게 캐치하고 아이디어를 현실화하는 열정맨!",
        "방송인 🎤": "사람들과 소통하며 에너지를 전파하는 직업. ENFP의 밝은 에너지를 살릴 수 있어요.",
        "여행가 ✈️": "자유롭고 다채로운 경험을 즐기며 콘텐츠도 만들 수 있는 직업.",
        "크리에이터 🎬": "YouTube, SNS 등에서 자기 표현! ENFP의 창의력을 발휘할 수 있어요."
    }
}

# ----- 🎯 사용자 선택 -----
mbti_choice = st.selectbox("🔍 당신의 MBTI 유형을 선택하세요:", list(mbti_jobs.keys()))

# ----- 💼 추천 결과 -----
st.markdown("## 📌 추천 직업 목록")

st.markdown('<div class="mbti-card">', unsafe_allow_html=True)

for job in mbti_jobs[mbti_choice]:
    with st.expander(f"👉 {job}"):
        st.markdown(mbti_job_descriptions[mbti_choice].get(job, "설명이 준비 중이에요!"))

st.markdown('</div>', unsafe_allow_html=True)

# ----- 🎉 마무리 -----
st.markdown("---")
st.markdown("🎁 **당신의 개성과 잘 어울리는 직업을 탐색해보세요!**")
st.markdown("💡 MBTI는 참고용! 당신의 진짜 가능성은 무한해요 🌌")
