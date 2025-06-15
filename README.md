🩺 MEDI-BOT
MEDI-BOT is an AI-powered assistant that answers medical queries using standard treatment guidelines. It leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-based responses.

🚀 Features
✅ Ask any disease-related question and get an AI-generated response based on medical guidelines
✅ Uses Groq + LangChain for fast and powerful LLM answers
✅ Embeds PDF guidelines with HuggingFace sentence-transformers
✅ Efficient vector search using FAISS
✅ Interactive frontend built with Streamlit

⚙️ Tech Stack
LangChain (RAG framework)

Groq (LLM backend)

HuggingFace Embeddings (sentence-transformers/all-MiniLM-L6-v2)

FAISS (vector storage and search)

Streamlit (frontend)


📝 How It Works
1️⃣ The PDF of standard treatment guidelines is loaded and split into chunks.

2️⃣ Each chunk is converted into embeddings using HuggingFace.

3️⃣ FAISS indexes the embeddings for fast retrieval.

4️⃣ LangChain combines Groq’s LLM with the relevant chunks to generate answers.

5️⃣ Streamlit provides an easy-to-use interface for users to ask questions.

🌱 Future Improvements
Enhance accuracy with more medical documents

Add user authentication

Improve UI/UX design

Explore more advanced RAG strategies

💡 Goal
This project was built to gain deeper knowledge of RAG (Retrieval-Augmented Generation) and experiment with combining LLMs + custom medical data.

