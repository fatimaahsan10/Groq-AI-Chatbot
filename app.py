import os
import gradio as gr
from groq import Groq

# Get API key from secret environment
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)
model_name = "llama3-8b-8192"

# Define chat function
def chatbot(message, history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    reply = response.choices[0].message.content
    return reply

# Launch Gradio ChatInterface
gr.ChatInterface(fn=chatbot, title="🤖 Groq AI Chatbot", theme="soft").launch()
