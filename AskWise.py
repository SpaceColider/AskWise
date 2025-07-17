import gradio as gr
import requests

API_KEY = "or-v1-e032c02ddcb3363fc8a88fbc2933b389189f97d5fb97d02dcb3e1a6dd70fec22"
MODEL = "anthropic/claude-sonnet-4"

def ask_ai(user_input, mode):
    if mode == "Direct Answer":
        prompt = user_input
    elif mode == "Hint":
        prompt = f"Give only a hint to solve the following question without giving the final answer: {user_input}"
    else:
        prompt = f"Give a full explanation for: {user_input}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://your-deployment-url.com",
        "X-Title": "My AI Chatbot"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error {response.status_code}: {response.text}"

iface = gr.Interface(
    fn=ask_ai,
    inputs=[
        gr.Textbox(label="Ask me anything!"),
        gr.Radio(["Direct Answer", "Hint", "Full Explanation"], label="Mode", value="Direct Answer")
    ],
    outputs="text",
    title="AskWise",
    description="Team 1, Team Leader – Smayan"
)

iface.launch()
