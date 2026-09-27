# Finconecta
Finconencta was an enterprise GenAI platform deployed on AWS. The application used a RAG-style architecture so that LLM could answer questions using enterprise-specific information rather than relying only on the model's pretrained knowledge. My work was mainly on the AWS infrastructure, backend integration, deployment and supporting services.We used services such as Amazon Bedrock, S3, OpenSearch Serverless, DynamoDB, EventBridge, Kinesis, Lambda, ECR, and AWS Batch.

# End-to-end architecture
1. Enterprise data
Documents -> Amazon s3 -> Bedrock Knowledge base -> Document parsing -> Chunking -> Titan Embedding Model -> Vector embeddings -> OpenSearch Serverless Vector Index
2. USER Query
User -> Application/API -> Backend / GenAI Service -> Bedrock Knowledge base -> Query embedding created -> OpenSearch serverless -> similarity retrieval -> Relevant text chunks -> Foundation model -> Gnerated response -> Application

This is exactly how Bedrock Knowledge Bases are designed to support RAG:a source as S3 holds raw documents, those documents are converted into chunks and embeddings, embeddings are stored in a vector store such as OpenSearch Serverless, and relevant chunks are retrieved when a query arrives.

# s3- what exactly was its responsibility?
S3 should be thought of as the raw knowledge/data layer.
Don't say: "we stored vectores in s3"
Say
**We used s3 as the source location for the enterprise knowledge documents that needed to be indexed by the RAG system**
conceptually it looked like
s3://finconecta-knowledge-base/

    products/
        product_a.pdf
        product_b.pdf

    financial-data/
        report_2024.pdf

    documentation/
        services.pdf
        policies.pdf

**The s3 bucket contained the source or enterprise data that the knowledge base needed to ingest**
The Amazon Bedrock Knowledge Bases can directly connect to an S3 bucket as its data source. S3 contains the raw documents; Bedrock processes those documents into the representation required for retrieval

# Why S3
Because s3 gives us:
1. Durable object storage
2. High Scalability
3. IAM access control
4. Encryption
5. Versioning capability
6. Easy integration with bedrock
7. Event-based integration
8. Low-cost document storage

# What happens after a file enters s3?
Suppose this document exists: financial_product_guide.pdf
Inside:
Product: Business Credit Facility

Eligibility:
Annual turnover greater than...

Interest:
...

Required documents:
...

-> Bedrock Knowledge Base sees s3 as its data source
Now the ingestion process conceptually becomes
s3 document -> Read/extract document contents -> Split into chunks -> Vectors -> Opensearch Index
**AWS describes Bedrock Knowledge Bases as taking source data, chunking it, creating vector embeddings, and storing those embeddings in a connected vector database.**

# Chunking in finconecta architecture
Imagine a PDF contains 100 
We don't create one embedding for the entire PDF.

Instead:

Document

"FinConecta product..."
"Eligibility..."
"Pricing..."
"Risk..."
"Terms..."

becomes:

Chunk 1
Chunk 2
Chunk 3
Chunk 4
...

For example:

Chunk 47:

"The XYZ financial product is available to organizations
with annual revenue greater than..."

Each chunk becomes independently retrievable.

Why?

Because when the user asks:

What are the eligibility criteria for XYZ?

we don't need all 100 pages.

We want the most relevant chunks.

# Titan Embeddings - what exactly was happening?
The embedding model converts text into numbers
For example: "XYZ product requires minimum annual revenue of $5 million"
becomes something conceptually like: 
[
  0.023,
 -0.183,
  0.772,
  0.401,
 ...
]
this array is vector
**The embedding model does not generate an answer. Its job is to convert the document content into numerical representations that capture semantic meanings**
Amazon Bedrock Knowledge Bases requires an embedding model to convert source information into vector embeddings for vector-store retrieval.

# Why embeddings instead of normal keyword matching?
Suppose the source document says: "The customer may terminate the agrement"
User asks: "Can I cancel the contarct"
Tradition exact keyword search: terminate != cancel and it can struggle
Embedding search understand that:
terminate, cancel, end agrement, close contract all this can carry similar semantic meaning.
So embeddings let us do semantic search

# OpenSeacrh Serverless - what exactly did we store there?
This is critical
s3: Stores original source documents
OpenSearch: Stores searchable representation of those documents
Conceptually:
{
  "text": "The customer is eligible if annual revenue exceeds...",
  "embedding": [
    0.02,
    -0.19,
    0.72
  ],
  "metadata": {
    "source": "financial_product.pdf",
    "page": 12
  }
}
So OpenSearch contains something like:
Chunk -> Embeddin vector -> Metadata
**OpenSearch Serverless provides vector-search collection for storing embeddings and performing similarity search using k-nearest-neighbor functionality. It supports vector similarity measure including cosine similarity, Euclidean distance and dot product.**

# OpenSearch terminology
1. Collection: In OpenSearch Serverless: Collection is the logical grouping containing one or more indexes
-> For RAG, we use a: Vector Search Collection AWS manages underlying search infrastructure for us.
2. Index: Inside the collection: knowledge-index, might conceptually contain:
document_id, text, vector, metadata
Example:
{
  "document_id": "doc-200-chunk-14",
  "text": "Minimum account balance is...",
  "embedding": [...],
  "source": "account_policy.pdf"
}

# Why OpenSearch Serverless?
**We used OpenSearch Serverless because we need scalable semantic/vector search without managing OpenSearch cluster ourselves**
Advantages:
No manual cluster provisioning
Automatic scaling
Vector search
k-NN search
Metadata filtering
Integration with Bedrock Knowledge Bases
Serverless infrastructure
Supports semantic search
**AWS explicitly positions vector-search collections for GenAI applications, chatbots and semantic search**

# Now user asks a question — what happens?

Suppose:
User:
Which financial product is suitable for a customer
looking for X?

The application sends that query to the backend.

Architecture:

Frontend
   ↓
API/backend
   ↓
Bedrock Knowledge Base

Now query-time RAG starts.

# Query embedding
The Query: Which product is suitable for x?
it is now converted into a vector
Conceptually:
User Questions -> Embedding model -> [0.21,-0.17,0.63,..]
Important:Document embeddings and query embeddings should use the same compatible embedding space
Otherwise similar comaparison becomes meaningless.

# OpenSearch similarity search
Now we have: query_vector, OpenSearch compares it against stored document vectors
Example:
Query embedding -> OpejnSearch
chunk 17 -> 0.93 similarity
Chunk 81 → 0.88
Chunk 42 → 0.82
Chunk 10 → 0.54
Chunk 77 → 0.23
Then retrive: Top 3 or Top 5
depending on configuration.
OpenSearch vector collections use k-NN search to find similar vector efficiently.

# What gets returned from OpenSearch
Not Simply this: 0.93
We want the actual original chunk
For Example:
Chunk 17:
"Product A provides working capital funding for..."

Chunk 81:
"Product A eligibility criteria include..."

Chunk 42:
"Product B is intended for..."

Those become the context to LLM

# Bedrock's role here
Amazon Bedrock can be involved in multiple different roles
1. Role-1 -> embeddings
Text -> Embedding Model -> vector
2. Role-2: -> RAG orchestration
Bedrock knowledge Bases manages: data source, chunking, embedding, vector retrieval
3. Role-3: -> generation
Foundation model generates the natural-language answer
For Example: Claude, Nova, etc through bedrock

**Bedrock Knowledge Bases exposes both Retrieve and RetrieveAndGenerate. Retrieve returns relevent source chunks; RetrieveAndGenerate combines retrieval with a model call to produce the answer and can return citations.**

# Retrieve and RetrieveAndGenerate
Retrieve
Question
 ↓
Knowledge Base
 ↓
Relevant chunks

Application controls what happens next.

For example:

chunks = retrieve(question)

prompt = create_prompt(chunks, question)

answer = call_model(prompt)

More control.

RetrieveAndGenerate

Bedrock does:

question
 ↓
retrieve
 ↓
augment prompt
 ↓
invoke model
 ↓
generate answer

for you.

Conceptually:

response = bedrock.retrieve_and_generate(...)

AWS describes RetrieveAndGenerate as combining retrieval with model invocation to perform the RAG workflow.

# Prompt augmentation
Suppose retrived context is 
Context 1:Product A provides...
Context 2:Eligibility requires...
Context 3:For customers with...

-> Then the model gets something conceptually likr:

System:
You are an assistant for financial institutions.
Use the supplied context to answer the user's question.
Do not invent information.

CONTEXT:
Product A provides...
Eligibility requires...
For customers...

QUESTION:
Which financial product should I select?

The LLM now has enterprise information that wasn't necessarily part of ots training data

That's the Augmented part of: Retrieval-Augmented Generation

# Then Bedrock foundation model generates response
The model could produce:

Based on the available product information,
Product A appears most relevant because...

And ideally citations can identify:

financial_product.pdf
page 12

Bedrock's RetrieveAndGenerate flow can return citations associated with the source chunks.

# DynamoDB
DynamoDB was part of the supporting application infrastructure, while the actual vectorized knowledge used for semantic retrival was handled through OpenSearch Serverless

**We stored all chat sessions in DynamoDB.**

# What DynamoDB would normally hold in this type of architecture
DynamoDB might hold application-level information such as:
conversation metadata
request status
processing state
job metadata
user/session references
model execution information
application configuration
workflow state
Example:
{
  "request_id": "REQ10028",
  "user_id": "USER11",
  "status": "COMPLETED",
  "created_at": "...",
  "model": "...",
  "result_reference": "..."
}

But again:

OpenSearch = vector retrieval
DynamoDB = application/state/metadata if needed
Do not mix them.

# S3 vs DynamoDB vs OpenSearch
| Service                   | Primary role                                                                      |
| ------------------------- | --------------------------------------------------------------------------------- |
| **S3**                    | Original/raw enterprise documents                                                 |
| **OpenSearch Serverless** | Embeddings, searchable chunks and metadata for semantic retrieval                 |
| **DynamoDB**              | Application/state/metadata where required                                         |
| **Bedrock**               | Embeddings, knowledge-base retrieval/orchestration and foundation-model inference |

# What was Lambda doing?
Lambda supporting in 
API processing
data processing
workflow triggers
event consumers
service integration
**Lambda was part of the supporting serverless infrastructure for backend and integration workflows**







