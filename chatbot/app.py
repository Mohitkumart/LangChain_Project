import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## Langsmith tracking
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Promt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Please response to user quesies"),
        ("user","Qestion:{question}")
    ]
)

## Streamlit framework

st.title("Langchain Demo With OPENAI API")
input_text = st.text_input("Search the topic you want")

## OPEN AI LLM

llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
