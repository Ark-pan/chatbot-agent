import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Ai Chatbot", page_icon="🤖")
st.title("🤖 A Simple Ai Assistant v2.0")

# Setup Official Google SDK
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Missing API Key!")
    st.stop()

# Initialize Model
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Interaction Logic
if prompt := st.chat_input("What can I do for you today?..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Standard Streaming with the Official SDK
        try:
            # We use the built-in stream=True
            response = model.generate_content(prompt, stream=True)
            
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:

            st.error(f"Error: {e}")
