import streamlit as st
from datetime import date


st.sidebar.title("MENU")
menu = st.sidebar.selectbox("눌러서 선택", ["홈", "버튼"])
# 웹페이지 제목
if menu == '홈':
    st.title("라은이 안녕")

    # 오늘의 날짜
    today = date.today()
    specific_date = date(2023, 10, 25)
    days_difference = (today - specific_date).days

    con = st.container(border=True)
    # 생일 축하 메시지
    con.markdown("### 짠 아까 너가 그린거")
    st.markdown(f"### :rainbow[오늘이 {today.year}년 {today.month}월 {today.day}일이니까 떠든지 {days_difference}일 째야]")
    st.markdown("이거 자동으로 매일 업데이트 된다? 신기하지")

    # 생일 이미지 (이미지 URL을 원하는 이미지로 변경하세요)
    con.image("https://i.imgur.com/wmDsIRk.jpg", caption="바부")

    # 생일 축하 음악 (YouTube 링크)
    con.write("🎶 [너가 좋아하는 노래](https://youtu.be/SHQ0tGLuY6A?si=m2Oz95UCc_AVVf3x) 🎶")


if menu == '버튼':
    if st.button('눌러봐'):
        st.balloons()
        st.markdown("## :rainbow[신기하지]")
    if st.button('이것도 눌러봐'):
        st.snow()
        st.markdown("## :rainbow[쩔지]")
