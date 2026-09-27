# What is Amazon API Gateway?
Amazon API Gateway is a managed AWS service used to create, expose, secure, monitor and manage APIs

# Architecture

Frontend/client -> HTTPs -> API Gateway -> Lambda -> Business Logic -> S3/DynamoDB/SQS/SiteWise

API Gateway contains
Authentication
Authorization
Throttling
Validation
Routing
CORS

# API Gateway defination
API Gateway is a managed AWS service that acts as the entry point for backend APIs. It receives HTTP requests from clients, performs functions such as routing, authentication, authorization, throttling and request handling and forwards the request to backend integration such as lambda

# Why we need API Gateway
Suppose you have lambda and you don't want frontend directly invoking lamdba 
so frontend -> api gateway -> lambda
API gateway gives you a proper HTTP iterface
GET /assets
GET /assets/{id}
POST /assets
POST /asset/{id}
DELETE /asset/{id}
It also provides a centralized place for security, throttling, routing, monitoring, CROS, and other API concerns

# REST API design
Imagine we are building an asset service.

Don't design everything like:

/createAsset
/getAsset
/updateAsset
/deleteAsset

A REST-style API would normally be:

POST   /assets
GET    /assets
GET    /assets/{asset_id}
PUT    /assets/{asset_id}
DELETE /assets/{asset_id}

HTTP method represents the action.

Important methods
Method	         Purpose	    Example
GET	             Retrieve	    GET /assets/123
POST	         Create	        POST /assets
PUT	             Full update	PUT /assets/123
PATCH	         Partial update	PATCH /assets/123
DELETE	         Delete	        DELETE /assets/123

# What happens when an API request arrives
Suppose: GET/v1/assets/123
Conceptually:
client -> DNS -> HTTPS -> API Gateway -> Route Matching -> Authentication / Authorization -> Throttling -> Request handling -> Lambda -> Business Logic -> DynamoDB -> Lambda Response -> API Gateway -> Client

Your Lambda may receive information such as:
{
  "pathParameters": {
    "asset_id": "123"
  }
}
Then Python can read it:
asset_id = event["pathParameters"]["asset_id"]

# Path parameters vs query parameters
1. Path Parameters: Used to identify a specific resource
Example: GET /assets/123
Here:123=asset_id
Route:GET/asset/{asset_id}
2. Query parameters: Used for filtering, sorting, pagination etc
Example: GET/ asset?status=ACTIVE&limit=20
Here: status=ACTIVE and limit=20

# API Gateway + Lambda integration
POST/asset -> API Gateway -> Lambda -> DynamoDB
Example request:
{
    "asset_name": "Machine-101",
    "model_id": "MODEL-01"
}
Lambda performs:
1. Parse request
2. Validate input
3. Check authorization if applicable
4. Execute business logic
5. Access database/service
6. Build response
Response:
{
    "asset_id": "12345",
    "asset_name": "Machine-101",
    "status": "CREATED"
}
HTTP:
201 Created

# HTTP status code
1. Success
200 OK
201 created
202 Accepted
204 No content
For example:
POST /bulk-assets
       ↓
SQS
       ↓
Processing happens later
You could return:
202 Accepted
because the request has been accepted but processing isn't necessarily complete.
2. Client Errors
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
429 To many requests
**important**
401:Unauthorized:You are not successfully authenticated
403:forbidden:We know who you are and you don't have permission to access this particular service
3. Server errors
500 Internal server error
502 Bad Gateway
503 service unavaibale 
504 Gateway timeout

# API Versioning **(very important)**
Imaging your current api is GET/v1/assets/{id}
{
    "name":"Machine-abd",
    "id":123
}
and many frontend/client applications already depend on this 
Now business requirement changes significantly
You want
{
    "asset_name":"Machine-abd",
    "asset_id":123,
    "asset_status":"active",
    "metadata":[]
}
if you change v1, existing clients could break
instead:
    v1/assets/{id} -> existing behavious
    v2/assets/{id} -> new behavious
This is called API versioning
**Defination:API versioning allow us to introduce breaking changes to an API while maintaining backward compatibility for existing customers**

# When should you create V2
Suppose:Bug fix,Performance improvement,Internal refactoring
Usually:No new API versio

But:Breaking request structure,Breaking response structure,Major behavioral change,Removing existing fields,Changing field meaning/type
may justify:V2

Excellent interview statement:
**“I wouldn't create a new version for every change. I would mainly version an API when the change breaks the existing contract.”**

# API versioning strategies
1. URL/path versioning
/api/v1/assets
/api/v2/assets
2. Header versioning
GET/ assets
Accept-Version: v2
URL stays clean, but version selection is less visible
3. Query parameter versioning
GET / assets?version=v2

For interviews, path versioning is easiest to explain:
/v1/assets
/v2/assets

# Authentication vs Authorization
1. Authentication:Who are you ?
User -> Login -> Token -> API Request
2. Authorization: What are you allowed to do?
Normal User
GET /assets       ✅
DELETE /assets    ❌

Admin
GET /assets       ✅
DELETE /assets    ✅

API gateway can work with mechanisms such as JWT authorizers, Lambda authorizers, Cognito-based architecture and IAM authorization depending on the API type/design.


# JWT flow
understand the concept
User -> Login -> Identity Provider(AWS Cognito) -> JWT access token -> Frontend
Frontend -> Authorization: Bearer <token> -> API Gateway -> validate token 
-> Valid?
 ├── NO → reject
 └── YES
       ↓
     Lambda

# API rate limiting/throttling
Suppose one client starts sending huge traffic
Client -> 10,000 request/sec -> API Gateway -> Lambda -> Database
That could overload downstream systems or increase costs
Throttling helps control traffic
Two concepts to know
1. Rate: Sustained request rate
Example: 100 requests/second
2. Brust: Temporary spike allowed above normal sustained traffic
when applicable limits are exceeded, clients can receive
429 Too Many Requests
Client applications should generally use retyr startegies such as exponential backoff with jitter, rather than immediately hammering the API again

# What is exponential backoff?
Instead of 
Request failed -> retry immediately -> retry immediately -> retry immediately
Do:
Request Failed -> wait -> Retry -> wait longer -> retry
For example conceptually:
1 sec -> 2 sec -> 4 sec -> 8 sec
Usually add some randomness - jitter - so thousands of clients don't all retyr at exactly the same moment

# CORS ***
Very common frontend/backend
Suppose 
Frontend: https://app.company.com
API: https://api.company.com
These are different regions
The browser may enforce cross-origin rules
You configure CORS to specify things such as 
Allowed Origins
Allowed Methods 
Allowed Headers
Eample: Access-Control-Allow-Region: https://app.company.com
Avoid blindly allowing: *
for sensitive production APIs unless that's genuienly appropriate
Interview Answer
**CORS controls which browser origins are allowed to access the API. If it is missconfigured, the backend may be working correctly but the brower can still block frontend requets**

# API Gateway timeout scenari
Imagine:

API Gateway
 ↓
Lambda
 ↓
Very long processing
 ↓
Database
 ↓
External service

If synchronous processing takes too long, the client can time out even if backend work continues.

Don't design long-running workflows as:

API
 ↓
Wait 2 minutes
 ↓
Wait...
 ↓
Response

Instead:

POST /jobs
 ↓
API Gateway
 ↓
Lambda
 ↓
SQS
 ↓
Worker

Immediately return something like:

{
    "job_id": "JOB-123",
    "status": "PROCESSING"
}

with:

202 Accepted

Then:

GET /jobs/JOB-123

could return:

{
    "job_id": "JOB-123",
    "status": "COMPLETED"
}

This is exactly why your SQS/bulk-processing knowledge is useful in backend interviews.

# 502 Bad Gateway
Scenario:

API Gateway
 ↓
Lambda
 ↓
Invalid/error response

You may see:

502 Bad Gateway

Troubleshooting approach:

1. Check API Gateway logs
2. Check Lambda invocation
3. Check CloudWatch Lambda logs
4. Check exceptions
5. Check response format
6. Check integration configuration

For Lambda proxy-style integrations, make sure the Lambda returns the expected structure.

Conceptually:

return {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json"
    },
    "body": '{"message":"success"}'
}

# 504/timeout troubleshooting
uppose:

GET /reports
 ↓
API Gateway
 ↓
Lambda
 ↓
Slow DB query
 ↓
Timeout

Don't immediately increase every timeout.

First identify why it's slow.

Check:

CloudWatch logs
Lambda duration
Database query time
External API latency
Cold starts
Network connectivity
Downstream throttling

Then optimize architecture.

For truly long-running jobs:

API → SQS → Worker


# API input validation
Never blindly trust:

{
    "asset_name": "",
    "quantity": -100
}

Validate:

Required fields
Data types
Length
Allowed values
Ranges
Formats

For example:

if not asset_name:
    return {
        "statusCode": 400,
        "body": "asset_name is required"
    }

With FastAPI/Pydantic, you can define request schemas and validation at the application layer.

