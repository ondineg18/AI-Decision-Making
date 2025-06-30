print('hello')
import streamlit as st

genre = st.radio(
    "What's your favorite color?",
    ["blue", "red", "purple"]
)
age = st.slider("", 0, 130, 0)
st.title("Ethical Decision-Making")
st.dataframe(data=None, width=None, height=None)
st.text_input(label="good", value="10", type="default")
options = st.multiselect(
    "What are some of the specific harms of not reporting your friend? Who is affected negatively? How will they feel?",
    ["sad", "angry", "despaired", "stressed", "guilty", "frustrated", "scared"]
    
)
