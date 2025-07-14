import streamlit as st
from datetime import datetime
from utils import *
from constant import *

st.set_page_config(layout="wide")

# if "click_sequence" not in st.session_state:
#     st.session_state["click_sequence"]=[]
# if "state" not in st.session_state:
#     st.session_state["state"] = 0
# if "scenario" not in st.session_state:
#     st.session_state['question']=1
# if "user_answer" not in st.session_state:
#     st.session_state['user_answer']={}

# actions[scenario]=[[action_name, time, choice],[],[], ...]

def condition1(scenario):
    data = read_data()
    st.title(data[scenario]['scenario'])
    st.write("## Make your decision")
    option_1 = data[scenario]['option_1']
    option_2 = data[scenario]['option_2'] 

    if question_type_mapping[scenario]=="multiple_choice":

        first_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"first_choice", index=None)
        st.session_state['first_choice'] = True if first_choice is not None else False

    if question_type_mapping[scenario]=="slider":
        option_3 = data[scenario]['option_3']
        if scenario in scenario_is_donation: 
            likert_max = 10000
            st.write("*Please make sure the sum of your three choices is less than 10000*")
        else:
            likert_max = 7
        first_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"first_choice_1")
        first_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"first_choice_2")
        first_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"first_choice_3")
        st.session_state['first_choice'] = True
    if st.button("confirm", key="first_button") and st.session_state['first_choice'] == True:
        answer=None
        if question_type_mapping[scenario]=="multiple_choice":
            answer = first_choice
        else:
            answer = [first_choice_1, first_choice_2, first_choice_3]
        st.session_state['state']+=1
        st.session_state['user_answer'][scenario + "first_choice"] = [str(datetime.now()), answer]

    if st.session_state["state"]>0:
        AI_suggestion = load_explanation(scenario, "AI-suggestions")
        st.write("## AI Suggestion")
        AI_suggestion = AI_suggestion.replace("$", "\\$")
        st.write(AI_suggestion)

        st.write("## Update or maintain your decision")
       
        if question_type_mapping[scenario]=="multiple_choice":

            second_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"second_choice", index=None)

            st.session_state['second_choice'] = True if second_choice is not None else False

        if question_type_mapping[scenario]=="slider":
            option_3 = data[scenario]['option_3']
            if scenario in scenario_is_donation: 
                likert_max = 10000
                st.write("*Please make sure the sum of your three choices is less than 10000*")
            else:
                likert_max = 7
            second_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"second_choice_1")
            second_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"second_choice_2")
            second_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"second_choice_3")
            st.session_state['second_choice'] = True

        if st.button("confirm", key="second_button") and st.session_state['second_choice'] == True:
            if question_type_mapping[scenario]=="multiple_choice":
                answer = second_choice
            else:
                answer = [second_choice_1, second_choice_2, second_choice_3]
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "first_choice"] = [str(datetime.now()), answer]

    if st.session_state["state"]>1:
        st.write("## Click to explore decision choices based on different ethical frameworks")
        
        if st.button("deontology framework"):
            deontology_explanation = load_explanation(scenario, 'deontology')
            st.write(deontology_explanation)
            st.session_state["click_sequence"].append([str(datetime.now()), "deontology"])

        if st.button("utilitarianism framework"):
            uti_explanation = load_explanation(scenario, 'utilitarianism')
            st.write(uti_explanation)
            st.session_state["click_sequence"].append([str(datetime.now()), "utilitarianism"])
        
        if st.button("virtue ethics framework"):
            virtue_explanation = load_explanation(scenario, 'virtue ethics')
            st.write(virtue_explanation)
            st.session_state["click_sequence"].append([str(datetime.now()), "virtue ethics"])

        if st.button("care ethics framework"):
            care_explanation = load_explanation(scenario, 'care ethics')
            st.write(care_explanation)
            st.session_state["click_sequence"].append([str(datetime.now()), "care ethics"])

        st.write("## Update or maintain your decision")
        
        if question_type_mapping[scenario]=="multiple_choice":

            third_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"third_choice", index=None)

            st.session_state['third_choice'] = True if third_choice is not None else False

        if question_type_mapping[scenario]=="slider":
            option_3 = data[scenario]['option_3']
            if scenario in scenario_is_donation: 
                likert_max = 10000
                st.write("*Please make sure the sum of your three choices is less than 10000*")
            else:
                likert_max = 7
            third_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"third_choice_1")
            third_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"third_choice_2")
            third_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"third_choice_3")

            st.session_state['third_choice'] = True

        if st.button("confirm", key="third_button") and st.session_state['third_choice'] == True:
            if question_type_mapping[scenario]=="multiple_choice":
                answer = third_choice
            else:
                answer = [third_choice_1, third_choice_2, third_choice_3]
            
            st.session_state['actions'][scenario+'c1_click_hist'] = st.session_state["click_sequence"]
            st.session_state["click_sequence"] = []
            st.session_state['state']+=1
            st.session_state['first_choice'] = False
            st.session_state['second_choice'] = False
            st.session_state['third_choice'] = False
            st.session_state['user_answer'][scenario + "third_choice" + "C1"] = [str(datetime.now()), answer]

    if st.session_state["state"]>2:
        if st.button("continue"):
            st.session_state["state"]=0
            st.session_state["question"]+=1
            st.rerun()


# IMAGE CONDITION2

def condition2(scenario):
    data = read_data()
    st.title(data[scenario]['scenario'])
    st.write("## Make your decision")
    option_1 = data[scenario]['option_1']
    option_2 = data[scenario]['option_2']
    image_1 = data[scenario]['image_1']
    image_2 = data[scenario]['image_2']
    
    if question_type_mapping[scenario]=="multiple_choice":

        first_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"first_choice", index=None)
        st.session_state['first_choice'] = True if first_choice is not None else False

    else:
        option_3 = data[scenario]['option_3']
        image_3 = data[scenario]['image_3']
        if scenario in scenario_is_donation: 
            likert_max = 10000
            st.write("*Please make sure the sum of your three choices is less than 10000*")
        else:
            likert_max = 7
        first_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"first_choice_1")
        first_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"first_choice_2")
        first_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"first_choice_3")
        st.session_state['first_choice'] = True

    if st.button("confirm", key="first_button") and st.session_state['first_choice']:
        if question_type_mapping[scenario]=="multiple_choice":
            answer = first_choice
        else:
            answer = [first_choice_1, first_choice_2, first_choice_3]
        st.session_state['state']+=1
        st.session_state['user_answer'][scenario + "first_choice" + "C2"] = [str(datetime.now()), answer]

    if st.session_state["state"]>0:
        AI_suggestion = load_explanation(scenario, "AI-suggestions")
        st.write("## AI Suggestion")
        AI_suggestion = AI_suggestion.replace("$", "\\$")
        st.write(AI_suggestion)

        st.write("## Update or maintain your decision")
        
        if question_type_mapping[scenario]=="multiple_choice":

            second_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"second_choice", index=None)
            st.session_state['second_choice'] = True if second_choice is not None else False

        else:
            option_3 = data[scenario]['option_3']
            if scenario in scenario_is_donation: 
                likert_max = 10000
                st.write("*Please make sure the sum of your three choices is less than 10000*")
            else:
                likert_max = 7
            second_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"second_choice_1")
            second_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"second_choice_2")
            second_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"second_choice_3")
            st.session_state['second_choice'] = True
        
        if st.button("confirm", key="second_button") and st.session_state['second_choice'] == True:
            if question_type_mapping[scenario]=="multiple_choice":
                answer = second_choice
            else:
                answer = [second_choice_1, second_choice_2, second_choice_3]
            now = datetime.now()
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "second_choice" + "C2"] = [str(datetime.now()), answer]


    if st.session_state["state"]>1:
        
        if question_type_mapping[scenario]=="multiple_choice":
            col1, col2 = st.columns(2)

            with col1:  
                st.header(option_1)
                st.image(image_1)
            with col2:
                st.header(option_2)
                st.image(image_2)
        else:
            col1, col2, col3 = st.columns(3)

            with col1:  
                st.header(option_1)
                st.image(image_1)
            with col2:
                st.header(option_2)
                st.image(image_2)
            with col3:
                st.header(option_3)
                st.image(image_3)
        st.write("## Update or maintain your decision")
        
        if question_type_mapping[scenario]=="multiple_choice":

            third_choice=st.radio(
                "",
                options=[option_1, option_2], key=scenario+"_"+"third_choice", index=None)
            st.session_state['third_choice'] = True if third_choice is not None else False

        else:
            option_3 = data[scenario]['option_3']
            if scenario in scenario_is_donation: 
                likert_max = 10000
                st.write("*Please make sure the sum of your three choices is less than 10000*")
            else:
                likert_max = 7
            third_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"third_choice_1")
            third_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"third_choice_2")
            third_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"third_choice_3")
            st.session_state['third_choice'] = True

        if st.button("confirm", key="third_button") and st.session_state['third_choice'] == True:
            if question_type_mapping[scenario]=="multiple_choice":
                answer = third_choice
            else:
                answer = [third_choice_1, third_choice_2, third_choice_3]
            st.session_state['state']+=1
            st.session_state['first_choice'] = False
            st.session_state['second_choice'] = False
            st.session_state['third_choice'] = False
            st.session_state['user_answer'][scenario + "third_choice" + "C2"] = [str(datetime.now()), answer]

    if st.session_state["state"]>2:
        if st.button("continue"):
            st.session_state["state"]=0
            st.session_state["question"]+=1
            st.rerun()


# INTERACTIVE CONDITION 3

def condition3(scenario):
    data = read_data()
    st.title(data[scenario]['scenario'])
    st.write("## Make your decision")
    option_1 = data[scenario]['option_1']
    option_2 = data[scenario]['option_2'] 

    if question_type_mapping[scenario]=="multiple_choice":

        first_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"first_choice", index=None)
        st.session_state['first_choice'] = True if first_choice is not None else False

    else:
        option_3 = data[scenario]['option_3']
        if scenario in scenario_is_donation: 
            likert_max = 10000
            st.write("*Please make sure the sum of your three choices is less than 10000*")
        else:
            likert_max = 7
        first_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"first_choice_1")
        first_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"first_choice_2")
        first_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"first_choice_3")
        st.session_state['first_choice'] = True

    if st.button("confirm", key="first_button") and st.session_state['first_choice'] == True:
        if question_type_mapping[scenario]=="multiple_choice":
            answer = first_choice
        else:
            answer = [first_choice_1, first_choice_2, first_choice_3]
        st.session_state['state']+=1
        st.session_state['user_answer'][scenario + "first_choice" + "C3"] = [str(datetime.now()), answer]

    if st.session_state["state"]>0:
        AI_suggestion = load_explanation(scenario, "AI-suggestions")
        st.write("## AI Suggestion")
        AI_suggestion = AI_suggestion.replace("$", "\\$")
        st.write(AI_suggestion)

        st.write("## Update or maintain your decision")
       
        if question_type_mapping[scenario]=="multiple_choice":

            second_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"second_choice", index=None)
            st.session_state['second_choice'] = True if second_choice is not None else False

        else:
            option_3 = data[scenario]['option_3']
            if scenario in scenario_is_donation: 
                likert_max = 10000
                st.write("*Please make sure the sum of your three choices is less than 10000*")
            else:
                likert_max = 7
            second_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"second_choice_1")
            second_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"second_choice_2")
            second_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"second_choice_3")
            st.session_state['second_choice'] = True
        
        if st.button("confirm", key="second_button") and st.session_state['second_choice'] == True:
            if question_type_mapping[scenario]=="multiple_choice":
                answer = second_choice
            else:
                answer = [second_choice_1, second_choice_2, second_choice_3]
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "second_choice" + "C3"] = [str(datetime.now()), answer]

    if st.session_state["state"]>1:
        st.write("## Pick an ethical framework to explore with an interactive tool")
        
        with st.expander("utilitarianism") as expander_util:
            if expander_util:
                st.session_state["click_sequence"].append([str(datetime.now()), 'utilitarianism'])
            harm_1 = st.select_slider (
                data[scenario]['slider_caption_1'], 
                options=data[scenario]['slider_options_1'] 
                
            )

            harm_2 = st.select_slider (
                data[scenario]['slider_caption_2'],
                options=data[scenario]['slider_options_2']
            )
            
            st.session_state['actions'][scenario+'util'+"C3"] = [harm_1, harm_2]
            if question_type_mapping[scenario]=="slider":

                harm_3 = st.select_slider (
                    data[scenario]['slider_caption_3'],
                    options=data[scenario]['slider_options_3']
                )
                st.session_state['actions'][scenario+'util'+"C3"] = [harm_1, harm_2, harm_3]
        with st.expander("deontology") as expander_deon:
            if expander_deon:
                st.session_state["click_sequence"].append([str(datetime.now()), 'deontology'])
            # st.write("Select personal values/moral duties you live by")
            values = st.multiselect(
                "Select personal values/moral duties that are important to you:",
                ["Justice", "Honesty", "Responsibility", "Compassion", "Selflessness", "Loyalty", "Empathy", "Accountability"]
            )

            st.session_state['actions'][scenario+'deontology'+"C3"] = values

        with st.expander("virtue ethics") as expander_virtue:
            if expander_virtue:
                st.session_state["click_sequence"].append([str(datetime.now()), 'virtue ethics'])
            st.write("Think about your role model, or the most virtuous person you know. What would they do? Why?")
            user_input = st.text_area("Reflect here:")
            
            st.session_state['actions'][scenario+'virtue ethics'+"C3"] = user_input

        with st.expander("care ethics") as expander_care:
            if expander_care:
                st.session_state["click_sequence"].append([str(datetime.now()), 'care ethics'])
            emotions_1 = st.multiselect(
                "If option 1 is chosen, who is affected the most emotionally? How will they feel?",
                ["sad", "happy", "angry", "relieved", "scared", "loved", "guilty", "hopeful", "stressed",]
            )

            emotions_2 = st.multiselect(
                "If option 2 is chosen, who is affected the most emotionally? How will they feel?",
                ["sad", "happy", "angry", "relieved", "scared", "loved", "guilty", "hopeful", "stressed",]
            )
            
            st.session_state['actions'][scenario+'util'+"C3"] = [emotions_1, emotions_2]
            if question_type_mapping[scenario]=="slider":
                        
                emotions_3 = st.multiselect(
                    "If option 3 is chosen, who is affected the most emotionally? How will they feel?",
                    ["sad", "happy", "angry", "relieved", "scared", "loved", "guilty", "hopeful", "stressed",]
                )
                st.session_state['actions'][scenario+'util'+"C3"] = [emotions_1, emotions_2, emotions_3]

        st.write("## Update or maintain your decision")  
        
        if question_type_mapping[scenario]=="multiple_choice":

            third_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"third_choice", index=None)
            st.session_state['third_choice'] = True if third_choice is not None else False

        else:
            option_3 = data[scenario]['option_3']
            if scenario in scenario_is_donation: 
                likert_max = 10000
                st.write("*Please make sure the sum of your three choices is less than 10000*")
            else:
                likert_max = 7
            third_choice_1 = st.slider(option_1, 1, likert_max, 1, key=scenario+"_"+"third_choice_1")
            third_choice_2 = st.slider(option_2, 1, likert_max, 1, key=scenario+"_"+"third_choice_2")
            third_choice_3 = st.slider(option_3, 1, likert_max, 1, key=scenario+"_"+"third_choice_3")
            st.session_state['third_choice'] = True
     
        if st.button("confirm", key="third_button") and st.session_state['third_choice'] == True:
            if question_type_mapping[scenario]=="multiple_choice":
                answer = third_choice
            else:
                answer = [third_choice_1, third_choice_2, third_choice_3]
            st.session_state['state']+=1
            st.session_state['first_choice'] = False
            st.session_state['second_choice'] = False
            st.session_state['third_choice'] = False
            st.session_state['user_answer'][scenario + "third_choice" + "C3"] = [str(datetime.now()), answer]


    if st.session_state["state"]>2:
        if st.button("continue"):
            st.session_state["state"]=0
            st.session_state["question"]+=1
            st.rerun()

if __name__== '__main__':
    condition3(str(st.session_state["question"]))