# CI/CD pipeline in AWS
A CI/CD pipeline is simply an automated process that takes your code from your laptop and deploys it into production without anyone manually copying files.

# Workflow
Developer -> Git Repository(GitHub / CodeCommit) -> AWS CodePipeline -> Source Stage -> Build Stage (CodeBuild) -> Test Stage(pytest) -> Package Stage -> Deploy Stage(CodeDeploy / CloudFormation / CDK / ECS / Lambda) -> AWS Environment 

# Step 1 -- Developer writes code
Suppose you are developing a FastAPI Project

backend/
    app.py
    routes.py
    service.py
    models.py
    requirements.txt

You make some changes.
Example:Added a new REST API which is GET / users
Everything works locally, now you want AWS to deploy it

# Step 2 -- Git Branching
In companies nobody works directly on main
Typical structure
main
develop
feature/login
feature/payment
feature/report
bugfix/token

Example:You are developing login, so you create a branch 
git checkout -b feature/login
Now you are working only on your branch.
Commit: git add . and git commit -m "added login page"
push: git push origin feature/login
What happens after Push? Nothing
Until someone creates a Pull Request
Example: feature/login --> develop
Manager reviews
Approves
Merge
Now develop has latest code

# How AWS detech this?
This is the most common interview question
AWS continous watches your repository
There are multiple ways
Example: GitHub -> Webhook -> AWS CodePipeline
GitHub sends an HTTP webhook
POST 
Repository Updated
AWS immediately knows
Someone pushed code
Pipeline automatically starts
Nobody clicks anything

# AWS CodePipeline
Imagie CodePipeline as the manager
Its only job is 
Take code -> Build -> Test -> Deploy

# Stage 1 -- Source
Pipeline first downloads code
Source cab be 
GitHub
BitBucket
CodeCommit
GitLab
Example: Repository is backend-api and  Branch is develop
AWS downloads latest source

# Stage 2 -- Build
Now AWS has your code.
But code cannot run immediately, it has to build first
AWS uses CodeBuild
Think of CodeBuild as a temporary Linux machine
It Starts
Ubuntu -> Download code -> Runs Command -> Deletes itself

**buildspec.yml** 
Every CodeBuild project looks for 
**buildspec.yml**
Example:
version: 0.2

phases:

  install:
    commands:
      - pip install -r requirements.txt

  pre_build:
    commands:
      - echo Running Tests

  build:
    commands:
      - pytest

  post_build:
    commands:
      - zip deployment.zip *

This file tells AWS what to execute

What happens inside CodeBuild?
Imagine
Fresh Linux Machine -> Install Python -> Install PIP -> Install dependencies -> Run Tests -> Package code -> upload artifact

Everything happens automatically

# Stage 3 -- Testing
Suppose your project contains
tests/
test_login.py
test_payment.py
test_isers.py

CodeBuild runs -- pytest
if even one test fails
Pipeline stops
Nothing gets deployes

Why? because AWS protects production.
Example:
Login API broken -> pytest fails -> Pipeline stops -> Users never see broken code

# Stage 4 -- Artifact
**Artifact means the final packaged output produced by build process that is ready to deployed or used**
Now build succeeds
AWS packages everything
Example: development.zip
or Docker Image
backend:v14
**Artifacts are usually stored in S3**
Example:
my-artifacts/
backend.zip
build2.zip
build3.zip

# Stage 5 -- Deploy
Now deployment begins
Depending on application
1. Lambda 
Upload ZIP -> Replace Lambda Code
2. ECS
Push Docker Image -> Start New Containers -> Stop Old Containers
3. EC2
Copy files -> Restart Service -> Health Check
4. CDK
cdk deploy
AWS updates infrastructure

1. How Lambda Deployment Works
Suppose API Gateway -> Lambda
Pipeline reaches deploy stage
AWS automatically 
upload ZIP -> Update Lambda -> Publish new version -> Traffic starts hitting new version
No manual upload

2. Hoe EC2 deployment works
Example: FastAPI -> EC2 -> Gumicorn -> Nginx -> Pipeline -> SSH -> Copies files -> Installs requirements -> Restarts Gunicorn -> Done

3. Docker Deploymet
Suppose project uses Docker
Pipeline -> Build Docker Image (docker build) -> Tag(backend:v25) -> Push (ECR) -> ECS pulls latest image -> Runs new container

# What triggers deployment?
Usually -> Merge into develop (or) Merge into main
Example:
feature/login -> develop -> Pipeline starts

# Manual Trigger
Sometimes manager clicks
Release ->  then pipeline starts

# Schedules Trigger
Every night 2 AM -> Run pipeline

# Rollback
Suppose deployment breaks
AWS can 
Deploy Previous Build
Example:
Version 16 -> Broken -> Rollback -> Version 15
Users never notice

# Environment Flow
Real companies never deploy directly to Production
Developer -> Dev -> QA -> UAT -> Production
Every stage has its own AWS account or environment

# Typical AWS Services Used
Service -> Purpose
GitHub -> Source code
CodePipeline -> Pipeline orchestartion
CodeBuild -> Build & test
s3 -> Artifact storage
CodeDeploy -> Deploy to EC2/Lambda
ECR -> Docker Images
ECS/EKS -> Containers
CloudForamtion/CDK -> Infrastructure deployment
CloudWatch -> Logs and monitoring
IAM -> Permissions
SNS -> Notifications
Secrete Manager -> Secure credentials

We followed a Git-based development workflow where developers worked on feature baranches and raised pull requests to the development branch.Once the PR was approved and merged, AWS CodePipeline automatically detected the change through a GitHub webhook. The pipeline triggered AWS CodeBuild, which provisioned a temporary build environment, installed project dependencies, executed the build process, and validated the application.Infrastructure changes were manged using AWS CDK, and deployments updated services such as AWS Lambda, API Gateway, DynamoDB, and related cloud resources. We also monitored deplyments using ClodWatch logs and metrics, and any pipeline failures prevented deployment to ensure production stability. 