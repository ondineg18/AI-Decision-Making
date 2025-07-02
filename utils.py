import json

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