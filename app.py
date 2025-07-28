import streamlit as st
import streamlit.components.v1 as htmlviewer
st.set_page_config(layout="wide",page_title='성현준의 문제해결' )

# Title Msg#1
st.title('This is JUN_JUN Webapp!!')


with open('./index.html', 'r', encoding='utf-8') as f: 
    html = f.read()
    f.close()


# Box#1(4), Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)
    with st.expander('Content #2...'):
        st.write(html, height=600, unsafe_allow_html=True)
    with st.expander('Content #3...'):
        st.write(html, height=600, unsafe_allow_html=True)


        
with col2:
    with st.expander('Tips..'):
        st.info('Tips..')
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by Hyeon Jun', unsafe_allow_html=True)