import streamlit as st

st.title("Please answer the following questions based on your experience with previous questions AI decision support aids")
IF_1=st.slider("The interactive features encouraged me to think critically about my decisions", 1, 7, key="IF_1")
IF_2=st.slider("I considered multiple perspectives before making my decisions", 1, 7, key="IF_2")
IF_3=st.slider("The interactive features made the dilemmas feel more real or emotionally engaging", 1, 7, key="IF_3")
IF_4=st.slider("I reflected on my own values when making my decisions", 1, 7, key="IF_4")
IF_5=st.slider("The interactive features changed the way I viewed the dilemmas", 1, 7, key="IF_5")
IF_6=st.slider("The interactive features helped me determine what I individually think", 1, 7, key="IF_6")
IF_7=st.slider("I felt more confident in the decisions I made after using the interactive features", 1, 7, key="IF_7")

if st.button("Confirm"):
    st.session_state['C3_questions'] = [IF_1, IF_2, IF_3, IF_4, IF_5, IF_6, IF_7]
    if st.session_state['condition_questionnaire'] == 3:
        st.switch_page("pages/post_study_questions.py")
    else:    
        st.switch_page("pages/questions.py")