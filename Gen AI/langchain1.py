from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")

response = llm.invoke("I want to open a restaurant for Indian food. Suggest a fancy name.")

print(response.content)