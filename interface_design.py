import streamlit as st
from utils import *

if "expander_account" not in st.session_state:
    st.session_state["expander_count"]=0

data = read_data()
st.text_input(data['s1']['scenario'])

# with st.expander("deontology framework"):
#     st.write(load_explanation('s1', 'deontology'))
#     st.session_state["expander_count"]+=1
#     print(st.session_state["expander_count"])

with st.expander("utilitarianism framework"):
    st.write(load_explanation('s1', 'deontology'))

if st.button("deontology framework"):
    deontology_explanation = load_explanation('s1', 'deontology')
    st.write(deontology_explanation)
    st.session_state["expander_count"]=st.session_state["expander_count"]+1
    print(st.session_state["expander_count"])

if st.button("utilitarianism framework"):
    uti_explanation = load_explanation('s1', 'utilitarianism')
    st.text(uti_explanation)

if st.button("care ethics framework"):
    care_explanation = load_explanation('s1', 'care ethics')
    st.text(care_explanation)


st.image("S1_Image1.png", caption="Option 1: Tell the patient about their condition")
st.image("S1_Image2.png", caption="Option 2: Do not tell the patient about their condition")

harm = st.select_slider (
    "use the slider to visualize the harm created if option 1 is chosen",
    options=[
        "no harm",
        "minimal harm",
        "some harm",
        "significant harm",
        "very significant harm",
    ]
)

harm = st.select_slider (
    "use the slider to visualize the harm created if option 2 is chosen",
    options=[
        "no harm",
        "minimal harm",
        "some harm",
        "significant harm",
        "very significant harm",
    ]
)

harm = st.select_slider (
    "use the slider to visualize the harm created if option 3 is chosen",
    options=[
        "no harm",
        "minimal harm",
        "some harm",
        "significant harm",
        "very significant harm",
    ]
)