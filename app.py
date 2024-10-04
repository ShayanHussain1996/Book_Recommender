import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

#import the local environment
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# Design the page
headers={"authorization":st.secrets["GOOGLE-API-KEY"],"content-type":"application/json"}
st.title("Book Recommender Systems...")
user_input = st.text_input("Enter the Book title,genre or keyword")

demo_template = '''Based on {user_input}provide Book recommendations'''
template = PromptTemplate(
    input_variables=['user_input'],
    template=demo_template
)

llm=ChatGoogleGenerativeAI(model="gemini-pro",api_key=os.getenv("GOOGLE-API-KEY"))

if user_input:
    prompt = template.format(user_input=user_input)
    recommendations=llm.predict(text=prompt)
    st.write(f"Recommendations for you:\n{recommendations}")
else:
    st.write("enter")