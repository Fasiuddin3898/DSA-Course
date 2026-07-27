# API
API stands for Application Programming Interface
client --> API --> server
# HTTP
HyperText Transfer Protocol.It is simply a language that the client and server use to communicate.
Imaging two people speak english
Similarly,
Browser speaks HTTP
Server understand HTTP
Example Request: GET/users HTTP/1.1
Server understands: "Oh, he wants the users."
# HTTPS= HTTP+Security
Browser -->Encypted --> Server
Nobody can read data
Suppose you're sending
Username
Password
Bank Details
HTTP
username=admin
password=1234
Anyone can intercept it.

HTTPS encrypts it.
kJHASDKJASDKJASDHJKAS
Nobody can understand it.

# What is SSL/TLS?
SSL/TLS is the technology that provides encryption for HTTPS.
When you visit -> https://google.com
Browser first checks
Is Google's certificate valid?
If yes
Encrypted connection starts.
That's why you see
🔒
near the URL.

# HTTP Request Structure
Whenever you call an API -> GET /users HTTP/1.1
you call with
Host: example.com
Authorization: Bearer token
Content-Type : application/json
Body
{
   "name":"John"
}
Every request has
Method
URL
Headers
Body

# HTTP Response
Server replies -> 
http/1.1 200 OK
Content-Type: application/json
Body
{
   "message":"Success"
}

# HTTP Methods
# GET (Retrieve data)
GET /users
Response
[
  {
    "id":1,
    "name":"John"
  }
]
# POST (Create Data)
POST /users
Body
{
 "name":"David"
}
# PUT (Replace entire object)
Before
{
"name":"John",
"age":25
}
PUT
{
"name":"David",
"age":30
}
Everything gets replaced.
# PATCH (Update only required field)
Before
{
"name":"John",
"age":25
}
PATCH
{
"age":30
}
After
{
"name":"John",
"age":30
}
# DELETE (Delete a resource)
DELETE /users/5

# Status Codes

Code        ->     Meaning
200. -> Success
201. -> Created
204. -> Deleted Successfully
400. -> Bad Request
401. -> Unauthorized
403. -> Forbidden
404. -> Not Found
405. -> Method Not Allowed
409. -> Conflict
500. -> Server Error

# REST API 
Rest means "Representational State Transfer"
It is a standard way of desiging APIs
Instead of getAllStudents, createAllStudents, deleteStudent

REST says
GET/students
POST/students
GET/student/10
DELETE/student
Everything resolves around resource like (student)

Almost every REST API sends JSON or array of JSON
