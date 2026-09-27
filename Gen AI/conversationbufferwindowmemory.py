from langchain.memory import ConversationBufferWindowMemory #In ConversationBufferWindowMemory this we only restrict certain amount of chat should goes in
from langchain.chains import LLMChain,ConversationChain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

#LLMChain is an object in which you defined what is your llm and what is your prompt

llm_groq=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

memory = ConversationBufferWindowMemory(k=1)

convo = ConversationChain(
    llm=llm_groq,
    memory=memory
)
convo.run("Who won first cricket world cup")
answer1=convo.run("who was the caption of the winning team?")
print(f'answer1 {answer1}')
convo.run("What is 5+5?")
answer=convo.run("who was the caption of the winning team?")
print(f'answer after the window set to 1 {answer}')