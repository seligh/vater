import streamlit as st
from datetime import date


st.sidebar.title("MENU")
menu = st.sidebar.selectbox("눌러서 선택", ["홈", "인재", "버튼"])
# 웹페이지 제목
if menu == '홈':
    st.title("아빠 생신 축하드려요 🎉")

    # 오늘의 날짜
    today = date.today()
    specific_date = date(1982, 6, 20)
    days_difference = (today - specific_date).days

    con = st.container(border=True)
    # 생일 축하 메시지
    con.markdown("### 맛도 좋고 몸에도 좋은 생일 케이크")
    st.markdown(f"### :rainbow[오늘이 {today.year}년 {today.month}월 {today.day}일이니까 태어난지 D+{days_difference}일]")
    st.markdown("### 나이 많이 드셨네")
    st.markdown("이거 매일 업데이트 돼요 신기하죠")

    # 생일 이미지 (이미지 URL을 원하는 이미지로 변경하세요)
    con.image("https://i.imgur.com/ZiPT4mH.jpg", caption="겁나 비싼 케이크")

    # 생일 축하 음악 (YouTube 링크)
    con.write("🎶 [생일 축하 노래](https://youtu.be/Xf5w8beE8Ow?si=6ezfWYyx-atxooNQ) 🎶")

if menu == '인재':
    st.markdown('#### 솔직히 이정도면 겁나 노력했다 그죠')
    st.markdown('#### 흠 뭐적지')
    concon = st.container(border=True)
    concon.markdown("**인재**의 다른 뜻은 다음과 같다.")
    concon.markdown("- **인재**(人才): 재주가 매우 뛰어난 사람")
    concon.markdown("- **인재**(人災): 인간에 의해 발생하는 재난")
    concon.markdown("[출처] (https://ko.wikipedia.org/wiki/%EC%9D%B8%EC%9E%AC)")
    concon.markdown(":orange[위에 꺼가 아무래도 좋겠죠?]")

if menu == '버튼':
    if st.button('눌러봐요'):
        st.balloons()
        st.markdown("## :rainbow[신기하죠]")
    if st.button('이것도 눌러봐요'):
        st.snow()
        st.markdown("## :rainbow[쩔죠]")
