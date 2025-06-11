# 💬 LangChain_Project

A chatbot interface built using **LangChain** with support for both **OpenAI** and **Ollama (Local LLMs)**. The frontend is powered by **Streamlit** for an interactive and clean experience.

---

## 📦 Requirements

Make sure you have Python 3.8+ installed.

Install the dependencies using:

```bash
pip install -r requirements.txt


### USING OPEN AI
 -- make sure you put following details in your .env 

LANGCHAIN_API_KEY = ""
OPENAI_API_KEY = ""

# Run Open AI chatbot
"streamlit run chatbot/app.py" 

## Using OLLAMA

1- Download ollama in your system 
[Download Ollama](https://ollama.com/download)

2 - install models in your system

Run the following command in your terminal (CMD):

```bash
ollama run gemma


# Run OLLAMA chatbot
"streamlit run chatbot/locallama.py" 

