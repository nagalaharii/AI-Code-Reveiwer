import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAr6TSzpmpFs_uKgYJqcVnI2rhJVGMrGh0")
sys_prompt = """You are an AI code reviewer in a Python application.
                Your job is to:
                Identify Issues: Find bugs, syntax errors, and logical flaws in the code.
                Provide Fixes: Return corrected or optimized code snippets with explanations.
                Keep explanations simple and accessible, maintaining a professional tone.
                Focus on accuracy, efficiency, and enhancing the user's understanding of best coding practices.
"""
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                          system_instruction=sys_prompt)
st.title("An AI Code Reviewer")

user_prompt = st.text_area("Enter your Python code here...")

if st.button("Review Code"):
    if user_prompt:
        response = model.generate_content([sys_prompt, user_prompt])
        ai_response = response.text
        st.write(ai_response)
    else:
        st.write("Please enter some code to review.")