import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import time

# 페이지 설정
st.set_page_config(layout="wide", page_title="성현준의 문제해결")
st.title("This is JUN_JUN Webapp!!")

# HTML 파일 경로 설정
base         = Path(__file__).parent
index_path   = base / "index.html"
jndex_path   = base / "jndex.html"
kndex_path   = base / "kndex.html"
mndex_path   = base / "mndex.html"
zndex_path   = base / "zndex.html"

# HTML 읽기
html1 = index_path.read_text(encoding="utf-8")
html2 = jndex_path.read_text(encoding="utf-8")
html3 = kndex_path.read_text(encoding="utf-8")
html4 = mndex_path.read_text(encoding="utf-8")
html5 = zndex_path.read_text(encoding="utf-8")

# (왼쪽 expander 제목, 왼쪽 렌더링 함수, 오른쪽 팁 텍스트) 쌍 목록
pairs = [
    (
        "비버 챌린지 1. 짐 옮기기",
        lambda: components.html(html1, height=700, scrolling=True),
        "짐을 다 옮기는 순간의 시간을 찾는다."
    ),
    (
        "비버 챌린지 2. 짐 옮기기2",
        lambda: components.html(html2, height=700, scrolling=True),
        "1층은 이미 짐이 도착한 층이다."
    ),
    (
        "강화 타이밍 자동화",
        lambda: components.html(html3, height=900, scrolling=True),
        "강화 타이밍에 대한 팁을 여기에 입력하세요."
    ),
    (
        "AI 강화 타이밍 예측",
        lambda: components.html(html4, height=600, scrolling=True),
        "AI 적용은 하지 못했습니다.  \n  \n open AI, 브라우져 내 예측 통합 등을 사용"
    ),
    (
        "룰 기반 강화 타이밍 계산",
        lambda: components.html(html5, height=600, scrolling=True),
        "룰 기반 전문가 시스템  \n  \n 기본 강화는 3번  \n  \n 문제행동 빈도&강도 심할 경우 강화 증가."
    ),
]

# 각 expander와 팁을 1:1 대응시켜 렌더링
for title, render_left, tip_text in pairs:
    left_col, right_col = st.columns((4, 1))
    if title == "강화 타이밍 자동화":
        with left_col:
            with st.expander(title):
                # 1) 기존 차트 HTML 렌더링
                components.html(html3, height=900, scrolling=True)


        with right_col:
            with st.expander("팁"):
                st.info("시작 교시 문제행동 빈도와 강도를 체크해주세요.")
    else:
        # 나머지 expander는 원래대로
        with left_col:
            with st.expander(title):
                render_left()
        with right_col:
            with st.expander("팁"):
                st.info(tip_text)
# 하단 푸터
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<p style="color:blue; text-align:center;">'
    '© All rights reserved by Hyeon Jun'
    '</p>',
    unsafe_allow_html=True
)
