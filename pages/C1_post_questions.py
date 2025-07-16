import streamlit as st

st.title("Please answer the following questions based on your experience with the AI decision support aids in the previous questions")
E1=st.slider("The explanations encouraged me to think critically about my decisions", 1, 7, key="E1")
E2=st.slider("I considered multiple perspectives before making my decisions", 1, 7, key="E2")
E3=st.slider("The explanations made the dilemmas feel more real or emotionally engaging", 1, 7, key="E3")
E_attention=st.slider("Please select number 7 for this question. This is an attention-check question.", 1, 7, key="E_attention")
E4=st.slider("I reflected on my own values when making my decisions", 1, 7, key="E4")
E5=st.slider("The explanations changed the way I viewed the dilemmas", 1, 7, key="E5")
E6=st.slider("The explanations helped me determine what I individually think", 1, 7, key="E6")
E7=st.slider("I felt more confident in the decisions I made after viewing the explanations", 1, 7, key="E7")

if st.button("Confirm"):
    st.session_state['C1_questions'] = [E1, E2, E3, E_attention, E4, E5, E6, E7]
    if st.session_state['condition_questionnaire'] == 3:
        st.switch_page("pages/post_study_questions.py")
    else:    
        st.switch_page("pages/questions.py")