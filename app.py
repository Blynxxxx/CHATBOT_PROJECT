import streamlit as st
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

def initialize_sidebar():
    """Set up the sidebar contents."""
    with st.sidebar:
        st.title('Orientation Chatbot')
        st.markdown('''
        ## About
        This app is an LLM-powered chatbot built using:
        - [StreamLit](https://streamlit.io/)
        - [LangChain](https://python.langchain.com/)
        - [Google Gemini](https://ai.google.dev/)
        ''')
        add_vertical_space(5)
        st.write('Created by Group-8')

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text.replace("\n", " ") + " "
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
    return text.strip()

def split_text(text):
    """Split text into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=300, 
        length_function=len
    )
    return text_splitter.split_text(text=text)        