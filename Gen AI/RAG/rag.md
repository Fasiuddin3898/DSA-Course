# RAG = Retrieval-Augmented Geneartion
Instead of asking an LLM to answer only from the knowledge learned during training, we retrive relevent information from our own knowledge base and provide that information as context to the LLM.

Basic Architecture 
1. First flow - Prepare the documets
Documents
↓
Documents Loader -> Reads the documents and give us the document content
↓
Preprocessing -> Clean/normalizes that content
↓
Chunking -> Splits the content into smaller pieces
↓
Embedding Models -> Converts each chunks into numbers (vectors)
↓
Vector Embeddings -> The numerical represnetation of each chunk
↓
Vectore Databse -> Stores the chunks + their vectors for later searches

2. Second flow - User asks question
User Question
↓
Embedding Model -> Converts the question into a vector
↓
Query Vector -> Numerical representation of the question
↓
Vector Search -> Searches the Vector Database for vectors similar to the question
↓
Top-K Relevent Chunks -> Gets the most relevent pieces of the original document
↓
Prompt Construction -> Combines the user's question + relevent chunks into a prompt
↓
LLM -> Reads the prompt and generates the answer
↓
Final Answer -> Returned to the user

RAG combines information retrieval with a LLM. We first convert enterprise documents into embeddings and store them in a vector database. When the user asks a question, we convert the query into an embedding, retrive the most relvant document chunks using similarity search, add those chunks to the prompt, and send the augmented prompt to the LLM to generate a grounded answer.

# Why do we need RAG?
Why use RAG when we already have ChatGPT or LLM?
LLMs have a fixed training cutoff and don't automatically know private enterprise information. They can hallucinate
RAG allows us to provide current and domain-specific information to the model at runtime. It avoids retraining the model every time data changes and makes responses more grounded in enterprise data.

Main reasons:
Private/company data
Latest information
Reduce hallucination
Provide domain-specific context
Avoid expensive fine-tuning
Easier knowledge updates
Can provide citations/source references

# RAG has two major pipelines

1. Offline/Ingestion Pipeline
Documents -> Document Loader -> chunks(splits the data into smaller pieces) -> embedding model (coverts each chunks in to number) -> vector embeddings (The numerical represntation of each chunk) -> vector Database (stores the chunks + their vectors for lateral search)

2. Online/Query Pipeline
User query -> Query Embedding also (Embedding model) -> vector search -> retrive top-k chunks -> Optional reranking -> Construct prompt -> LLM -> Response

If asked what happens when a new documnet is uploaded ?
Explain Ingestion pipeline
If asked what happens after a user asks a question?
Explain the retrieval/query pipeline

# Document Ingestion
Imagine the company uploads.
pdf, docx,csv,txt,html,confluence pages,databse records
First a loader reads the documents
for example: document=load_document("company_policy.pdf")
Then extract text.
pdf -> Text extraction -> cleaning -> chunking
possible preprocessing.
1. remove html
2. remove extra whitespace
3. remove headers/footers
4. noemalize encoding
5. extract tables
6. preserve document metadata
Example:

{
    "text": "Employees receive 24 annual leaves...",
    "source": "employee_policy.pdf",
    "page": 15,
    "department": "HR"
}

Metadata becomes extremely useful later.

# Chunking
We usually don't embed an entire 100-page PDF as one vector
Instead
Doucent
↓
chunk 1
chunk 2
chunk 3
chunk 4
...
...
For Example:
chunk_size = 500 tokens
chunk_overlap = 50 tokens
Why Chunk? Because embeddings should represent focused semantic information

If the chunk is too large:
-> unrelated concepts mix together
-> retrieval becomes less precise
-> more tokens send to LLM
-> cost increases

if too small
-> context can be lost
-> incomplete sentences
-> related information gets seperated

**Example**
Suppose your company has a document like this:
Company Leave Policy
Employees receive 20 annual leave days per year.
Employees can apply for leave through the HR portal.
Leave requests must be submitted at least 2 days in advance.
Managers are responsible for approving or rejecting leave requests.
Employees can carry forward up to 5 unused leave days to the next year.
Sick leave is separate from annual leave and provides 10 days per year.

If we use:

chunk_size = 30 tokens
chunk_overlap = 5 tokens

The document might be split roughly like:

Chunk 1:
"Employees receive 20 annual leave days per year.
Employees can apply for leave through the HR portal."
Chunk 2:
"through the HR portal.
Leave requests must be submitted at least 2 days in advance.
Managers are responsible..."

Notice that "through the HR portal" appears in both chunks.

That's the overlap.

Then:
Chunk 3:
"Managers are responsible for approving or rejecting leave requests.
Employees can carry forward up to 5 unused..."

And so on.
Why overlap?
Imagine the important sentence is split exactly at the boundary:

Chunk 1:
"Employees can carry forward up to 5"
Chunk 2:
"unused leave days to the next year."

Without overlap, the meaning is split.

With overlap, we might get:

Chunk 1:
"Employees can carry forward up to 5 unused"


Chunk 2:
"up to 5 unused leave days to the next year."

So the important information appears together in at least one chunk.

And then in RAG

After chunking:

Document
   ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
   ↓
Embedding model
   ↓
Vector for each chunk
   ↓
Vector database

Later, if the user asks:

"How many annual leave days do employees get?"

The query is embedded, and the vector database might retrieve:

Chunk 1:
"Employees receive 20 annual leave days per year..."

That relevant chunk is then given to the LLM, which can answer:

"Employees receive 20 annual leave days per year."

So the key idea is: chunking turns one large document into smaller, meaningful pieces that can be individually embedded and retrieved.

**This is how the chunks are stored in vector database**
Each chunk is converted into one vector, not each word individually into 1, 2, 3, 4.

For example, imagine we have:

Chunk 1:
"Employees receive 20 annual leave days per year."

The embedding model takes that entire chunk and produces something like:

Chunk 1
   ↓
Embedding Model
   ↓
[0.21, -0.73, 0.45, 0.11, ...]

That entire list of numbers is the vector embedding for Chunk 1.

Then:

Chunk 2
   ↓
Embedding Model
   ↓
[-0.18, 0.62, 0.31, -0.44, ...]

And Chunk 3 gets its own vector, Chunk 4 gets its own vector, and so on.

So the Vector Database roughly stores:

┌─────────────────────────────────────────────┐
│ Original Chunk                              │
│ "Employees receive 20 annual leave days..." │
│                                             │
│ Vector                                      │
│ [0.21, -0.73, 0.45, 0.11, ...]             │
└─────────────────────────────────────────────┘


┌─────────────────────────────────────────────┐
│ Original Chunk                              │
│ "Employees can apply through HR portal..."  │
│                                             │
│ Vector                                      │
│ [-0.18, 0.62, 0.31, -0.44, ...]             │
└─────────────────────────────────────────────┘
One very important thing

The numbers don't mean:

0.21 = Employees
-0.73 = receive
0.45 = 20

No. ❌

The whole vector together represents the semantic meaning of the chunk.

So think:

Chunk → Embedding Model → One vector representing that chunk → Vector Database

And yes, the vector database normally keeps the vector along with the original chunk/text and metadata, so when a search finds that vector, it can give you the actual chunk back.

That's the key connection.

**The embedding model does NOT look at your vector database when generating the query vector.**

Think of it as two separate steps.

1. Embedding model creates the vector

You give it:
"How many leaves do we have per year?"
The embedding model processes the meaning of that sentence and produces a vector:
[0.19, -0.70, 0.48, 0.09, ...]
It does this without looking at your company's vector database.
So yes, you can think of the embedding model as having a consistent mapping of meaning → numbers.
For example, conceptually:
"How many leaves do we have per year?"
             ↓
       Embedding Model
             ↓
[0.19, -0.70, 0.48, 0.09, ...]

Your document chunk was previously processed by the same embedding model:
"Employees receive 20 annual leave days per year."
             ↓
       Embedding Model
             ↓
[0.21, -0.73, 0.45, 0.11, ...]

Notice that both vectors end up in a similar region because the meaning is related.

2. THEN the vector database gets involved

Only after the query vector has been created:

User question
      ↓
Embedding Model
      ↓
Query Vector
      ↓
Vector Database

Now the vector database says:

"Okay, I have this query vector. Let me compare it with all the vectors I have stored."

For example:

Query:
[0.19, -0.70, 0.48, 0.09]

Stored vectors:
Chunk 1 → [0.21, -0.73, 0.45, 0.11]  ← very similar
Chunk 2 → [0.80,  0.12, -0.33, 0.71]  ← not similar
Chunk 3 → [0.18, -0.69, 0.50, 0.10]  ← very similar

The vector database calculates a **similarity score** between the query vector and stored vectors.

Then it returns the most similar chunks.

The important distinction

Think of it like this:

Embedding Model = creates the coordinates
Vector Database = searches the coordinates

For example, imagine a map.

The embedding model takes:
"How many leaves do we have per year?"

and says:

"I'll represent this meaning as location (0.19, -0.70, 0.48...)."

Then the vector database says:

"Let me look at all the locations I have stored and find the ones closest to (0.19, -0.70, 0.48...)."

That's why the embedding model doesn't need to know what's inside your company's database.

It simply converts text into a consistent numerical representation.

And then the vector database performs the comparison.

So the actual flow is:

                    ┌─────────────────┐
                    │ Embedding Model │
                    └────────┬────────┘
                             │
                    creates vector
                             │
User Question ───────────────┤
                             ↓
                    [query vector]
                             │
                             ↓
                  ┌────────────────────┐
                  │   Vector Database  │
                  │                    │
                  │ Compare with stored│
                  │      vectors       │
                  └─────────┬──────────┘
                            ↓
                    Similar chunks
                            ↓
                           LLM
                            ↓
                      Final Answer

One subtle but very important point: the numbers aren't universal in the sense that 0.19 always means "leave." The whole vector represents the meaning, and the embedding model has learned to place semantically related texts near each other in that vector space.

# What is chunk overlap
Suppose 
chunk 1:tokens 1-500
chunk 2:tokens 450-950

There are 50 overlapping tokens
why?
Imagine an important paragraph starts at token 480

without overlap:
Chunk 1-> first half
Chunk 2-> second half
The meaning may be broken
Overlap presreves semantic continuity

**Chunk overlap prevents important contextual information from being lost at chunk boundaries.For example, with a 500-token chunk and a 50-token overlap, the last 50 tokens of one chunk are included at the beginning of the next chunk**

# Chunking strategies
1. Fixed-size chunking:Every 500 tokens.Simple and fast

2. Recursive chunking:Attemps to split based on paragraph,sentence,words,characters while respecting a maximum size 
LangChain example concept: RecursiveCharacterTextSplitter

3. Semantic chunking;Breaks documents when semantic meaning changes.
For example:
Topic: Employee Benifits
Topic: Leave Policy
Topic: Remote work
each can become its own chunk

4. Document-structure chunking:Uses Title, Heading, Subheading, Paragraph
very useful for enterprise PDFs/documentation

# How do you choose chunk size
There isn't one universal chunk size.I decide based on document structure, embedding model constarints, retrieval quality and LLM context window

I would start sith something like 300-800 tokens, use an overlap of around 10-20%, and then evaluate retrieval quality using a represntative question dataset.

For structured documentation, I prefer semantic or heading-aware chunking over blindly splitting by characters.

# What are Embeddings
Embedding converst text inti a numerical vector
Example: "How can I reset my password"
might become:[0.12, -0.31, 0.88, 0.14, ...]
Could be hundreds or thousands of dimesnions.
The important property: Semantically similar sentences have vectors that are close together
Example:
How do I reset my password?
and
I forgot my password. How can I change it?
have similar embeddings.
But:
What is the weather today?
would have a very different embedding.

# Embedding Model
Possible embeddings systems include:
1. Amazon titan embeddings
2. OpenAI embeddings
3. Cohere embeddings
4. Sentance Transformers
Focus on Amazon Bedrock/Titan because my resume alligns with aws
Example: Document chunks -> Amazon Titan Embeddings -> Vectors -> OpenSearch Serverless

# What is vector database
A vector database stores embeddings and performs similarity search
Examle: OpenSearch, Pinecone, FAISS, Chroma, Weaviate, Milvus, pgvector

**OpenSeacrh Serverless**
Example stored object:
{
  "text": "Employees receive 24 days annual leave.",
  "embedding": [0.22, -0.71, 0.18],
  "metadata": {
    "source": "hr_policy.pdf",
    "page": 12,
    "department": "HR"
  }
}

# How Vector Search Works
User: How many annual leaves do employees get
Covert query into embedding: query -> embedding model -> query vectors
Compare it against document vector and the nearest vectors are returned
Query vector
     ↓
Vector DB
Chunk A similarity = 0.92
Chunk B similarity = 0.85
Chunk C similarity = 0.73
Chunk D similarity = 0.35

We might retrieve:Top-K = 3

# Cosine Similarity: cosine similarity means the angle between two vectors
Formula: cousine similarity = (A.B)/(||A||*||B||)
Don't derive it mathematically unless they ask
Understand:
1 -> extremely similar
0 -> unrelated
-1 -> opposite direction
**Cosine similarity compares the direction of two vectors rather than their magnitude.In RAG systems, it helps determine how semantically similar the query embedding is to stored document embeddings**

# Top-K
Suppose top_k=5 it means retrive the five most relevent chunks
Problem with Top-k too high:
1. irrelevent context
2. more tokens
3. more cost
4. possible LLM confusion
Too low: important context may be missed
there fore it is tuned experimentally

# Metadata Filtering
Suppose documents are stored for:

HR
Finance
Engineering
Marketing

A Finance user asks:

What was Q4 revenue?

Instead of searching every document:

filter = {
    "department": "finance"
}

Then vector search occurs only inside Finance documents.

Can also filter using:

user_id
tenant_id
department
document_type
date
region
access_level

This also helps security.

# Hybrich search
**Vector search is semantic**
**Keyword search is lexical**
Example: Honda model HN-X5724 (An exact product ID might work better through keyword search.)
Semantic query:vehicles with transmission problems(works better through embeddings)
Hybrid search combines: Vector search + BM25 Keyword Search
Then combine/ranks results
**Hybrid retrieval combines semantic vector search with lexical search such as BM25. Vector search is good for conceptual similarity, while lexical search performs well for exact identifiers, names and domain terminology**

# Reranking
Initial vector search
100,000 chunks -> retrive top 20 -> reranker -> best 5 chunks -> LLM
Why? Vector similarity isn't always perfect
A reranker can evaluate query-document relevance more accurately
This generally improves retrieval quality

# Prompt Construction
After retrieving chunks:

Context:
Employees receive 24 annual leave days.
Unused leaves can be carried forward...

Question:
How many annual leaves do employees receive?

Prompt:

You are an HR assistant.

Answer the question only using the provided context.

If the answer cannot be found in the context,
say you do not have enough information.

Context:
{retrieved_context}

Question:
{user_question}

Send that to the LLM.

# What is prompt engineering
Prompt engineering means designing prompts so that LLM performs reliably
You can control : persona, instructions, context, restrictions, output format, examples, tool usage
Example:
You are a financial assistant.
Use only the supplied company documents.
Do not invent numbers.

Return:
{
 "answer": "",
 "source": ""
}

# Prompt Roles
Typically:
System Prompt
User Prompt
Assistant Messages
Tool Messages

System:
You are an enterprise financial assistant.
Use only provided context.

User:
What was Q4 revenue?

Tool result:
Q4 revenue was $8.4 million.

Assistant:
Q4 revenue was $8.4 million.

# Temperature
**What is temeprature: Temperature controls randomness.**
Temperature=0 More deterministic.
Useful for : enterprise Q&A, RAG, extraction, structured output

Higher: 0.7 - 1 means more creative. This is useful for content generation and brainstroming
For enterprise RAG: 0-0.3 is commonly preferred

# RAG Hallunication
Can RAG completely eliminate hallucination?
Correct answer: No, RAG reduces hallucination but doesn't eliminate it
Hallucination can still happen because:
1. wrong document retrived
2. insufficient context
3. conflicting documents
4. bad prompt
5. stale documnets
Solution:
better retrieval
reranking
metadata filters
strong prompts
similarity thresholds
citations
evaluation
fallback responses
For example:
If similarity < threshold:
    return "I couldn't find reliable information."

# What is Functiona Calling/Tool Calling?
Suppose the user asks: What is the order status for order 123?
That information isn't in RAG documents.
The model can call: get_order_status(order_id="123")
Tool returns:
{
    "status":"shipped"
}
LLM:Order 123 is shipped
**Architecture**
User -> LLM -> Decides tool required -> Tool/function -> REST API/DB/enterprise system -> Tool Output -> LLM -> Response

# RAG vs Tool Calling
Very Importrant
1. Use RAG for: unstructured knowledge, PDFs, documentation, policies, manuals, knowledge base
2. Use tool calling for: live database information, APIs, transactions, weather, order status, creating tickets, sending emails, executing operations

Example:"What us our leave policy"? Ans: -> use RAG
Example:"How many leaves do I currently have?" aNS: -> HR API tool call
Excellent interview distinction

# Agent vs RAG
1. RAG: Retrive -> Generate
2. Agent
Understand Task -> Decide action -> Calls tools -> Observe results -> Possibly call more tools -> Answer
**RAG can be one tool inside an agent**
Example:
**Agent**
1. Search knowledge base
2. Get customer data
3. Query databse
4. Call forecasting model
5. send notification




