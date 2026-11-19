from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st




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
