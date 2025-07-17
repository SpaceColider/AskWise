import streamlit as st
import requests

# Set your Claude API Key here
API_KEY = "or-v1-e032c02ddcb3363fc8a88fbc2933b389189f97d5fb97d02dcb3e1a6dd70fec22"  # Paste your OpenRouter API key here

# Claude model name
MODEL = "anthropic/claude-sonnet-4"

# App UI
st.set_page_config(page_title="AskWise", layout="centered")
st.title("Team 1, team leader-Smayan")
st.markdown("Ask me anything!")

# Input box
user_input = st.text_input("You:", "")

# Chat mode selector
mode = st.radio("Select Response Mode:", ["Direct Answer", "Hint( For mathematical questions only)", "Full Explanation"])

# Build prompt based on mode
if user_input:
    if mode == "Direct Answer":
        prompt = user_input
    elif mode == "Hint":
        prompt = f"Give only a hint to solve the following question without giving the final answer: {user_input}"
    else:
        prompt = f"Give a full explanation for: {user_input}"

    # Claude API call using OpenRouter
    headers = {
    "Authorization": f"Bearer {API_KEY}",  # ✅ This MUST begin with f"
    "HTTP-Referer": "https://askwise-8sekwyge5pusbxguzxycxq.streamlit.app",
    "X-Title": "My AI Chatbot"
}


    

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        st.markdown(f"**Claude:** {reply}")
    else:
        st.error(f"Error: {response.status_code}\n{response.text}")
