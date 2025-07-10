from interface_design import *

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

st.set_page_config(layout="wide")

if "click_sequence" not in st.session_state:
    st.session_state["click_sequence"]=[]
if "state" not in st.session_state:
    st.session_state["state"] = 0
if "scenario" not in st.session_state:
    st.session_state['scenario']=1
if "user_answer" not in st.session_state:
    st.session_state['user_answer']={}

if st.session_state["scenario"] == 13:
    st.switch_page("pages/post_study_questions.py")

if scenario_mapping[st.session_state['scenario']] == 'condition1':
    condition1(str(st.session_state["scenario"]))
elif scenario_mapping[st.session_state['scenario']] == 'condition2':
    condition2(str(st.session_state["scenario"]))
else:
    condition3(str(st.session_state["scenario"]))