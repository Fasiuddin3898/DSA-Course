# A simpleSequentialChain in LangChain is a chain where the output of one LLM/prompt becomes the input of the next step sequentially.
from langchain_groq import ChatGroq
from langchain.chains import LLMChain,SimpleSequentialChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")

prompt_template_name=PromptTemplate(
    input_variables=['cusine'],
    template="I want to open a resturant for {cusine} food.Suggest only one fancy name for my resturant"
)

name_chain=LLMChain(llm=llm,prompt=prompt_template_name)
print(f'name_chain {name_chain.run("Hyderabadi")}')

prompt_template_items=PromptTemplate(
    input_variables=['resturant_name'],
    template="Suggest some menu items for {resturant_name}.Return it as a comma seperated items."
)

food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items)

chain=SimpleSequentialChain(chains =[name_chain,food_items_chain])
response=chain.run("Indian")
print(f'response {response}')



