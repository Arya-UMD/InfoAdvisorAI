# InfoAdvisorAI
![image](https://github.com/user-attachments/assets/ee257061-0a34-4cba-bb1e-a5367bacf26e)

Project Report: Virtual Info Advisor Q&A Application
Introduction
This project presents a Virtual Info Advisor Q&A platform aimed at streamlining the process of providing quick and accurate answers to frequently asked questions. The system is designed to assist users with their queries in real-time using a semantic search-based methodology. The application is particularly suited for academic institutions or businesses that require a centralized system for handling common inquiries.

Objectives
Simplify Information Retrieval: Provide users with an intuitive platform to access specific answers from a dataset of predefined Q&A pairs.
Enhance User Interaction: Create a responsive and easy-to-use interface powered by Streamlit.
Utilize AI-Powered Search: Employ semantic search algorithms for improved relevance in question-answer matching.
Features
Semantic Search: Utilizes state-of-the-art Hugging Face embeddings (sentence-transformers/all-MiniLM-L6-v2) to process user queries and find similar entries in the Q&A dataset.
Efficient Query Processing: Leverages FAISS for fast and scalable similarity search.
Cached Data Loading: Integrates Streamlit’s caching mechanisms to improve app performance.
Flexible Deployment: Supports virtual and in-person use cases with drop-in advising timings included in the dataset.
Technical Overview
Tools and Technologies
Framework: Streamlit for building a user-friendly web interface.
Search Engine: FAISS (Facebook AI Similarity Search) for indexing and retrieving similar questions.
Machine Learning Model: Hugging Face sentence-transformer for embedding textual data.
Data Processing: Pandas for handling CSV datasets.
Workflow
Data Preparation:
A CSV file (QandA.csv) containing questions and their corresponding answers serves as the knowledge base.
Embedding Generation:
User questions and dataset entries are embedded into vector representations using Hugging Face models.
Index Creation:
A FAISS index is built to store and search the question embeddings efficiently.
Search and Retrieval:
User inputs are compared with the dataset using FAISS, retrieving the closest match and its corresponding answer.
Response Display:
The answer is presented in the app’s interface.
Functional Highlights
Input
A text field where users can type their questions.
Output
A matching answer from the dataset, displayed interactively in response to the query.
Drop-In Advising
Integrated drop-in advising timings:
Monday and Tuesday: 1:30 PM to 3:30 PM
Wednesday and Thursday: 9:30 AM to 11:00 AM
Available both virtually and in-person.
Results
The application successfully enables users to retrieve precise answers for their queries, minimizing time spent on manual searches or redundant questions. The semantic search model ensures highly relevant matches, improving user satisfaction.

Future Enhancements
Dynamic Dataset Updates: Add functionality for real-time updates to the Q&A dataset.
Improved NLP Models: Integrate more advanced language models for higher accuracy.
Multi-Language Support: Expand the app to handle queries in multiple languages.
Analytics Dashboard: Track usage metrics and popular queries for continuous improvement.
Conclusion
The Virtual Info Advisor Q&A application demonstrates the potential of combining machine learning techniques with interactive web tools to create effective information systems. Its robust design and ease of use make it a valuable tool for organizations looking to improve their information management processes.
