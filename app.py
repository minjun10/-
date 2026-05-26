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
