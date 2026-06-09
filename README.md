import streamlit as st

st.set_page_config(
    page_title="취미 인터뷰 & 수업 댓글 생성기",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 취미 인터뷰 & 수업 댓글 생성기")
st.write("취미에 대해 답하면 수업 댓글을 자동으로 생성합니다.")

# 이름
name = st.text_input("이름")

# 취미 선택
hobby_option = st.selectbox(
    "취미를 선택하세요",
    [
        "",
        "독서",
        "운동",
        "그림 그리기",
        "음악 감상",
        "악기 연주",
        "게임",
        "요리",
        "사진 촬영",
        "기타"
    ]
)

# 기타 선택 시
custom_hobby = ""
if hobby_option == "기타":
    custom_hobby = st.text_input("취미를 직접 입력하세요")

# 취미 시작 계기
reason = st.text_area("취미를 시작하게 된 계기")

# 취미 활동 내용
activity = st.text_area("주로 어떤 활동을 하나요?")

# 배운 점
lesson = st.text_area("취미를 통해 배운 점은 무엇인가요?")

if st.button("수업 댓글 생성"):
    try:
        hobby = custom_hobby.strip() if hobby_option == "기타" else hobby_option

        if not name.strip():
            st.warning("이름을 입력하세요.")
        elif not hobby:
            st.warning("취미를 선택하세요.")
        elif not reason.strip():
            st.warning("취미 시작 계기를 입력하세요.")
        elif not activity.strip():
            st.warning("취미 활동 내용을 입력하세요.")
        elif not lesson.strip():
            st.warning("배운 점을 입력하세요.")
        else:

            comment = (
                f"{name}은(는) {hobby}에 꾸준한 관심을 가지고 활동하고 있으며, "
                f"'{reason}'를 계기로 취미를 시작하였다. "
                f"평소 {activity} 활동에 적극적으로 참여하며 경험을 쌓고 있다. "
                f"특히 취미 활동을 통해 {lesson}의 가치를 배우고 실천하는 모습이 돋보인다. "
                f"자기주도적으로 관심 분야를 탐구하며 긍정적인 태도로 성장하고 있음."
            )

            st.success("수업 댓글 생성 완료!")

            st.text_area(
                "생성된 수업 댓글",
                value=comment,
                height=200
            )

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.markdown("---")
st.caption("취미 인터뷰 & 수업 댓글 생성기")
