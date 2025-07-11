from interface_design import *

if "question_order" not in st.session_state:
    st.session_state["question_order"] = []

scenario_mapping = {
    1: 'condition1',
    2: "condition3",
    3: "condition3",
    4: "condition3",
    5: "condition3",
    6: "condition3",
    7: 'condition1',
    8: 'condition1',
    9: 'condition1',
    10: 'condition1',
    11: "condition3",
    12: "condition3",

}

st.write(st.session_state['question_order'])

# st.set_page_config(layout="wide")

if "click_sequence" not in st.session_state:
    st.session_state["click_sequence"]=[]
if "state" not in st.session_state:
    st.session_state["state"] = 0
if "scenario" not in st.session_state:
    st.session_state['scenario']=1
if "user_answer" not in st.session_state:
    st.session_state['user_answer']={}
if "question" not in st.session_state:
    st.session_state["question"]=1

if st.session_state["question"] == 13:
    st.switch_page("pages/post_study_questions.py")

# if st.session_state["question"]==5
#     st.switch_page("pages/C1_post_questions")

scenario_num = st.session_state['question_order'][st.session_state['question']]

condition_num = get_condition_num(st.session_state['PID'], st.session_state['question'])

if condition_num == 'condition1':
    condition1(str(scenario_num))
elif condition_num == 'condition2':
    condition2(str(scenario_num))
else:
    condition3(str(scenario_num))