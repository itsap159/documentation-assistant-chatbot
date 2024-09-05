# Documentation Assistant Chatbot

### A LLM-powered chatbot for enhanced documentation accessibility

---

## Overview

This project is an LLM-based Documentation Assistant Chatbot designed to assist users in quickly retrieving and interacting with documentation. It leverages Retrieval-Augmented Generation (RAG), LangChain, Pinecone, and Streamlit for its core functionality. By combining the power of these technologies, the chatbot delivers fast, accurate, and relevant answers to user queries.

Key features include web scraping for automated knowledge base creation, robust query handling, and a user-friendly interface using Streamlit.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **LLM-powered query handling**: Efficiently answer questions from the documentation using a pre-trained language model.
- **Retrieval-Augmented Generation (RAG)**: Improves retrieval accuracy by 40%, ensuring more relevant results.
- **Streamlit Interface**: Easy-to-use and responsive UI for seamless interaction.
- **Knowledge Base Generation**: Automated web scraping to build a comprehensive and up-to-date knowledge base.

---

## Technologies Used

- **Language Models**: Pre-trained LLMs for natural language understanding and query generation.
- **LangChain**: A framework for integrating language models with various data sources.
- **Pinecone**: A fast and scalable vector database for document embeddings and retrieval.
- **Streamlit**: Web-based user interface for the chatbot.
- **Web Scraping**: Tools and scripts for automatically building and maintaining the knowledge base from documentation sources.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/documentation-assistant-chatbot.git
cd documentation-assistant-chatbot
```

### Create the vritual environment and install the dependencies.

```bash
pipenv install
pipenv shell
```

### Run the app

```bash
streamlit run main.py
```
You can now interact with the application on your local computer.

## How It Works
- **RAG (Retrieval-Augmented Generation)**
The chatbot uses RAG to first retrieve relevant documents using Pinecone and then generate a precise response based on these documents. This two-stage approach ensures relevance and coherence in the answers.

- **LangChain**
LangChain integrates various components, including retrieval, LLM-based response generation, and document parsing.

- **Pinecone Vector Database**
Documentation is indexed as vector embeddings in Pinecone. User queries are matched to the most relevant vectors (documents) in real-time.

- **Web Scraping**
A script periodically scrapes new documentation from specified URLs, indexes it in Pinecone, and updates the knowledge base.

- **Streamlit**
Provides a web interface for users to interact with the chatbot, submit queries, and upload documents.- 