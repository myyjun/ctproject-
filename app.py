import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 페이지 설정
st.set_page_config(layout="wide", page_title="성현준의 문제해결")

# 타이틀
st.title("This is JUN_JUN Webapp!!")

# 로컬 HTML 파일 경로
index_path   = Path(__file__).parent / "index.html"
jndex_path  = Path(__file__).parent / "jndex.html"

# HTML 읽기
html1 = index_path.read_text(encoding="utf-8")
html2 = jndex_path.read_text(encoding="utf-8")

# 레이아웃: 좌우 4:1 컬럼
col1, col2 = st.columns((4, 1))

with col1:
    # 1번 문제: index.html (탭·타이머 포함)
    with st.expander("비버 챌린지 1. 짐 옮기기"):
        components.html(
            html1,
            height=700,
            scrolling=True
        )

    # 2번 문제: jndex.html (새로운 CT 탭 UI)
    with st.expander("비버 챌린지 2. 짐 옮기기2"):
        components.html(
            html2,
            height=700,
            scrolling=True
        )

    # 3번 컨텐츠: 유튜브 영상
    with st.expander("Content #3..."):
        st.info("Content…")
        st.video("https://www.youtube.com/watch?v=XyEOEBsa8I4")

    # 4번 컨텐츠: 이미지
    with st.expander("이미지 가지고 오기"):
        st.image("image/비버1.jpg")

with col2:
    with st.expander("Tips.."):
        st.info("문제 해결의 힌트나 추가 설명을 여기에 넣으세요.")

# 하단 푸터
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<p style="color:blue; text-align:center;">'
    '© All rights reserved by Hyeon Jun'
    '</p>',
    unsafe_allow_html=True
)
