from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

#LLMChain is an object in which you defined what is your llm and what is your prompt

llm_groq=ChatGroq(model="llama-3.3-70b-versatile")
prompt_template_name=PromptTemplate(
    input_variables=['cusine','food'],
    template="I want to open a resturant for {cusine} {food} food .Suggest a fancy name for my resturant"
)

chain=LLMChain(llm=llm_groq,prompt=prompt_template_name)
print(chain.run({"cusine":"American","food":"Fast"}))
print(f'memeory {chain.memory}')