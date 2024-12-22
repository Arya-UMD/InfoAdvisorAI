import streamlit as st
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings  # Correct class import for Hugging Face models
from langchain_community.vectorstores import FAISS

# Streamlit app title
st.title("Virtual Info Advisor Q&A 🌱")


# Function to load CSV data and return it as a pandas DataFrame
@st.cache_data  # Cache only the data, not the complex embedding models
def load_csv():
    return pd.read_csv('QandA.csv', encoding='latin-1')


# Create FAISS vector store from the CSV file without caching the embedding model itself
def create_faiss_index(df, _embedding_model):
    # Prepare documents with the questions
    questions = df['Question'].tolist()
    documents = [{'page_content': question} for question in questions]

    # Create FAISS vector store
    vectordb = FAISS.from_texts(texts=questions, embedding=_embedding_model)
    return vectordb


# Initialize the Hugging Face embeddings model (use HuggingFaceEmbeddings)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the Q&A data
df = load_csv()

# Create FAISS vector index for semantic search
vectordb = create_faiss_index(df, embedding_model)

# Input field for the user to ask a question
question = st.text_input("Question: ")

# If the user enters a question, perform the search and get the answer
if question:
    # Perform semantic search to find the most similar question in the dataset
    results = vectordb.similarity_search(question, k=1)  # Get the closest match

    # Extract the closest matching question
    if results:
        matched_question = results[0].page_content

        # Find the corresponding answer in the DataFrame
        matched_answer = df[df['Question'] == matched_question]['Answer'].values[0]
        st.header("Answer")
        st.write(matched_answer)
    else:
        # If no similar question is found, display "I don't know"
        st.header("Answer")
        st.write("I don't know")
