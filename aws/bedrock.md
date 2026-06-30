# Amazon Bedrock
Amazon Bedrock is a fully managed AWS service that provides access to multiple foundation models(FMs) from AWS and third-party providers through a single API.It allows developers to build Generative AI applications without managing infrastructure or training models.

It is a 
-> Fully Managed
-> Foundation Models
-> Single API
-> No infrastructure management

Why was Bedrock introduced?
Before Bedrock, if you want to use a LLM, you had to:
1.Choose a model
2.Host the model
3.Manage GPUs
4.Scale servers
5.Handle model updates

example: application -> ec2 -> gpu -> llama model
here you are responsible for everything

with bedrock
your application -> amazon bedrock -> claude,llama,titan,nova,mistral,cohere,AI21

AWS Managed:
-> Infrastructure
-> GPUs
-> Scaling
-> Availability
-> Updates
You only sends prompts and recive response

# What are Foundation Model(FMs)
A foundation model is a large pre-trained AI model
example: Claude,Llama,Amazon Titan,Nova, Mistral,Cohera,AI21
These models are trained on massive datasets and can perform
-> Text Generation
-> Summarization
-> Translation
-> Coding
-> Question answering
-> Chatbots
-> Image Generation
-> Embeddings

# Bedrock Architecture
Client(web/mobile) -> API Gateway -> Lambda(python) -> Amazon Bedrock -> Calude 3.5 Sonnet or Nova Pro or llama 3 -> Generated response -> lambda -> user

# What models are available in Bedrock?
Amazon Models
-> Titan Text
-> Titan Embeddings
-> Nova Lite
-> Nova Pro
-> Nova Premier
Anthropic Models
-> Claude 3 Haiku
-> Calude 3 Sonnet
-> Claude 3 Opus
-> Claude 3.5 Sonet
-> Clude 4(depending on region availability)
Meta
-> Llama 3
-> Llama 4
Cohere
-> Command
-> Command R
-> Embed
AI21
-> Jurassic
-> Jamba
Mistral
-> Mistral Large
-> Mixtral

# Interview Question
# Why bedrock instead of ChatGPT API?
Bedrock Provides
-> Security through AWS IAM
-> Cloudwatch Monitoring
-> Enterprise compliance
-> Multiple models through one API
-> Easy integration with AWS services
you don't need different SDKs for each model

# Main Bedrock features
1.Text Generation
2.Chat
3.Summarization
4.Question Answering
5.Translation
6.Code Generation
7.Image Generation
8.Embedding(very import):instead of generating text, AI converts text into vectors.
example:python -> [0.23,0.18,0.15,..]
Embeddings are used for
-> Semantic Search
-> Recommendations
-> RAG
-> Similarity Search

# Bedrock Components

1.Model Access: First enable the model
console -> Bedrock -> Model Access -> Request Access
only after approval we can use it

2.Playground: AWS provides a playground, where we can test prompts like ChatGPT. No coding required

3.Knowledge Bases:(very important) suppose company has
-> PDFs
-> Word files
-> Excel
-> Policies
Bedrock can connect to them
Architecture: pdf -> s3 -> Knowledge Base -> Vector Database -> Bedrock -> Answer
Example:If employee asks
what is our leave policy?
Bedrock searches company doucment first then answer

4.Guardrails:(Very Important)
Guardrails prevent harmful outputs.
Example:
Don't answer
-> Violence
-> Hate speech
-> Sensitive data
-> Personal information
Guardrails filter prompts and responses

5.Agent:Agent can perform actions
Example:
User:Book my flight tommorow
Agent: checks calender -> calls calender -> calls lambda -> book tickets -> return confirmation
Unlike a normal model, an agent can interact with external systems 

# How python calls Bedrock
using boto3 library

import boto3
client=boto3.client("bedrock-runtime")
response=client.invoke_model("model name")

Flow:
python -> boto3 -> Bedrock Runtime -> claude -> Response -> Python

# IAM Permissions
Lambda needs permission
Example:bedrock:InvokeModel
without this, you'll get Access Denied

# Bedrock+Lambda
This is common in interviews

client -> API Gateway -> Lambda -> Bedrock -> Lambda -> User

# Bedrock+s3

resume.pdf -> S3 -> Lambda -> External text -> Bedrock -> Summary

# Bedrock+dynamoDB
for storing
Chat History -> DynamoDB Each conversation -> saved -> Displayed later

# Bedrock+OpenSearch
Flow
Documents -> Embedding Model -> Vectors -> OpenSearch -> User Question -> Similarity Search -> Relevent Documents -> Bedrock -> Answer
This is called RAG(Retrival-Argumented-Generation)

# Why OpenSearch?
LLMs only know what they are trained on
Suppose user asks:What is TensorIOT leave policy
Claude doesn't know
Instead OpenSearch finds the relevant company document
Bedrock uses that document.Then answer accurately

# First, understand one important fact

Suppose I ask ChatGPT:

What is TensorIoT's internal leave policy?

It cannot answer because it was not trained on your company's internal documents.

Similarly,

Suppose your client uploads:

Employee Handbook.pdf
HR Policy.docx
Salary.xlsx

Does Bedrock automatically know these documents?

No.

Bedrock has zero knowledge about your company's private files.

So we need to somehow "teach" Bedrock these documents without retraining the model.

This is where RAG (Retrieval-Augmented Generation) comes in.

# Overall Architecture
Client Upload Files(PDF,DOC,EXCEL) -> Amazon s3(Raw documents stored) -> Knowledge Base Sync -> Extarct text from documents -> Split into small chunks -> Generate Embeddings using Bedrock(Titan Embeddings) -> Store Embeddings in Vector Database(OpenSearch Serverless) -> User asks questions -> Generate embedding of question -> Search Vector Database
-> Find Similar chunks -> Sends retrived chunks +User Question -> Claude/Nova -> Final Answer

LLM Never search s3 directly

# Step 1: Client uploads documents

Suppose client uploads

Employee_Handbook.pdf

HRPolicy.pdf

Salary.xlsx

LeavePolicy.docx

Where do we store them?

Usually

Amazon S3

because

cheap
scalable
durable

So S3 becomes

S3

Employee_Handbook.pdf

LeavePolicy.docx

HRPolicy.pdf

Nothing special yet.

# Step 2: Does Bedrock read S3 every time?

No.

Imagine S3 contains

5000 PDFs

Each PDF

200 pages

Suppose every user asks

What is maternity leave?

Should Bedrock read

5000 PDFs

every single time?

Impossible.

Too slow.

Too expensive.

So AWS doesn't do that.

# Step 3: Build a Knowledge Base

Now Bedrock creates a Knowledge Base.

Knowledge Base says

My documents are inside this S3 bucket.

Then it starts processing.

# Step 4: Document Parsing

Suppose PDF contains

Company Leave Policy

Employees receive 24 annual leaves.

Unused leaves expire after one year.

Employees can work remotely.

AWS extracts text.

Now

Raw Text

instead of PDF.

# Step 5: Chunking

This is extremely important.

LLMs don't process huge PDFs efficiently.

Instead

AWS splits them.

Example

Original

100 pages

↓

Chunk 1

Page 1-3

↓

Chunk 2

Page 4-6

↓

Chunk 3

Page 7-10

Every chunk becomes

200-500 words

Approximately.

Now we have many small pieces.

Example

Chunk 1

Annual Leave Policy
Chunk 2

Medical Leave
Chunk 3

Travel Policy

# Step 6: Generate Embeddings

This is the part everyone finds confusing.

Suppose chunk is

Employees receive 24 annual leaves.

Can OpenSearch search plain text?

Yes.

But semantic search is much better.

Instead,

Bedrock converts this sentence into numbers.

Example

Employees receive 24 annual leaves.

↓

[0.234,
-0.817,
0.551,
...
1536 numbers]

These numbers are called

Embedding Vector

Think of it as the AI's mathematical representation of the meaning of the sentence.

Two sentences with similar meanings will have embeddings that are close together in vector space.

For example:

Employees get 24 annual leaves.

and

Workers receive 24 vacation days.

will produce similar embeddings even though the wording is different.

# Where are embeddings stored
Not in dynamoDB
Not in s3 They are stored in Vector Database

Example

OpenSearch Serverless

Pinecone

Redis

Aurora PostgreSQL with pgvector

MongoDB Atlas Vector Search

In AWS,

most companies use

OpenSearch Serverless

# What does the Vector DB store?

Example

Embedding

[0.123,
0.91,
0.55,
...]

↓

Corresponding Text

Employees receive 24 annual leaves.

↓

Document Name

Employee_Handbook.pdf

↓

Page

12

Every chunk has:

embedding
original text
metadata


# How would you implement a chatbot over client PDFs

I would store the raw documents in an s3 bucket. Then I'd configure an Amazon Bedrock knowledge Base pointing to that bucket.During ingestion,Bedrock extracts the document text, splits it into chunks, generate embeddings using an embedding model such as Amazon Titan Embeddings, and stores those embeddings in a vector database like OpenSearch Serverless. When a user asks a question, the system generates am embedding for the question, perform a similarity search in the vector database to retrive the most relevent document chunks, and passes those chunks as context to a foundation model such as Claude or Nova. The model then generates an accurate response grounded in the client's documents instead of relying only on it's pre-trained knowledge.

First understand this

Suppose your documents contain:

Employees receive 24 annual leaves.

During ingestion, Bedrock generates an embedding like this:

"Employees receive 24 annual leaves."

↓

Titan Embeddings Model

↓

[0.12, -0.56, 0.91, 0.33, ...]

This vector is stored in OpenSearch.

Now suppose another document contains:

Employees can work remotely.

Another embedding is generated.

"Employees can work remotely."

↓

[0.91, -0.11, 0.44, ...]

OpenSearch now contains

Vector 1 → Employees receive 24 annual leaves.

Vector 2 → Employees can work remotely.

Vector 3 → Medical insurance policy.

Vector 4 → Salary revision process.

...
Thousands of vectors
Now the user asks
How many vacation days do employees get?

Notice something.

This exact sentence

How many vacation days do employees get?

does not exist inside OpenSearch.

So what do we do?

We generate a new embedding for the user's query.

Question

↓

Titan Embeddings

↓

[0.15, -0.61, 0.88, ...]

So yes,

every new query gets its own embedding generated.

Now your question is

Do we have embeddings already for every word in the world?

No.

This is the biggest misconception.

We are not storing embeddings for every English word.

Instead,

we generate an embedding for the entire input text.

For example

Input

How many vacation days do employees get?

↓

Embedding Model

↓

One vector

[0.12,
0.44,
-0.78,
...
1536 numbers]

Not

How

↓

vector

many

↓

vector

vacation

↓

vector

days

↓

vector

The embedding model looks at the whole sentence and produces one vector representing its meaning.

Then how does similarity work?

Suppose OpenSearch contains

Employees receive 24 annual leaves.

Embedding

[0.13, 0.45, 0.87]

User asks

How many vacation days do employees get?

Embedding

[0.12, 0.46, 0.86]

The vectors are very close.

Although

annual leave

and

vacation days

are different words,

their meanings are similar.

So OpenSearch returns that chunk.

This is called

Semantic Search

instead of

Keyword Search


