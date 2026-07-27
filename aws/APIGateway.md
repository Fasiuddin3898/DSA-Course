# What is API Gateway?
API Gateway is a fully managed service that acts as the front door for your backend services.
It recives requests from clients and forwards them to
-> Lambda
-> EC2
-> ECS
-> EKS
-> HTTP Servers
-> Any REST endpoint
Instead of exposing your lambda directly, users call API Gateway

# Why do we need API Gateway ?
Imagine every lambda had its own URL
Problems
-> No Authentication
-> No Authorization
-> No Rate Limiting
-> No Monitoring
-> No API Versioning
-> No CORS Handling
API Gateway solves all of these

Real Example:Suppose your building a e commerce application
GET/products
POST/orders
GET/orders
DELETE/orders/{id}
client never talks to lambda
Browser -> API Gateway -> Lambda -> DynamoDB

# Components of API Gateway
API gateway consits of 
API -> Resources -> Method -> Integrations -> Backend
Example:
API ShoppingAPI -> Resource /Products -> Method GET -> Integration Lambda -> Lambda Function

# Resource
A resource is simply the URL path
Example: /users /products /orders /login /admin

# Methods
Each resource can have methods
GET POST PUT DELETE PATH OPTIONS
Example: GET/users, POST/users, DELETE/user/10

# Endpoint Types
There are theree endpoint types

1. Edge Optimized:Uses CloudFront automatically
Best for Global users
Example: USA INDIA EUROPE -> Cloud front -> API Gateway
Lowest latency globally

2. Regional: Available only in one AWS Region
Example: Mumbai Region
Best choice for most projects

3. Private: accessible only inside a VPC
Used by
-> Internal Microservices
-> Banking
-> Healthcare

# Types of API Gateway
AWS offers three API styles

1. REST API
older but more Features
Supports
-> API Keys
-> Usage Validations
-> Request Validations
-> Authorizers
-> Mapping Templates
Most interview questions use REST API

2. HTTP API
Newer Cheaper Faster Supports
-> JWT
-> Lambda 
-> OAuth
Missing some REST features.Recommended for new applications

3. WebSocket API
For real time communication
Examples: Chat Apps, Gaming, Stock Market, Notifications

# Request Flow
Let's understand exactly what happens
Browser -> DNS -> API Gateway -> Authentication -> Authorization -> Throttling -> Validations -> Transformation -> Lambda -> Business Logic -> DynamoDB -> Response -> API Gateway -> Client

# Integration Types
1. Lambda Proxy Integration
Most common. Client request goes directly to Lambda 
Browser -> API Gateway -> Lambda
Lambda recives. event, context
Example event
{
 "httpMethod":"GET",
 "path":"/users",
 "headers":{},
 "queryStringParameters":{},
 "body":""
}
2. Non Proxy Integration
API Gateway modifies request before sending
Can map fields. Useful for legacy systems
3. HTTP Integration
calls another HTTP endpoint
Example: API Gateway -> https://backend.company.com
4. AWS Service Integration
API gateway directly calls AWS services
Example:API Gateway -> SQS -> SNS -> Step Functions
No lambda required

# Stages
Stages represent environments
dev qa test prod
Example URL
https://abc.execute-api.amazonaws.com/dev
https://abc.execute-api.amazonaws.com/prod
Each stage can have
-> Variables
-> Logging
-> Throttling