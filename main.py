import streamlit as st
from utils import *
from constant import *

hide_sidebar()

if "PID" not in st.session_state:
    st.session_state['PID'] = -1

st.title("Welcome to our study on AI-assisted decision-making.")

st.text("Intro")

# pre-study questions

user_ID = st.text_area("What is your Prolific ID?")

age=st.radio(
    "What is your age?", ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
)

user_ID = st.text_area("What is your occupation?")

st.write("What types of AI do you have experience with?")
AI_use = st.checkbox("Chatbot AI (ChatGPT, Claude, Gemini, etc.)")
AI_use = st.checkbox("Image/video generation")
AI_use = st.checkbox("Conversational AI (Alexa, Siri, etc.)")
AI_use = st.checkbox("Others")

AI_frequency=st.radio(
    "How frequently do you use AI of any kind?", ["daily", "weekly", "monthly", "rarely", "not at all"]
)
if st.button("Submit"):
    # TODO: before posting study, change to get_articipant_num
    # st.session_state['PID']=get_participant_num()
    # for testing setting PID = 1
    st.session_state['PID']=1
    st.session_state["question_order"]=participants_order[st.session_state['PID']]
    st.switch_page("pages/questions.py")

