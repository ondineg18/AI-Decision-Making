import json
import requests
import streamlit as st
def hide_sidebar(set_wide=False):
    if set_wide:
        st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
    else:
        st.set_page_config(initial_sidebar_state="collapsed")
    no_sidebar_style="""
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        """

def read_data():
    file_path = "AI_output" + "/dummy.json"
    with open('/Users/26goedhuiso/Documents/AI-Decision-Making/AI_output/condition1/dummy.json', 'r') as file:
        data = json.load(file)

    return data

def load_explanation(scenario_num, framework):
    file_path = "AI_output" + "/condition1/dummy.json"
    with open('/Users/26goedhuiso/Documents/AI-Decision-Making/AI_output/condition1/dummy.json', 'r') as file:
        data = json.load(file)

    return data[scenario_num][framework]

def get_participant_num():
    response = requests.get("http://128.111.28.83:8000/next_participant")
    participant_id = response.json()["participant_number"]
    return participant_id