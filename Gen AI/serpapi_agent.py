import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain,SimpleSequentialChain,SequentialChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools

load_dotenv()


serp_api=os.getenv("SERPAPI_API_KEY")
llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

tools=load_tools(["serpapi","llm-math"],llm=llm)

agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

answer=agent.run("What is the GDP of india in 2025")
print(f'answer {answer}')