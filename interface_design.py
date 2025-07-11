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

def condition1(scenario):
    data = read_data()
    st.title(data[scenario]['scenario'])
    st.write("## Make your decision")
    option_1 = data[scenario]['option_1']
    option_2 = data[scenario]['option_2'] 

    if question_type_mapping[scenario]=="multiple_choice":

        first_choice=st.radio(
            "",
            options=[option_1, option_2], key="first_choice")

    if question_type_mapping[scenario]=="slider":
        option_3 = data[scenario]['option_3']
        first_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"first_choice_1")
        first_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"first_choice_2")
        first_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"first_choice_3")

    if st.button("confirm"):
        answer=None
        if question_type_mapping[scenario]=="multiple_choice":
            answer = first_choice
        else:
            answer = [first_choice_1, first_choice_2, first_choice_3]
        st.session_state['state']+=1
        st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

    if st.session_state["state"]>0:
        AI_suggestion = load_explanation(scenario, "AI-suggestions")
        st.write("## AI Suggestion")
        st.write(AI_suggestion)

        st.write("## Update or maintain your decision")
       
        if question_type_mapping[scenario]=="multiple_choice":

            second_choice=st.radio(
            "",
            options=[option_1, option_2], key="second_choice")

        if question_type_mapping[scenario]=="slider":
            option_3 = data[scenario]['option_3']
            second_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"second_choice_1")
            second_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"second_choice_2")
            second_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"second_choice_3")
        
        if st.button("confirm", key="second_button"):
            if question_type_mapping[scenario]=="multiple_choice":
                answer = first_choice
            else:
                answer = [first_choice_1, first_choice_2, first_choice_3]
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

    if st.session_state["state"]>1:
        st.write("## Click to explore decision choices based on different ethical frameworks")
        
        if st.button("deontology framework"):
            deontology_explanation = load_explanation(scenario, 'deontology')
            st.write(deontology_explanation)
            st.session_state["click_sequence"].append("deontology")
            print(st.session_state["click_sequence"])

        if st.button("utilitarianism framework"):
            uti_explanation = load_explanation(scenario, 'utilitarianism')
            st.write(uti_explanation)
            st.session_state["click_sequence"].append("utilitarianism")
            print(st.session_state["click_sequence"])
        
        if st.button("virtue ethics framework"):
            virtue_explanation = load_explanation(scenario, 'virtue ethics')
            st.write(virtue_explanation)
            st.session_state["click_sequence"].append("virtue ethics")
            print(st.session_state["click_sequence"])

        if st.button("care ethics framework"):
            care_explanation = load_explanation(scenario, 'care ethics')
            st.write(care_explanation)
            st.session_state["click_sequence"].append("care ethics")
            print(st.session_state["click_sequence"])

        st.write("## Update or maintain your decision")  
        
        if question_type_mapping[scenario]=="multiple_choice":

            third_choice=st.radio(
            "",
            options=[option_1, option_2], key="third_choice")

        if question_type_mapping[scenario]=="slider":
            option_3 = data[scenario]['option_3']
            third_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"third_choice_1")
            third_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"third_choice_2")
            third_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"third_choice_3")
     
        if st.button("confirm", key="third_button"):
            if question_type_mapping[scenario]=="multiple_choice":
                answer = first_choice
            else:
                answer = [first_choice_1, first_choice_2, first_choice_3]
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

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
    
    print(question_type_mapping[scenario])
    print(question_type_mapping[scenario]=="multiple_choice")
    if question_type_mapping[scenario]=="multiple_choice":


        first_choice=st.radio(
            "",
            options=[option_1, option_2], key=scenario+"_"+"first_choice")

    else:
        print(question_type_mapping[scenario])
        option_3 = data[scenario]['option_3']
        first_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"first_choice_1")
        first_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"first_choice_2")
        first_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"first_choice_3")

    if st.button("confirm"):
        if question_type_mapping[scenario]=="multiple_choice":
            answer = first_choice
        else:
            answer = [first_choice_1, first_choice_2, first_choice_3]
        now = datetime.now()
        st.session_state['state']+=1
        st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

    if st.session_state["state"]>0:
        AI_suggestion = load_explanation(scenario, "AI-suggestions")
        st.write("## AI Suggestion")
        st.write(AI_suggestion)

        st.write("## Update or maintain your decision")
        
        if question_type_mapping[scenario]=="multiple_choice":

            second_choice=st.radio(
            "",
            options=[option_1, option_2], key="second_choice")

        else:
            option_3 = data[scenario]['option_3']
            second_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"second_choice_1")
            second_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"second_choice_2")
            second_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"second_choice_3")
        
        if st.button("confirm", key="second_button"):
            if question_type_mapping[scenario]=="multiple_choice":
                answer = first_choice
            else:
                answer = [first_choice_1, first_choice_2, first_choice_3]
            now = datetime.now()
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer


    if st.session_state["state"]>1:
               
        col1, col2 = st.columns(2)

        with col1:  
            st.header(option_1)
            st.image(image_1)
        with col2:
            st.header(option_2)
            st.image(image_2)

        st.write("## Update or maintain your decision")
        
        if question_type_mapping[scenario]=="multiple_choice":

            third_choice=st.radio(
                "",
                options=[option_1, option_2], key="third_choice")

        else:
            option_3 = data[scenario]['option_3']
            third_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"third_choice_1")
            third_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"third_choice_2")
            third_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"third_choice_3")

        if st.button("confirm", key="third_button"):
            if question_type_mapping[scenario]=="multiple_choice":
                answer = first_choice
            else:
                answer = [first_choice_1, first_choice_2, first_choice_3]
            now = datetime.now()
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

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
            options=[option_1, option_2], key="first_choice")

    else:
        option_3 = data[scenario]['option_3']
        first_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"first_choice_1")
        first_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"first_choice_2")
        first_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"first_choice_3")

    if st.button("confirm"):
        if question_type_mapping[scenario]=="multiple_choice":
            answer = first_choice
        else:
            answer = [first_choice_1, first_choice_2, first_choice_3]
        st.session_state['state']+=1
        st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

    if st.session_state["state"]>0:
        AI_suggestion = load_explanation(scenario, "AI-suggestions")
        st.write("## AI Suggestion")
        st.write(AI_suggestion)

        st.write("## Update or maintain your decision")
       
        if question_type_mapping[scenario]=="multiple_choice":

            second_choice=st.radio(
            "",
            options=[option_1, option_2], key="second_choice")

        else:
            option_3 = data[scenario]['option_3']
            second_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"second_choice_1")
            second_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"second_choice_2")
            second_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"second_choice_3")
        
        if st.button("confirm", key="second_button"):
            if question_type_mapping[scenario]=="multiple_choice":
                answer = first_choice
            else:
                answer = [first_choice_1, first_choice_2, first_choice_3]
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

    if st.session_state["state"]>1:
        st.write("Pick an ethical framework to explore with an interactive tool")
        
        with st.expander("utilitarianism"):

            harm = st.select_slider (
                data[scenario]['slider_caption_1'], 
                options=data[scenario]['slider_options_1'] 
                
            )

            harm = st.select_slider (
                data[scenario]['slider_caption_2'],
                options=data[scenario]['slider_options_2']
            )

            if question_type_mapping[scenario]=="slider":

                harm = st.select_slider (
                    data[scenario]['slider_caption_3'],
                    options=data[scenario]['slider_options_3']
                )
        with st.expander("deontology"):
            # st.write("Select personal values/moral duties you live by")
            values = st.multiselect(
                "Select personal values/moral duties that are important to you:",
                ["Justice", "Honesty", "Responsibility", "Compassion", "Selflessness", "Loyalty", "Empathy", "Accountability"]
            )

        with st.expander("virtue ethics"):
            st.write("Think about your role model, or the most virtuous person you know. What would they do? Why?")
            user_input = st.text_area("Reflect here:")

        with st.expander("care ethics"):
            emotions_1 = st.multiselect(
                "If option 1 is chosen, who is affected the most emotionally? How will they feel?",
                ["sad", "happy", "angry", "relieved", "scared", "loved", "guilty", "hopeful", "stressed",]
            )

            emotions_2 = st.multiselect(
                "If option 2 is chosen, who is affected the most emotionally? How will they feel?",
                ["sad", "happy", "angry", "relieved", "scared", "loved", "guilty", "hopeful", "stressed",]
            )

        if question_type_mapping[scenario]=="slider":
                    
            emotions_3 = st.multiselect(
                "If option 3 is chosen, who is affected the most emotionally? How will they feel?",
                ["sad", "happy", "angry", "relieved", "scared", "loved", "guilty", "hopeful", "stressed",]
            )


        st.write("## Update or maintain your decision")  
        
        if question_type_mapping[scenario]=="multiple_choice":

            third_choice=st.radio(
            "",
            options=[option_1, option_2], key="third_choice")

        else:
            option_3 = data[scenario]['option_3']
            third_choice_1 = st.slider(option_1, 1, 7, 1, key=scenario+"_"+"third_choice_1")
            third_choice_2 = st.slider(option_2, 1, 7, 1, key=scenario+"_"+"third_choice_2")
            third_choice_3 = st.slider(option_3, 1, 7, 1, key=scenario+"_"+"third_choice_3")
     
        if st.button("confirm", key="third_button"):
            if question_type_mapping[scenario]=="multiple_choice":
                answer = first_choice
            else:
                answer = [first_choice_1, first_choice_2, first_choice_3]
            st.session_state['state']+=1
            st.session_state['user_answer'][scenario + "_" +str(st.session_state["state"])] = answer

    if st.session_state["state"]>2:
        if st.button("continue"):
            st.session_state["state"]=0
            st.session_state["question"]+=1
            st.rerun()

if __name__== '__main__':
    condition3(str(st.session_state["question"]))