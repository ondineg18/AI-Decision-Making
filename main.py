import streamlit as st
from utils import *
from constant import *
# from analysis import analyze_user_data

hide_sidebar()

if "PID" not in st.session_state:
    st.session_state['PID'] = -1
if "pre_questions" not in st.session_state:
    st.session_state['pre_questions'] = {}
if "user_answer" not in st.session_state:
    st.session_state['user_answer']={}
if "actions" not in st.session_state:
    st.session_state['actions'] = {}

st.title("Welcome to our study on AI-assisted decision-making.")

intro = '''
Your participation will help us understand how different forms of AI decision support mechanisms influence human decision-making on ethical dilemmas.

You will first answer some pre-study questions; then, you will be asked to make decisions on 12 fictional ethical scenarios. In each scenario, the AI will present decision support in one of the following forms:

AI-generated explanations of a suggested decision based on different ethical frameworks
AI generated images depicting the potential aftermath of different choices
Interactive user interface elements, such as sliders and checkboxes, designed to encourage reflection on decisions

After every 4 scenarios, you will be asked to answer a few questions about the AI support mechanisms provided in those scenarios. After completing all 12 scenarios, you will be asked to answer some post-study questions, which then leads to the conclusion of the study.
"'''


st.write(intro)
st.write(":red[Please do not refresh the browser during the study, otherwise your data will be lost.]")
st.divider()

# pre-study questions

user_ID = st.text_area("What is your Prolific ID?")

age=st.radio(
    "What is your age?", ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    index=None
)

user_occupation = st.text_area("What is your occupation?")

st.write("What types of AI do you have experience with?")
AI_use_chat = st.checkbox("Chatbot AI (ChatGPT, Claude, Gemini, etc.)")
AI_use_image = st.checkbox("Image/video generation")
AI_use_conversation = st.checkbox("Conversational AI (Alexa, Siri, etc.)")
AI_use_others = st.checkbox("Others")
AI_use_none = st.checkbox("None")

AI_frequency=st.radio(
    "How frequently do you use AI of any kind?", ["daily", "weekly", "monthly", "rarely", "not at all"],
    index=None
)
if st.button("Submit"):
    # TODO: before posting study, change to get_articipant_num
    # st.session_state['PID']=get_participant_num()
    # for testing setting PID = 1
    user_checkbox = [AI_use_chat, AI_use_image, AI_use_conversation, AI_use_others, AI_use_none]
    user_choices = [user_ID, age, AI_frequency, user_occupation]
    if "" in user_choices or (user_checkbox.count(False) >= 5):
        st.write(":red[Please fill in all fields]")
    else:
        # st.session_state['PID']=1
        st.session_state['PID']=get_participant_num()
        if st.session_state['PID'] == 0: st.session_state['PID'] = 1
        st.session_state["question_order"]=participants_order[st.session_state['PID']]
        st.session_state['pre_questions']['user_choices'] = user_choices
        st.session_state['pre_questions']['user_checkbox'] = user_checkbox
        st.session_state['id'] = user_ID
        st.switch_page("pages/questions.py")

