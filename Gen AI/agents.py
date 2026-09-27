# A Reasoning model is an AI model designed to think step by step, analyze context and make logical decisions before generating a response.
# An agent is an AI system that can reason, take actions, use tools/apis, remember context and autonoously complete task towards a goal.x
# In simple words agents will connect with external tools it will use llm reasoning capabilities to perform a given task

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

tools=load_tools(['wikipedia','llm-math'],llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True # By keeping this as true we can find out what are the internal steps it is taking
)

response=agent.run("When was Elon Musk born? What is his age right now in 2026?")
print(f'response of elon mask {response}')