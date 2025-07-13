print('hello')
import streamlit as st

genre = st.radio(
    "What's your favorite color?",
    ["blue", "red", "purple"]
)
age = st.slider("", 0, 130, 0)
st.title("Ethical Decision-Making")
st.dataframe(data=None, width=None, height=None)
st.text_input(label="good", value="10", type="default")
options = st.multiselect(
    "What are some of the specific harms of not reporting your friend? Who is affected negatively? How will they feel?",
    ["sad", "angry", "despaired", "stressed", "guilty", "frustrated", "scared"]
    
)

"13": {
        "scenario": "Your friend asks you what you think about their artwork, but you feel that it is poorly done. Do you lie to protect their feelings?",
        "AI-suggestions": "Tell them what you really think about their artwork. Honesty builds trust. If you lie, your friend may never improve and could be misled about their work. However, you can be kind and constructive in how you share your opinion. For example, you might say, “I think you’ve got a strong concept, but maybe the technique could use more work.” This way, you’re being honest without being hurtful, and supporting their growth.",
        "utilitarianism": "It depends, but lean toward Option 1 – Tell the truth gently. Utilitarianism seeks to maximize overall happiness and minimize harm. If the truth helps your friend grow as an artist (even if briefly painful), it leads to long-term benefit. But if they're in a vulnerable emotional state, a harsh truth could do more emotional harm than good. Therefore, the best utilitarian choice is to tell the truth in a kind, encouraging, and helpful way — e.g., “Here’s what’s strong, and here’s what could improve.”",
        "deontology": "Tell them what you really think. Deontology is about moral duties and universal principles. One core principle is to always tell the truth—lying is inherently wrong because it disrespects others' autonomy. Even if the lie is well-intended, deceiving someone violates their right to the truth. You're obligated to be honest, but that doesn’t mean you have to be cruel — you can offer your opinion respectfully.",
        "virtue ethics": "Tell the truth kindly. Virtue ethics emphasizes being a good person and acting with integrity, courage, and kindness. Lying may feel kind, but it's cowardly if you're avoiding discomfort at the cost of honesty. A virtuous person finds a way to be genuine yet supportive — helping a friend improve while preserving the relationship.",
        "care ethics": "Lie to protect their feelings (or a gentle version of the truth). Care ethics focuses on relationships, empathy, and emotional well-being. If your friend is emotionally vulnerable, being honest might hurt the relationship or their self-esteem. The caring thing to do might be to protect their feelings—not through deception, but perhaps by focusing on what you genuinely like or offering soft, constructive feedback.",
        "option_1": "Tell them what you really think",
        "option_2": "Lie to protect their feelings",
        "slider_caption_1": "Use the slider to visualize the harm created if option 1 is chosen",
        "slider_options_1": ["no harm", "minimal harm", "some harm", "significant harm", "very significant harm"],
        "slider_caption_2": "Use the slider to visualize the harm created if option 2 is chosen",
        "slider_options_2": ["no harm", "minimal harm", "some harm", "significant harm", "very significant harm"]
    },