# Memory is something which remebers your past prompts and outputs and try to give relevent answers as per that

from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory #In ConversationBufferWindowMemory this we only restrict certain amount of chat should goes in
from langchain.chains import LLMChain,ConversationChain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
memory=ConversationBufferMemory() #Object of that class

#LLMChain is an object in which you defined what is your llm and what is your prompt

llm_groq=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)
prompt_template_name=PromptTemplate(
    input_variables=['cusine'],
    template="I want to open a resturant for {cusine} food .Suggest a fancy name for my resturant"
)

chain=LLMChain(llm=llm_groq,prompt=prompt_template_name,memory=memory)
convo=ConversationChain(llm=llm_groq)
print(chain.run("American"))
print(f'---------------')
print(f'memeory {chain.memory.buffer}')
print(f'--{convo.prompt.template}')
convo.run("Who won first cricket world cup")
convo.run("What is 5+5?")
ans=convo.run("who was the caption of the winning team?")
print(f'ans --------{ans}')
print(f'memory------{convo.memory}')


