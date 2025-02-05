import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page design
st.set_page_config(page_title="Book Recommender System", page_icon="📚")
st.title("Book Recommender System")
st.subheader("Find your next great read!")

# Input field for user to enter book title, genre, or keyword
user_input = st.text_input("Enter the book title, genre, or keyword")

# Prompt template for generating book recommendations
demo_template = '''Based on "{user_input}", provide book recommendations.'''
template = PromptTemplate(
    input_variables=['user_input'],
    template=demo_template
)

# Initialize the language model
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate recommendations
def get_recommendations(user_input):
    prompt = template.format(user_input=user_input)
    recommendations = llm.predict(text=prompt)
    return recommendations

# Display recommendations or a prompt to enter input
if user_input:
    recommendations = get_recommendations(user_input)
    st.write("### Recommendations for you:")
    st.write(recommendations)
else:
    st.info("Please enter a book title, genre, or keyword to get recommendations.")

# Add a footer for better aesthetics
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
    Made with ❤️ by [Your Name]
    </div>
    """, unsafe_allow_html=True
)
