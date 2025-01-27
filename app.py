from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

api_key = "AIzaSyDpw30wC4ISAQPqznh2XMMxgJj7d_1TOPY"
genai.configure(api_key=api_key)
##genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash-002")
def get_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="ASK RI")
st.header("GPT made by RRS29")
input=st.text_input("Input : ",key="input")
submit=st.button("Ask RI anything")


if submit:
    response=get_response(input)
    st.subheader("The Response is: ")
    st.write(response)