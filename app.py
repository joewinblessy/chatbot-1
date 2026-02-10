import streamlit as st
import google.generativeai as genai

# put your API key here (quick test only)
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 Gemini Bot")

user_text = st.text_input("Ask something:")

if st.button("Send"):
    response = model.generate_content(user_text)
    st.write(response.text)
