# Langchain
Langchain is a framework for building LLM-powered applications. It provides abstractions and components for connecting LLMs with prompts, tools, retrievers, vector databse, memory, structured outputs and application workflows

Without langChain
User
  ↓
Python Code
  ↓
Prompt
  ↓
LLM API
  ↓
Response

With LangChain
User
  ↓
Langchain Application
  ↓
Retrivers / Tools / Memory
  ↓
LLM
  ↓
Parser / Structured Output
  ↓
Response

# Why do we need LangChain
Suppose you are building a enterprise chatbot
You need:
LLM, Prompt Templates, RAG, Vector Databse, Document Loaders, Embeddings, Tools, Conversiona history, Structured responses, API integration
Writing all orchestration yourself becomes messy
LangChain gives you reusable abstrcutions
For Example:
Document -> Chunking -> Embeddings -> Vector DB -> Retriver -> Prompt -> LLM -> Answer

# Important LangChain Components

1. LLM / Chat Model: The model that generates responses.
Example: OpenAI, Anthropic, Amazon Bedrock, Gemini

2. Prompt Template: Instead of manually constructing prompt langchain provides ChatPromptTemplate
example:
from langchain_core.prompt import ChatPromptTemplates
prompt=ChatPromptTemplate.form_template("""
Answer the question using the context below
Context:
{context}
Question:
{question}
""")

# Chains: A Chain means connecting multiple operations together
For Example: Input -> Prompt -> LLM -> Parser -> OutPut
conceptually: chain = prompt | llm | parser
Then:
response=chain.invoke({
    "question":"what is RAG?"
})
**What is chain: A chain is a sequence of operations where the output of one component becomes the input of another. For example, a prompt can be passed to an LLM ans then the LLM output can be passed to an output parser. LangChain allows these components to be composed into reusable workflows.**

# LCEL - LangChain Expression Language is a simple way to connect different steps in LangChain using the | operator
Example: chain = prompt | llm | parser
Each step passes its output to the next steps
Then | opereator represents composition
Think: prompt -> LLM -> parser
This is called a Runnable pipeline
Example:
prompt="Explain {topic}"
llm=chatGPT
parser = StrOutputParser()
chain = prompt | llm | parser
If you run -> chain.invoke({"topic":"aws Lambda"})
It works roughly like:
"Explain AWS Lambda"
        ↓
      LLM
        ↓
" AWS Lambda is a serverless service..."
        ↓
     Parser
        ↓
Final clean text

So LCEL = a way to build pipelines/chains by connecting LangChain components with |.

Key thing to remember:

A | B | C means run A → pass the result to B → pass that result to C.

# RAG with LangChain

1. Indexing Phase
Documents -> Document Loader -> Text Splitting -> Chunks -> Embeddings -> Vector Database
Example:
PDF -> 100 page -> chunks -> embedding vectors -> Pinecone

2. Query Phase
User Ask: What is the company's leave policy
Then: question -> embeddings -> vector search -> relevent chunks -> prompt -> llm -> answer

# Retriever : A retriever job is to find out the relevent documents/chunks from the user's query
Example:
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)
Then:
docs = retriever.invoke(
    "What is the leave policy?"
)
**A retriver is a component that searches a knowledge source and returns documents relevant to a user query. In RAG, it retrives relevent chunks from a vector database or another search system, which are the provided to the LLM as context**

# Vector Store
LangChain can integrate with Pinecone, FAISS, Weaviate, Milvus, Chroma, OpenSearch etc
For my experience:
**For Finconecta**
s3
 ↓
Bedrock Knowledge Base
 ↓
Embeddings
 ↓
OpenSearch Serverless
 ↓
Semantic Search
 ↓
LLM
Thats conceptually very similar to a LangChain RAG system

# Tool: A tool is a external capability than an LLM can invoke\
This is where LangChain becomes interesting for Agentic AI.
Examples:
Weather api
Database Query
Calculator
Search API
Internal REST API
Python function
CRM API
Example:
@tool
def get_order_status(order_id str):
    return databse.get_order(order_id)

Now an agent can decode
User: "Where is order 123?"

LLM
 ↓
Recognize it needs order information
 ↓
Calls get_order_status()
 ↓
Get Result
 ↓
Generate Response

# Agent
A normal chain is A->B->C->D this workflow is predetermined
An agent is more dynamic:
              ┌── Tool A
              │
User → Agent ─┼── Tool B
              │
              ├── Tool C
              │
              └── Final Answer
Then LLM decides: Which tool should I use

# Chain vs Agent
Difference between chain and agent
**A chain follows a predefined sequence of operations, wheras an agent dynamically decides which action or tool to execute based on user's request. Chains are useful when the workflow is deterministic, while agents are useful when the workflow requires dynamic decision-making**
Example:
Chain: Question -> Retriver -> LLM -> Answer
Agent: Question -> Agent -> Should I Search -> Should I query DB? -> Should I call API? -> Final Answer

# Memory
Suppose user says:
User: My name is Fasi
LLM: Nice to meet you
User: What is my name?
The application needs converstaion context
Conceptually: Conversation Hitory -> Prompt -> LLM
**The LLM does not automatically remebers previous conversations.Your application has to save the conversation history somewhere(like Redis, DynamoDB, PostgreSQL etc) and then send that history back to the LLM when the user asks a follo-up-question**
Possible Storage: Redis, PostgreSQL, DynmoDB, MongoDB

# Context Management
Always remeber LLMs have a finite context window
Suppose conversation becomes: 100,000 tokens you can't blindly send the entire history ever time.
Solutions:
1. Truncation: Keep recent messages\
   old messages -> remove
   new messages -> keep
2. Summarization
   old conversation -> summary -> store summary
3. Retrieval-based memory
   Store important information in a datbase/vector store
   Conversation -> Embeddings -> Vector DB -> Retrieve relevent memories
4. Hybrid
   Recent conversation -> summary -> relevent memories









