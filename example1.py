## Integerate our code OPen ai key
import os
from constant import openai_keys
from langchain.llms import openai
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SimpleSequentialChain # in this it will only show the last message chain
from langchain.chains import SequentialChain# in this it will only show the every message chain
from langchain.memory import ConversationBufferMemory # to store the memory




import streamlit as st

os.environ["OPENAI_API_KEY"] = openai

# streamlit framework

st.title('Celebrity search results')
input_text = st.text_input("Search the topic you want")

# Prompt templates
first_input_template = PromptTemplate(
    input_variable=['name'],
    template="Tell me about {name}"
)
## OPENAI LLM
llm=openai(temperature=0.8)
chain = LLMChain(llm=llm, prompt= first_input_template, verbose=True, output_key='person')


# Prompt templates
second_input_template = PromptTemplate(
    input_variable=['person'],
    template="When was the {person} born"
)
## OPENAI LLM
llm=openai(temperature=0.8)
chain2 = LLMChain(llm=llm, prompt= second_input_template, verbose=True, output_key='dob')

# Prompt templates
third_input_template = PromptTemplate(
    input_variable=['dob'],
    template="Mention 5 major events happened around {dob}"
)
## OPENAI LLM
chain3 = LLMChain(llm=llm, prompt= third_input_template, verbose=True, output_key='description')

# parent_chain = SimpleSequentialChain(chains=[chain,chain2], verbose=True)

parent_chain = SequentialChain(chains=[chain,chain2,chain3],input_variables=['name'], output_variables=['person','dob','description'], verbose=True)


# if input_text:
#     st.write(parent_chain.run(input_text))
if input_text:
    st.write(parent_chain({'name':input_text}))