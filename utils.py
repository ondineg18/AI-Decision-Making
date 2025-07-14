import json
import requests
import streamlit as st
from constant import *
import dropbox

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
    with open('AI_output/condition1/dummy.json', 'r') as file:
        data = json.load(file)

    return data

def load_explanation(scenario_num, framework):
    file_path = "AI_output" + "/condition1/dummy.json"
    with open('AI_output/condition1/dummy.json', 'r') as file:
        data = json.load(file)

    return data[scenario_num][framework]

def get_participant_num():
    response = requests.get("http://128.111.28.83:8000/next_participant")
    participant_id = response.json()["participant_number"]
    return participant_id

def get_condition_num(pid, question):
    block_id = (question - 1) // 4
    return participants_condition_order[pid][block_id - 1]

def upload_file_to_dropbox(file_path, dropbox_path):
    app_key = st.secrets["dropbox"]["app_key"]
    app_secret = st.secrets["dropbox"]["app_secret"]
    refresh_token = st.secrets["dropbox"]["refresh_token"]
    try:
        dbx = dropbox.Dropbox(
            oauth2_refresh_token=refresh_token,
            app_key=app_key,
            app_secret=app_secret
        )
        
        with open(file_path, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    except Exception as e:
        print("Error during file upload:", e)