from interface_design import *

# if "question_order" not in st.session_state:
#     st.session_state["question_order"] = []


hide_sidebar(set_wide=True)

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
if "condition_questionnaire" not in st.session_state:
    st.session_state['condition_questionnaire'] = 0


# if st.session_state["question"]==5
#     st.switch_page("pages/C1_post_questions")

html_reminder = """
<div style='background-color: #ff6347; color: #f0f2f6; padding: 10px;'>
    <strong>Please do not refresh the web page.</strong> Otherwise, your previous answers will be lost.<br>
    If you clicked Confirm but the page isn’t responding, it’s likely because you haven’t made a selection yet.
</div>
"""

st.markdown(html_reminder, unsafe_allow_html=True)

if st.session_state['question'] <= 12:
    scenario_num = st.session_state['question_order'][st.session_state['question']]

condition_num = get_condition_num(st.session_state['PID'], st.session_state['question'])


if st.session_state["question"] == 5 and st.session_state['condition_questionnaire'] == 0:
    c_num = get_condition_num(st.session_state['PID'], st.session_state['question'] - 1)
    st.session_state['condition_questionnaire'] += 1
    if c_num == 1:
        st.switch_page("pages/C1_post_questions.py")
    if c_num == 2:
        st.switch_page("pages/C2_post_questions.py")
    if c_num == 3:
        st.switch_page("pages/C3_post_questions.py")   

if st.session_state["question"] == 9 and st.session_state['condition_questionnaire'] == 1:
    c_num = get_condition_num(st.session_state['PID'], st.session_state['question'] - 1)
    st.session_state['condition_questionnaire'] += 1
    if c_num == 1:
        st.switch_page("pages/C1_post_questions.py")
    if c_num == 2:
        st.switch_page("pages/C2_post_questions.py")
    if c_num == 3:
        st.switch_page("pages/C3_post_questions.py")  

if st.session_state["question"] == 13:
    c_num = get_condition_num(st.session_state['PID'], st.session_state['question'] - 1)
    st.session_state['condition_questionnaire'] += 1
    if c_num == 1:
        st.switch_page("pages/C1_post_questions.py")
    if c_num == 2:
        st.switch_page("pages/C2_post_questions.py")
    if c_num == 3:
        st.switch_page("pages/C3_post_questions.py")  

if condition_num == 1:
    condition1(str(scenario_num))
elif condition_num == 2:
    condition2(str(scenario_num))
else:
    condition3(str(scenario_num))

print("TEST", scenario_num)