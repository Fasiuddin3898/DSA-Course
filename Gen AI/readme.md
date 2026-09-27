# Generative AI
In generative AI you generate new content as per your reqiiremet example gpt, opous models.In summary generative AI is a category of AI that is associated with generating new content and that new content can be text, audio, video, images etcs 

# Non Gnerative AI:
You have a data and based on the past data you have to make decision for example you have perons financial data and you decide to give him a loan or not example ML models.

# Machine Learning Evolution:
For structured data we use "Statistical ML Models"
For un structured data we use "Neuarl Networks"
Statistical ML --> Neural Networks --> Recuurant Neural Network (RNN )
Language Model is an AI model that can predict next word(or set of words) for a given sequence of wordss
Text Model

statistical ML -> Neural Networks -> Recurrent Neural Networks(RNN) -> Transformers
# GPT Full Form : Generative Pre-trained Transformer
# Embeddings
Embedding is noting but a numeric representation of text inform of a vector in such a way that you can capture meaning of that text.Once you create embeddings you can do maths with words and sentences.

Lets understand vector database
# Sematic Search
Instead of just matching the key words understand the intent of the sentence and and give you the results.

# Neual Networks
when you search employee in apple and calories in apple google understands that first apple is phone and second apple is fruit
for vector data base you store the apple phone with some keywords like example (revenue of Apple)
related_to_phone 1
is_location 0
has_stock 1
revenue 82
is_fruit 0
calories 0 
we store same for apple as a fruit and orange as a fruit but there we give is_fruit 1 and calaroies 88 and 99 respectively and compare the embeddings of apple phone with apple company and apple fruit with orange fruit which matches the embedding more that result we produce 
famous example in NLP domain king - man + women = Queen this is called word to word technique 
We store this million of text embeddings in a vector database and when a query is asked we generate a embedding for that text and match with the embeddings which are present in our vectore base to get the exact match we use the cosine similarity or we use the hash tables where similar embessings stored in one place and we perform the linear search over there this technique is called locality sensitive hashingh. 

# LangChain:Langchain is a framework that allows you to build applications on top of llm or large language model

# RAG(Retrieval Argumented Generation)
  
# LangChain project
install langchain pip install langchain
and after that pip install openai

We have a variable temperature means how creative you want your model to be.
->if temp is set to 0 it means it is very safe it is not taking any bets
->if temp is set to 1 it will take risk, it may generate wrong output but it is very creative at the same time

Streamlit is a python framework used to quickly build interactive web applications and dashboards for machine learning and data science prjects using simple python code

-> verbose by keeping this a true any where in the code where we are calling the model we can get all the steps taking by the model before generating the response

-> SerpApi : It is google search API, what ever you do on google and what results it gives you and if you want to access those results programatically yopu can use SerpApi

-> What is memory for an Agent/Model?
Memory is something it remembers our all past conversations also on asking irrevelent questions it gives exact answer, once it asked about that previously

ConversationBufferMemory this captures all the converstaion happened between the llm and sends all the memory to the llm which increase the token size of the llm and as well it is very costly, so according to our use case we can send limited converstaions to llm instead of all using ConversationBufferWindowMemory

Semantic Search understands the context of the prompt and provide results as per context instead of only focousing on keywords.
For semantic search, we use something called embedding and a vector database.

# Architecture we will be using for 

TextLoader(UnsstructuredURLLoader) -> CharacterTextSplitter(Recursive text splitter) -> FAISS(Vector Data Base) -> RetrievalQAWithSourcesChain

# Text Loaders

