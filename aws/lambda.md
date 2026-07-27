# What is AWS lambda ?
AWS lambda is a serverless compute service that runs your code without managing servers

Instead of provisioning EC2 instances:
Upload Code -> Lambda -> Trigeered by Event -> Executes -> Returns Results

You pay only for execution time.

# Lambda Architecture ?
Client -> API Gateway -> Lambda -> Dynamo -> S3
OR
S3 Upload -> Lambda Trigeer -> Image Processing

# Lambda Lifecycle ?
A lambda execution environmet goes through theree phases
Request -> Container Creation -> Runtime Initilaization -> Load your code -> Execute Handler -> Freeze Container -> Reuse Container
If AWS reuses container: No cold start
otherwise              : Cold start

# Cold Start
Cold Start occurs when the lambda needs to create a new execution environment 
AWS must:
-> Allocate container
-> Start runtime
-> Dowload code
-> Load Dependencies
-> Initialize variables
-> Execute handler
Example:
User Request -> No Existing Container -> Create Container -> Initialize Runtime -> Run code
This initialization time is called Cold Start

# Warm Start
If AWS already has a container 
Request -> Existing Container -> Execute Immediately
No initialization

Why Cold Starts happen
-> First invocation
-> Scaling up
-> Container expired
-> New deployment
-> Version change

# How to reduce cold start
1. Increase Memory:more memory gives more cpu
Higher CPU = faster initialization
2. Keep Package Small
Avoid:Huge libraries, Unused dependencies, Large layers
3. Provisioned Concurrency:AWS keeps containers warm
without provisioned concurrency
Request -> create container -> run
with provisioned concurrency
Request -> Already Running -> Run
4. Avoid Huge Initialization
Bad
import pandas
import tensorflow
import torch
Good
Load only what's needed
5. Use Newer Runtimes:Python 3.12 initializes faster than older versions in many cases.

# Execution Environment
Each lambda execution environment contains
-> Runtime
-> Your code
-> Environment variables
-> Temporary storage
-> Memory
-> CPU

# Stateless Nature
Lambda is stateless, Never assume previous execution data exists
Bad: counter+=1
Good: Store data in Dynamo DB,Redis, S3, RDS

# Execution Context Reuse
Global variables survive if the container is reused
Example:
import boto3
client = boto3.client("s3")
The client is created only once
Next invocation reuses it
Interview Question:Why initialize boto3 outside handler?
Answer:To reuse connections and reduce latency.

# Memory
Configurable:128MB to 10,240MB(10GB)
Interview question: Does lambda CPU increase with memory?
Answer: Yes

# Timeout
Maximum: 15 minutes if exceeded Task timed out

# Ephemeral Storage
Default 512MB can increase up to 10 GB
Location: /tmp
Useful for
-> PDF generation
-> Video processing
-> Temporary files

# Environment Variables
Store DB_HOST, API_KEY, BUCEKT_NAME
never hardcode secrets
Use: Secrets Manager or Parameter Store

# Lambda Layers
Reusable libraries
Example: Layer -> numpy pandas requests
Multiple Lambdas can share maximum 5 layers.

# Lambda Versions
Each pusblish creates immutable version
Version 1 -> Version 2 -> Version 3
Cannot modify

# Aliases
dev qa prod
Example
prod -> Version 10
dev -> Version 15
Useful for deployments

# Reserved Concurrency
Limits one Lambda
Example: Account limit 1000 Function A 200 remaining 800
Gurantees Function A always has capacity

# Provisioned Concurrency
Pre-warmed containers
No cold start
Good for APIs, Banking, Healthcare

# Account Concurrency
Default 1000 concurrent executions (can be increased by requesting q quota increase)

# Concurrency
Suppose -> 100 Requests Execution Time 2 seconds
Concurrency -> 100
Because 100 functions run simultaneously
Formuls: Concurrency=Requests per sec * Duration
Example: 50 requests per sec and duration is 4 sec then concurrency is 200 

# Throttling
If concurrency limit exceeded
Request -> Limit Reached -> Throttle
For synchronous calls
429
Too Many Requests

# Event Sources
Lambda supports many triggers

Synchronous
-> API Gateway
-> ALB
-> Lambda URL
client waits

Asynchronous
-> S3
-> EventBridge
-> SNS
AWS retries automatically

Poll-based
-> SQS
-> Kinesis
-> DynamoDB Stream
Lambda polls

# Retry Behavior
s3 -> 2 tries
sns -> 2 retries
SQS -> Until message visibility timeout/ retyr policy exhausted(or it reaches the DLQ if configured)

# Dead Letter Queue(DLQ)
failed events go to
SQS or SNS
Useful for debugging

# Event Source Mapping
Lambda continously polls
SQS -> Lambda -> Delete Message

# Batch Size
SQS 1 to 10,000
Kinesis 1 to 10,000
Large batches reduce invocation count but increase processing time and failure impact.

# Visiility Timeout
For SQS
Message -> Lambda -> Processing -> Delete
If processing fails.Message become visible again
Best Practice: Visibikity timeout should be greater then lambda timeout

# IAM Security
Never use AdministratorAccess
Minimum permission
Example: Lambda -> S3 Read -> Only Bucket A
Least privilege

# Execution Role
Lambda assumes IAM Role
Example:Lambda -> IAM Role -> S3 -> DynamoDB

# Resource-Based Policy
ALlows other AWS services/accounts to invoke Lambda
Example: API Gateway -> Invoke Lambda

# VPC
Normally Lambda runs outside your vpc
Need RDS?
Attach Lambda to VPC
Lambda -> Private Subnet -> RDS
Need a NAT Gateway if Lambda in a private subnet requires internet access

# Security Groups 
When lambda is inside VPC Attach Security Group

# Monitoring
CloudWatch Metrics
Important Metrics
-> Invocations
-> Errors
-> Duration
-> Throttle
-> Concurrent Executions
-> Iterator Age(for stream-based sources)

# X-Ray
Trace requests
Find slow functions

# Why use Lambda ?
-> No server management
-> Auto Scaling
-> Pay per use
-> High Availability

# When not to use Lambda?
-> Long-running tasks(>15 minutes)
-> Large in-memory workloads
-> Applications requiring persistent state
-> Predictable, constant heavy workloads where EC2/ECS may be more cost-effective

# Differene between Reserved and Provisioned concurrency
-> Reserved concurrency limits maximum concurrency for that function.Does not elimate cold start
-> Provisioned concurrency keeps execution environments initialized, eliminates most cold starts and costs extra

# Why initialize boto3 outside handler?
Reuses execution context, Faster execution

# Difference between lambda and EC2 
Lambda                          Ec2
Serverless                      Manges Server
Auto Scaling.                   Manual/Auto Scaling Groups
Max 15 min                      No execution limit
Pay per request and duration    Pay while instance runs
Event-driven                    Always Available

# What happens if Lambda exceeds timeout
AWS terminates the execution and records a timeout error in CloudWatch Logs. Any in-progress work that isn't idempotent may need retries or compenastion logic.

# What is Cold Start?
Intialization time when AWS creates a new execution environment before running your code.

# What is Event Source Mapping
A configuration that tells lambda how to poll services like SQS, Kinesis, or DynamoDB streams and invoke your function with batches of records.