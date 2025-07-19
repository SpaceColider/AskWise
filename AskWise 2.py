import streamlit as st
import requests
import os

# --- Load API key from Streamlit secrets ---
API_KEY = st.secrets["OPENROUTER_API_KEY"]  # Secure, no hardcoding!

# Claude model name
MODEL = "anthropic/claude-sonnet-4"

# App UI
st.set_page_config(page_title="AskWise", layout="centered")
st.title("Team 1 – Team Leader: Smayan")
st.markdown("### Ask me anything!")

# User input
user_input = st.text_input("You:", "")

# Mode selector
mode = st.radio("Select Response Mode:", ["Direct Answer", "Hint (Math only)", "Full Explanation"])

# Prepare Claude API call
if user_input:
    if mode == "Direct Answer":
        prompt = user_input
    elif mode == "Hint (Math only)":
        prompt = f"Give only a hint to solve the following question without giving the final answer: {user_input}"
    else:
        prompt = f"Give a full explanation for: {user_input}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://askwise.streamlit.app/",  # Optional: Your Streamlit Cloud app URL
        "X-Title": "AskWise Claude Chatbot"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    # Make the request
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    # Display result
    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.markdown(f"**Claude:** {reply}")
    else:
        st.error(f"API Error {response.status_code}: {response.text}")

