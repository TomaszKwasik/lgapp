from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from func import script_file_path
from func import set_new_cwd

from langchain_core.globals import set_debug

set_debug(True)

st.title("Ask anything")

with st.sidebar:
    st.title("Provide the API key")
    API_KEY =  st.text_input("Grok API", type="password")

if not API_KEY:
    st.info("Enter Grok API key to continue")
    st.stop()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=API_KEY,  
    temperature=0.7
)


question = st.text_input("Enter the question: ")

if question:
    response = model.invoke(question)
    st.write(response.content)