import streamlit as st
import json
from utils import *
hide_sidebar()

st.write("## Post-Study Questions")

first_question=st.radio(
    "After seeing AI’s suggestion (and before seeing any explanation, image, or interactive features), how inclined were you to accept AI’s suggestion at the expense of your own?",
    options=["not inclined", "somewhat inclined", "quite inclined", "very inclined"],
    key="first_question",
    index=None
)

second_question=st.radio(
    "After reading the ethical framework explanations, how inclined were you to accept AI’s suggestion at the expense of your own?",
    options=["not inclined", "somewhat inclined", "quite inclined", "very inclined"],
    key="second_question",
    index=None
)

third_question=st.radio(
    "After seeing the images, how inclined were you to accept AI’s suggestion at the expense of your own?",
    options=["not inclined", "somewhat inclined", "quite inclined", "very inclined"],
    key="third_question",
    index=None
)

fourth_question=st.radio(
    "After using the interactive features, how inclined were you to accept AI’s suggestion at the expense of your own?",
    options=["not inclined", "somewhat inclined", "quite inclined", "very inclined"],
    key="fourth_question",
    index=None
)

# st.write("The following set of questions pertains to the ethical framework explanations you were shown")

# likely=st.slider("The explanations encouraged me to think critically about my decisions", 1, 7)
# likely=st.slider("I considered multiple perspectives before making my decisions", 1, 7)
# likely=st.slider("The explanations made the dilemmas feel more real or emotionally engaging", 1, 7)
# likely=st.slider("I reflected on my own values when making my decisions", 1, 7)
# likely=st.slider("The explanations changed the way I viewed the dilemmas", 1, 7)
# likely=st.slider("The explanations helped me determine what I individually think", 1, 7)
# likely=st.slider("I felt more confident in the decisions I made after viewing the explanations", 1, 7)

# st.write("The following set of questions pertains to the ethical framework explanations you were shown")

# likely=st.slider("The explanations encouraged me to think critically about my decisions", 1, 7)
# likely=st.slider("I considered multiple perspectives before making my decisions", 1, 7)
# likely=st.slider("The explanations made the dilemmas feel more real or emotionally engaging", 1, 7)
# likely=st.slider("I reflected on my own values when making my decisions", 1, 7)
# likely=st.slider("The explanations changed the way I viewed the dilemmas", 1, 7)
# likely=st.slider("The explanations helped me determine what I individually think", 1, 7)
# likely=st.slider("I felt more confident in the decisions I made after reading the explanations", 1, 7)

# st.write("The following set of questions pertains to the images you were shown")

# likely=st.slider("The images encouraged me to think critically about my decisions", 1, 7)
# likely=st.slider("I considered multiple perspectives before making my decisions", 1, 7)
# likely=st.slider("The images made the dilemmas feel more real or emotionally engaging", 1, 7)
# likely=st.slider("I reflected on my own values when making my decisions", 1, 7)
# likely=st.slider("The images changed the way I viewed the dilemmas", 1, 7)
# likely=st.slider("The images helped me determine what I individually think", 1, 7)
# likely=st.slider("I felt more confident in the decisions I made after viewing the images", 1, 7)

# st.write("The following set of questions pertains to the interactive features you explored")

# likely=st.slider("The interactive features encouraged me to think critically about my decisions", 1, 7)
# likely=st.slider("I considered multiple perspectives before making my decisions", 1, 7)
# likely=st.slider("The interactive features made the dilemmas feel more real or emotionally engaging", 1, 7)
# likely=st.slider("I reflected on my own values when making my decisions", 1, 7)
# likely=st.slider("The interactive features changed the way I viewed the dilemmas", 1, 7)
# likely=st.slider("The interactive features helped me determine what I individually think", 1, 7)
# likely=st.slider("I felt more confident in the decisions I made after using the interactive features", 1, 7)

fifth_question=st.radio(
    "Which decision-support aid most influenced you to reconsider or disagree with AI’s suggestions after exploring it?",
    options=["explanations", "images", "interactive features"],
    key="fifth_question",
    index=None
)

sixth_question=st.radio(
    "Which decision-support aid was the next most inflential in leading you to reconsider or disagree with AI's suggestions?",
    options=["explanations", "images", "interactive features"],
    key="sixth_question",
    index=None
)

attention_question=st.radio(
    "Please select images for this question. This is an attention-check question.",
    options=["explanations", "images", "interactive features"],
    key="attention_question",
    index=None
)

seventh_question=st.radio(
    "Which decision-support aid most encouraged you to think for yourself beyond AI’s suggestions?",
    options=["explanations", "images", "interactive features"],
    key="seventh_question",
    index=None
)

eighth_question=st.radio(
    "Which decision-support aid was the next most influential in encouraging you to think for yourself beyond AI’s suggestions?",
    options=["explanations", "images", "interactive features"],
    key="eighth_question",
    index=None
)

ninth_question=st.radio(
    "Which decision-support aid did you enjoy using the most?",
    options=["explanations", "images", "interactive features"],
    key="ninth_question",
    index=None
)

tenth_question=st.radio(
    "Which decision-support aid did you enjoy using the least?",
    options=["explanations", "images", "interactive features"],
    key="tenth_question",
    index=None
)

post_questions = [first_question, second_question, third_question, fourth_question, fifth_question, sixth_question, seventh_question, eighth_question, ninth_question, tenth_question, attention_question]
if st.button('Confirm') and None not in post_questions:
    save_path = st.session_state['id'] +'.jsonl'

    data_to_save = {
        "user_answer": st.session_state.get("user_answer"),
        "actions": st.session_state.get("actions"),
        "pre_questions": st.session_state.get("pre_questions"),
        "C1_questions": st.session_state.get("C1_questions"),
        "C2_questions": st.session_state.get("C2_questions"),
        "C3_questions": st.session_state.get("C3_questions"),
        "post_quesitons": post_questions,
        "PID": st.session_state.get("PID"),
        "id": st.session_state.get("id"),
        "question_order": st.session_state.get("question_order"),
    }

    with open (save_path, 'w') as file:
        print("TEST 200", st.session_state['C2_questions'])
        json_line = json.dumps(data_to_save)
        file.write(json_line +'\n')

    save_path = st.session_state['id'] +'.jsonl'
    dropbox_save_path = '/results-ethical/' + st.session_state['id'] + '.jsonl'
    upload_file_to_dropbox(save_path, dropbox_path = dropbox_save_path)
    st.switch_page("pages/final_page.py")
    