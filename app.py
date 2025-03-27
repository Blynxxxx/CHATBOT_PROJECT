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

def initialize_embeddings():
    """Initialize Google Gemini embeddings."""
    try:
        return GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=gemini_api_key)
    except Exception as e:
        st.error(f"Error initializing embeddings: {e}")
        return None

def create_vector_store(pdf_path, chunks, embeddings):
    """Create or load a vector store."""
    store_name = os.path.basename(pdf_path).replace('.pdf', '')
    store_path = f"vector_stores/{store_name}"

    if os.path.exists(store_path):
        return FAISS.load_local(store_path, embeddings, allow_dangerous_deserialization=True)
    else:
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        vector_store.save_local(store_path)
        return vector_store

def get_user_query():
    """Get the user query from Streamlit input."""
    return st.text_input("💬 Ask a question about Orientation:")


def generate_response(llm, docs, query):
    """Generate a response to the user query."""
    prompt = (
        f"You are a James Cook University Koalion and you are here to help Q&A regarding orientation information for new students."
        f"Based on the given information and text, answer the question: '{query}' in detail."
    )
    
    chain = load_qa_chain(llm=llm, chain_type="stuff")

    if docs:
        response = chain.run(input_documents=docs, question=prompt)
        negative_indicators = [
            "not contain information",
            "the text only mentions",
            "no relevant information",
            "unable to answer",
            "not found",
            "does not provide",
            "don't know ",
            "sorry"
        ]
        
        if not response or any(indicator in response.lower() for indicator in negative_indicators):
            prompt = (
                f"You are a James Cook University Koalion. Answer the following question based on general knowledge: '{query}'. "
                "If you cannot find specific information, provide a helpful response using information form the internet."
            )
            response = llm.invoke(prompt)
    else:
        response = llm.invoke(prompt)

    return response


def main():
    initialize_sidebar()
    st.title("📚 Orientation Chatbot")

    pdf_path = 'data/database.pdf'  # Update file path if needed

    if os.path.exists(pdf_path):
        text = extract_text_from_pdf(pdf_path)
        chunks = split_text(text)
        
        embeddings = initialize_embeddings()
        if embeddings is None:
            return

        vector_store = create_vector_store(pdf_path, chunks, embeddings)
        query = get_user_query()

        if query:
            with st.spinner("Finding information..."):
                docs = vector_store.similarity_search(query=query, k=5)
                llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2, google_api_key=gemini_api_key)
                response = generate_response(llm, docs, query)

                # Display response with background
                st.markdown(f'<div style="background-color:#f4f4f4;padding:10px;border-radius:10px;">{response}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
