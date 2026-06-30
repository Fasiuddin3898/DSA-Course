# What is Terraform
Instead of creating resources manually in aws you write a code example 

resource "aws_s3_bucket" "my_bucket" {
    bucket = "company-data"
}

Run one command.
Terraform creates the bucket automatically.
Infrastructured becomes code.

This is called Infrastructure as Code(Iac)

# What is Infrastructure as Code?
Instead of creating infrastructure manually we write a code like

main.tf -> terraform apply -> AWS

everything is automated

# Why comapnies USe Terraform

Suppose your comapny has dev,QA,UAT, Prod environments

Every env needs same lambda, same vpc, same IAM, Same Dynamo DB

without terraform each engineer creates resources manually and can make miskates but with Terraform
Code -> Terraform -> All environments identical
No manula work is needed and no configuration drift

# Benifits of using Terraform

-> Repeatable: Creates the same infrastructure 100 times.
-> Version Control: Store infrastructure in GIT
we can track:who changed, when changed, what changed, why changed
-> Automation: CI/CD can automatically create infrastructure
-> Easy Recovery: Entire AWS account deleted?
# RUN terraform apply
everything comes back.
-> Documentation: The code itself doccuments the infrastructure.

# Why Not AWS Console?
WS Console is good for learning.
Companies don't create production infrastructure manually because:
-> Human error
-> Difficult to reproduce
-> No version history
-> No automation

# Terraform Architecture
Developer -> Terraform CLI -> AWS Provider -> AWS API -> AWS Resources
Terraform never creates resources directly it calls AWS APIs.

# How Terraform Works
Example:you write
resource "aws_s3_bucket" "bucket"{

}

Terraform translates this into:
CreateBucket API -> AWS -> Bucket created
Terraform is an orchestrator

# Core Components
Every terraform project has
-> Provider
-> Resource
-> Variables
-> Outputs
-> State

# Terraform Files
Typical project:

terraform-project/

│
├── main.tf
├── provider.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── backend.tf
├── versions.tf
└── modules/

# Terraform language
Terraform uses HCL languages which is
HashiCorp Languaghe looks like JSON but easier then JSON
Example:
resources "aws_s3-bucket" "bucket"{
    bucket="mybucket"
}

# Basic Block Types
Terraform has several types of blocks:
-> terraform
-> provider
-> resource
-> variable
-> output
-> module
-> locals
-> data

# Terraform workflow
every project follows the same lifecycle

Write Code -> terraform init -> terraform fmt -> terraform validate -> terraform plan -> terraform apply -> terraform destroy

# Step 1: terraform init
terraform init: Initializes project
Downloads:AWS Provider, Plugins, Dependencies
Creates: .terraform/

# Step 2:terraform fmt
terraform fmt: Formats code
Example:
before fmt
resource "aws_s3_bucket" "bucket" {
bucket = "my_bucket
}
after fmt
resource "aws_s3_bucket" "bucket" {
    bucket="my_bucket"
}

# Step 3: terraform validate
terraform validate: Checks syntax, it doesn't create anything

# Step 4: terraform plan
terraform plan shows 
Terraform will perform:

+ Create Bucket

+ Create IAM Role

+ Create Lambda

Plan: 3 to add.

Nothing changes yet, this is a dry run

# Step 5: terraform apply
terraform apply actually creates resources

# Step 6: terraform destroy
Deletes everything created by terraform

# The Provider
Terraform supports many clouds: AWS, GCP, AZURE, Kubernetes, Docker, Github, Cloudflare
The provider tells Terraform which platform to manage.
Example:
provider "aws" {
    region = "ap-south-1"
}
Now terraform talks to AWS

# Resource
Everything in AWS is a resource
Example:s3,lambda,iam,vpc,ec2,sns,sqs,cloudwatch
terraform creates resources using resource block
Example:
resource "aws_s3_bucket" "logs"{
    bucket="my_company_logs"
}
Breaking it down
resource "aws_s3_bucket" "logs"
resource → Terraform keyword.
aws_s3_bucket → Resource Type (what kind of AWS resource to create).
logs → Terraform Resource Name (a local identifier used only within Terraform).

Inside the block:

bucket = "my-company-logs"
bucket → AWS S3 bucket property.
"my-company-logs" → The actual S3 bucket name that will be created in AWS.
What does logs refer to?

logs is not the AWS bucket name.

It is Terraform's internal name for the resource.

Terraform uses it to reference the resource elsewhere:

resource "aws_s3_bucket" "logs" {
  bucket = "my-company-logs"
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.logs.id
}

Here:

aws_s3_bucket.logs.id
means:
aws_s3_bucket → resource type
logs → Terraform resource name
id → attribute of the created bucket

# How Resources Depend on Each Other
Example: Lambda needs an IAM Role
Terraform understands depedencies automatically when one reference another.

Example: IAM Role -> Lambda -> API Gateway

Terraform creates the IAM role before the Lambda function.

# What is the defination of terraform
Terraform is an Infrastructue as Code(IaC) tool developed by HashiCorp that allows you to define, provision,update and manage infrastructure using code instead of manually creating resources

# What is the workflow of terraform?
terraform follows 
terraform init -> terraform fmt -> terraform validate -> terraform plan -> terraform apply -> terraform destroy

# What does terraform init do?
-> terraform init downloads providers
-> initializes backed
-> Creates .terraform directory
-> installs plugins

# State:What is terraform state
Terraform stores information about infrastructure in: terraform.tfstate
It tracks
-> Existing resources
-> Resource IDs
-> Dependencies
-> Metadata

# Why is state important
Terraform compares:Desired state(your code) vs Current state(state file)
Then decides what changes are required

# What happens if the state file is deleted?
Terraform loses track of existing resources and may try to recreate them.

# What is remote state?
Instead of storing the state locally,it's stored remotely(commonly in an S3 bucket)
Benefits:
-> Team collaboration
-> Backup
-> Shared state
-> Security

# Why store state in s3?
-> Centralized
-> Durable
-> Shared among developers
-> Versioning support

# Why use DynamoDB with S3?
Fore state locking. Prevents multiple users from modifying the same infrastructure simulteaneously

# What is state locking ?
Only one person/process can modify the state at a time.
Prevents corruption

# Vriables
Terraform Variables: Variables make configuration reusable
Example:
variable "region" {
    default = "ap-south-1"
}
