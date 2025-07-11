import streamlit as st

I1=st.slider("The images encouraged me to think critically about my decisions", 1, 7, key=I1)
I2=st.slider("I considered multiple perspectives before making my decisions", 1, 7, key=I2)
I3=st.slider("The images made the dilemmas feel more real or emotionally engaging", 1, 7, key=I3)
I4=st.slider("I reflected on my own values when making my decisions", 1, 7, key=I4)
I5=st.slider("The images changed the way I viewed the dilemmas", 1, 7, key=I5)
I6=st.slider("The images helped me determine what I individually think", 1, 7, key=I6)
I7=st.slider("I felt more confident in the decisions I made after viewing the images", 1, 7, key=I7)

if st.button("Confirm"):
    st.swtich_page("pages/questions.py")