## Integerate our code OPen ai key
import os
from constant import openai_keys
from langchain.llms import openai

import streamlit as st
os.environ["OPENAI_API_KEY"] = openai

# streamlit framework

st.title('Langchain demo with openai')
input_text = st.text_input("Search the topic you want")

## OPENAI LLM
llm=openai(temperature=0.8)

if input_text:
    st.write(llm(input_text))