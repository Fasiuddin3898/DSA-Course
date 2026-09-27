# VPC is Virtual Private Cloud
It is a isolated private network inside AWS

AWS
│
├── Company A
│   └── VPC
│
├── Company B
│   └── VPC
│
└── Company C
    └── VPC

# Your VPC is your own network where we control
1. IP addres ranges
2. subnets
3. routing
4. internet access
5. private access
6. firewalls
7. connectivity between resources

For example:

VPC
CIDR: 10.0.0.0/16

That gives your VPC a private IP range.

# The complete VPC architecture
                         INTERNET
                            │
                            │
                     Internet Gateway
                            │
                     ┌──────┴──────┐
                     │     VPC     │
                     │ 10.0.0.0/16 │
                     │              │
             ┌───────┴───────┐
             │               │
        Public Subnet    Private Subnet
        10.0.1.0/24      10.0.2.0/24
             │               │
             │               │
            ALB             EC2
             │               │
             │          Application
             │               │
             │          ┌────┴────┐
             │          │         │
             │        Redis      RDS
             │

The important components are 
1. VPC
2. CIDR
3. Subnet
4. Route Table
5. Internet Gateway
6. Security Groups
7. NAT Gateway
8. Network ACL
9. Availability Zones
10 Load Balancer

# VPC CIDR
Suppose I create: 10.0.0.0/16
This is the IP range avilable inside the VPC
You can divide it into subnets
For Example:
VPC
10.0.0.0/16
│
├── Public Subnet
│   10.0.1.0/24
│
├── Public Subnet
│   10.0.2.0/24
│
├── Private Subnet
│   10.0.10.0/24
│
└── Private Subnet
    10.0.11.0/24

# What is Subnet ?
A subnet is a smaller network inside your VPC
You typically divide your architectre into:
**Public Subnet**
Resources that need direct internet-facing connectivity
Example:
ALB
Bastion Host
NAT Gateway
**Private Subnet**
Resources that shouldn't be directly reachable from the internet
Example:
Application servers
RDS
Redis
internal services

# What makes a subnet public ?
A subnet is not public just because you call it public subnet. It becomes public subnet when its route table has a route to an Internet Gateway
Example:
Public Subnet
     │
     ↓
Route Table
     │
     ├── 10.0.0.0/16 → local
     │
     └── 0.0.0.0/0 → Internet Gateway
That 0.0.0.0/0 means:
For destinations outside my VPC, send traffic to the Internet Gateway.

# Private Subnet
A private subnet doesn't have a direct route to an Internet Gateway
instead, if resources need outbound internet access

Private EC2 -> Route Table -> NAT Gateway -> Internet Gateway -> Internet

# Internet Gateway
An Internet Gateway connects your VPC to the internet
example: internet -> internet gateway -> VPC
But simply attaching an internet gateway doesn't automatically make every resource interent accessible
you also need:
-> Appropriate route table
-> public IP where applicable
-> security group rules

# NAT Gateway
-> Suppose private EC2 needs to download the pip packages, OS updates and external APIs
and you don't want that EC2 a public IP.
so: Private EC2 -> NAT Gateway -> Internet Gateway -> Internet
**The EC2 can initiate the outbound connections, while remaining inaccessible directly from the public interent**

# Why NAT Gateway is also a cost topic

This is particularly useful for your Hala interview.
NAT Gateway can create AWS charges based on:
NAT Gateway usage
data processing
traffic passing through it

Suppose you have:
100 GB
Private EC2
    ↓
NAT Gateway
    ↓
Internet

You're paying for NAT Gateway data processing in addition to relevant data-transfer costs.

So you can optimize by using VPC endpoints for AWS services where appropriate.
For example:
EC2
 ↓
VPC Endpoint
 ↓
S3

instead of:
EC2
 ↓
NAT Gateway
 ↓
Internet
 ↓
S3

This can reduce unnecessary NAT traffic and improve network design.

# Security Groups
Think of Security Group as a firewall attached to your resource's network interface

Example:

Internet
   ↓
ALB
   ↓
EC2

You might configure:

ALB Security Group
Inbound:
80  → 0.0.0.0/0
443 → 0.0.0.0/0
EC2 Security Group

Instead of:

Port 8000 → 0.0.0.0/0

you can allow:

Port 8000 → ALB Security Group

That's much more secure.

# Security Group is stateful
If you allow: Inbound TCP 443, the response traffic is automatically allowed.
You don't need to explicitly create the reverse outbound rule for the response
That's because the security group are stateful

# NACL is Network Access Control List
It works at the subnet level
Security Group; Resources Level, Stateful and Allow Rules
NACL: Subnet Level, Stateless amd Allow+Deny

**Security Group= resource-level firewall and NACL=subnet-level firewall**

# Availability Zone
A VPC exits across an AWS Region
Example:
Hyderabad application
        ↓
AWS Region
        ↓
VPC
 ┌───────────────┐
 │               │
AZ-1            AZ-2
 │               │
EC2             EC2

Why?

High availability.

If AZ-1 has a problem:

AZ-2
 ↓
Application continues

# Route Tables
Route Tables determine where does the network traffic go ?
Example:

Destination       Target

10.0.0.0/16       local
0.0.0.0/0         igw

For private subnet:

Destination       Target

10.0.0.0/16       local
0.0.0.0/0         NAT Gateway

# Where does VPC fits in your project
A production GenAI platform may need private networking depending on the architecture and service configuration.

You can explain the networking design conceptually:

                 Internet
                    │
                 API Gateway
                    │
                  Lambda
                    │
          ┌─────────┴──────────┐
          │                    │
      AWS Services        Private Resources
          │                    │
      S3 / Bedrock       OpenSearch/etc.
                              │
                           VPC

But be careful:

Lambda is not automatically inside a VPC.

And many AWS managed services don't require you to put everything into your VPC.

# Lambda + VPC interview question
Lambda function run in AWS-managed infrastructure by default. If the lambda needs access to resources inside a customer's VPC, such as private databse or internal services, we can configure the Lambda function to connect to the VPC using subnets and Security Groups.

Lambda
  │
  │ VPC configuration
  ↓
Private Subnet
  │
  ↓
RDS / Redis / Internal Service

# Why would you put Lmabda in a vpc
Suppose:
Lambda -> RDS
and RDS is private. Then Lambda needs newtwork connectivity into the VPC
Architecture
                VPC
 ┌─────────────────────────────┐
 │                             │
 │  Private Subnet             │
 │       │                     │
 │     Lambda                  │
 │       │                     │
 │       ↓                     │
 │      RDS                    │
 │                             │
 └─────────────────────────────┘

 But don't put Lambda into a VPC just because it's more secure. There are networking and operational considerations.

# A good answer for your project
Most of my core workloads were serverless and used managed AWS services, so vpc wasn't something I had to configure manually for every component. However, I understands where VPC fits into the architecture, particularly where private resources, network isolation, security controls or VPC-connected workloads are required.
For example, if a lambda-based backend needs to access a private databse, Redis or internal service, I would place the relevent resources in private subnets and configure lambda networking and security groups accordingly. For workloads requiring outbound internet access from private subnets, I would use NAT Gateway, while for AWS services such as S3. I would consider VPC endpoints to avoid unnecessary NAT traffic.

               