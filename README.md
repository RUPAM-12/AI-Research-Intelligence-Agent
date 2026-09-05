# 🔎 AI Research Intelligence Agent

An agent-based AI research assistant that can search for information, plan research tasks, and generate structured responses using a local Large Language Model.

## ✨ Features

- 🤖 Multi-agent research workflow
- 🧠 Local LLM integration using Ollama
- 🔍 Web search and information gathering
- 📋 Task planning and execution
- 💾 Memory support
- 🌐 Streamlit web interface
- 🔄 Iterative agent workflow

## 🛠️ Technologies

**Python · Streamlit · Ollama · Requests · DuckDuckGo Search · Local LLMs**

## 🧩 Architecture

```text
User Query
    ↓
Agent Loop
    ↓
Planner Agent
    ↓
Research Agent
    ↓
Web Search / Tools
    ↓
Memory
    ↓
Final Response
🚀 Run Locally

Create a virtual environment:

python -m venv venv

Activate it on Windows:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install streamlit ollama requests ddgs

Make sure Ollama is installed and a supported local model is available.

Run the application:

python -m streamlit run app.py

Open:

http://localhost:8501

📁 Project Structure
AI-Research-Intelligence-Agent/
├── agents/
├── memory/
├── tools/
├── .streamlit/
├── agent_loop.py
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
🎯 Purpose

The project demonstrates how multiple specialized AI agents can work together to perform research-oriented tasks using a local language model and external information sources.

🙏 Acknowledgment

This project builds upon an existing open-source implementation. Original authors, licenses, and third-party components are retained and acknowledged.