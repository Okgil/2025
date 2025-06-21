import streamlit as st

# 🌟 Streamlit 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천 💼",
    page_icon="🧠",
    layout="wide"
)

# 🎨 스타일 설정
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

# 🔠 타이틀 출력
st.markdown('<div class="big-title">🧬 MBTI로 알아보는 진로 추천 💼</div>', unsafe_allow_html=True)
st.markdown("### 💡 MBTI 유형을 선택하면 ✨ 어울리는 직업 ✨을 추천해줄게요!")
st.markdown("---")

# 📋 MBTI 목록과 직업 매핑 (16개 전체)
mbti_jobs = {
    "INTJ 🧠🎯": ["전략 컨설턴트 📊", "과학자 🔬", "AI 엔지니어 🤖", "기획자 📈"],
    "INTP 📚🔍": ["데이터 과학자 🧮", "이론 물리학자 ⚛️", "UX 디자이너 🖌️", "게임 개발자 🎮"],
    "ENTJ 🏆🚀": ["CEO 🧑‍💼", "프로젝트 매니저 📋", "변호사 ⚖️", "경영 컨설턴트 💼"],
    "ENTP 🧨🗣️": ["스타트업 창업자 🚀", "방송작가 📺", "정치인 🎙️", "혁신가 💡"],

    "INFJ 🔮📚": ["상담심리사 🧘", "작가 ✍️", "사회운동가 🌍", "종교인 ⛪"],
    "INFP 🎨🌱": ["예술가 🎭", "시인 📝", "사회복지사 ❤️", "아동문학 작가 📖"],
    "ENFJ 🧑‍🏫💬": ["교사 👩‍🏫", "홍보 담당자 📢", "사회활동가 ✊", "코치 🗣️"],
    "ENFP 💥🎉": ["마케터 📣", "크리에이터 🎬", "여행가 ✈️", "기획자 📅"],

    "ISTJ 📏🛠️": ["회계사 🧾", "법무사 ⚖️", "데이터 관리자 📊", "경찰관 🚓"],
    "ISFJ 🤗🛡️": ["간호사 🏥", "초등교사 🏫", "사서 📚", "비서 📋"],
    "ESTJ 🧱📢": ["군인 🎖️", "경영자 🧑‍💼", "행정직 공무원 🏛️", "감독관 🕵️‍♂️"],
    "ESFJ 🤝💖": ["병원코디네이터 🏥", "이벤트 플래너 🎪", "HR 매니저 👥", "상담 교사 👩‍🏫"],

    "ISTP 🛠️🧩": ["정비사 🔧", "파일럿 🛫", "응급구조사 🚑", "소방관 🚒"],
    "ISFP 🎨🍃": ["패션디자이너 👗", "플로리스트 💐", "사진작가 📸", "요리사 🍳"],
    "ESTP ⚡🏎️": ["트레이더 💹", "스타트업 운영자 🚀", "프로 운동선수 🏋️", "영업 담당자 📞"],
    "ESFP 🌟🎤": ["방송인 🎤", "연예인 🎬", "헤어디자이너 ✂️", "여행 인플루언서 🧳"]
}

# 🔍 직업 설명 (간단 예시)
mbti_job_descriptions = {
    "INTJ 🧠🎯": {
        "전략 컨설턴트 📊": "기업 전략을 수립하고 방향성을 제시하는 두뇌파 직업이에요.",
        "과학자 🔬": "자연의 원리를 탐구하며, 지적인 도전을 즐기는 INTJ에게 적합해요.",
        "AI 엔지니어 🤖": "미래 기술을 선도하는 인공지능 개발자. 논리적 사고가 중요한 직업이에요.",
        "기획자 📈": "아이디어를 계획으로 구체화하는 역할! 창조와 전략을 모두 좋아하는 INTJ에게 딱이에요."
    },
    "INFP 🎨🌱": {
        "예술가 🎭": "자신의 내면 세계를 표현하는 자유로운 영혼!",
        "시인 📝": "섬세한 감정을 언어로 표현하는 아름다운 직업이에요.",
        "사회복지사 ❤️": "타인을 돕고 싶은 마음이 큰 INFP에게 잘 맞아요.",
        "아동문학 작가 📖": "순수함을 담아 아이들에게 상상력을 전달하는 작가!"
    },
    "ENFP 💥🎉": {
        "마케터 📣": "세상을 떠들썩하게 만들 아이디어 뱅크!",
        "크리에이터 🎬": "SNS와 유튜브 등에서 자신을 표현하는 자유로운 직업이에요.",
        "여행가 ✈️": "새로운 세상을 탐험하고 콘텐츠로 풀어내는 삶!",
        "기획자 📅": "아이디어를 현실로 만들고 팀을 이끄는 데 탁월한 역량을 보여줘요."
    },
    # 필요한 경우 아래 유형도 비슷한 방식으로 추가 가능
}

# MBTI 선택
mbti_choice = st.selectbox("🔍 당신의 MBTI 유형을 선택하세요:", list(mbti_jobs.keys()))

# 추천 직업 출력
st.markdown("## 📌 추천 직업 목록")
st.markdown('<div class="mbti-card">', unsafe_allow_html=True)

for job in mbti_jobs[mbti_choice]:
    with st.expander(f"👉 {job}"):
        description = mbti_job_descriptions.get(mbti_choice, {}).get(job, "설명이 준비 중이에요! 🎈")
        st.markdown(description)

st.markdown('</div>', unsafe_allow_html=True)

# 마무리
st.markdown("---")
st.markdown("🎁 **당신의 개성과 잘 어울리는 직업을 탐색해보세요!**")
st.markdown("💡 MBTI는 참고용! 당신의 진짜 가능성은 무한해요 🌌")
