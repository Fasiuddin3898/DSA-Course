# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
# load_dotenv()

# llm=ChatGroq(model="llama-3.3-70b-versatile")

prompt_template_name=PromptTemplate(
    input_variables=['cusine','food'],
    template="I want to open a resturant for {cusine} {food} food .Suggest a fancy name for my resturant"
)

response=prompt_template_name.format(cusine="Italian",food="indian")

print(response)

#A promptTemplate in langchain is a reusable template used to dynamically generate prompts by inserting variables into predefinde text
