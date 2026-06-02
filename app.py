import streamlit as st
import random

# 저녁 메뉴 리스트
menus = [
    "치킨",
    "피자",
    "햄버거",
    "떡볶이",
    "라면",
    "초밥",
    "제육볶음",
    "삼겹살",
    "돈까스",
    "파스타",
    "김치찌개",
    "카레",
    "마라탕",
    "샌드위치",
    "쌀국수"
]

# 페이지 설정
st.set_page_config(
    page_title="저녁 메뉴 추천기",
    page_icon="🍽️"
)

# 제목
st.title("🍽️ 저녁 메뉴 추천기")

st.write("버튼을 누르면 오늘 저녁 메뉴를 추천해줘!")

# 버튼
if st.button("메뉴 추천받기"):
    menu = random.choice(menus)
    st.success(f"오늘의 저녁 메뉴는 👉 **{menu}**")

# 메뉴 추가 기능
st.subheader("메뉴 직접 추가하기")

new_menu = st.text_input("추가할 메뉴 입력")

if st.button("메뉴 추가"):
    if new_menu.strip() == "":
        st.warning("메뉴를 입력해주세요!")
    else:
        menus.append(new_menu)
        st.success(f"'{new_menu}' 메뉴가 추가되었어요!")

# 현재 메뉴 목록 보기
with st.expander("현재 메뉴 목록 보기"):
    for m in menus:
        st.write(f"- {m}")
import streamlit as st
from google import genai
from google.genai import types

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💝",
    layout="centered"
)

st.title("💝 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# -----------------------------
# API 키 불러오기
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error(
        "API 키를 찾을 수 없습니다.\n\n"
        "Streamlit Secrets에 GEMINI_API_KEY를 등록해주세요."
    )
    st.stop()

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요 😊\n\n"
                "연애 고민, 썸, 재회, 이별, 커뮤니케이션 등 "
                "무엇이든 편하게 이야기해주세요."
            )
        }
    ]

# -----------------------------
# 채팅 기록 출력
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("연애 고민을 입력하세요")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # AI 응답 생성
    with st.chat_message("assistant"):
        response_placeholder = st.empty()

        try:
            # 시스템 프롬프트
            system_prompt = """
당신은 공감 능력이 뛰어난 연애상담 전문가입니다.

규칙:
- 사용자의 감정을 존중한다.
- 비난하거나 단정하지 않는다.
- 현실적이고 구체적인 조언을 제공한다.
- 위험하거나 유해한 행동은 권장하지 않는다.
- 답변은 자연스럽고 따뜻한 한국어로 작성한다.
- 필요하면 추가 질문을 통해 상황을 파악한다.
"""

            # 대화 이력 구성
            history_text = ""

            for msg in st.session_state.messages:
                role = "사용자" if msg["role"] == "user" else "상담사"
                history_text += f"{role}: {msg['content']}\n"

            prompt = f"""
{system_prompt}

대화 기록:
{history_text}

상담사:
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.8,
                    max_output_tokens=1000,
                )
            )

            answer = response.text

            response_placeholder.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:
            error_msg = (
                "⚠️ 답변 생성 중 오류가 발생했습니다.\n\n"
                f"오류 내용: {str(e)}"
            )

            response_placeholder.error(error_msg)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_msg
                }
            )

# -----------------------------
# 채팅 초기화 버튼
# -----------------------------
st.divider()

if st.button("🗑️ 대화 초기화"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요 😊\n\n"
                "연애 고민을 편하게 이야기해주세요."
            )
        }
    ]
    st.rerun()
