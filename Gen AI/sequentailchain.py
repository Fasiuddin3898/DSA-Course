# A SequentailChain in LangChain is advanced chain that connects multiple chains together while allowoing multiple outputs and inputs between them
from langchain_groq import ChatGroq
from langchain.chains import LLMChain,SimpleSequentialChain,SequentialChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

prompt_template_name=PromptTemplate(
    input_variables=['cusine'],
    template="I want to open a resturant for {cusine} food.Suggest only one fancy name for my resturant"
)

name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="resturant_name")

prompt_template_items=PromptTemplate(
    input_variables=['resturant_name'],
    template="Suggest some menu items for {resturant_name}.Return it as a comma seperated items."
)

items_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key="items_name")

seq_chain=SequentialChain(
    chains=[name_chain,items_chain],
    input_variables=['cusine'],
    output_variables=['resturant_name','items_name']
)

response=seq_chain.invoke({'cusine':'Hyderabadi'})

print(f'seq_chain response {response}')