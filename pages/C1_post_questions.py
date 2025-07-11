import streamlit as st

E1=st.slider("The explanations encouraged me to think critically about my decisions", 1, 7, key=E1)
E2=st.slider("I considered multiple perspectives before making my decisions", 1, 7, key=E2)
E3=st.slider("The explanations made the dilemmas feel more real or emotionally engaging", 1, 7, key=E3)
E4=st.slider("I reflected on my own values when making my decisions", 1, 7, key=E4)
E5=st.slider("The explanations changed the way I viewed the dilemmas", 1, 7, key=E5)
E6=st.slider("The explanations helped me determine what I individually think", 1, 7, key=E6)
E7=st.slider("I felt more confident in the decisions I made after viewing the explanations", 1, 7, key=E7)

if st.button("Confirm"):
    st.swtich_page("pages/questions.py")