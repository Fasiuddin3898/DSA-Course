# How would you optimize AWS cost in your project

In my projects, cost optimization was mainly handled by choosing managed and serverless services appropriately, monitoring resource usage, avoiding unnecessary resource consumption, and putting controls around storage, logging, compute and data transfer.

For example, we used S3 for file storage, Lambda for event-driven processing, DynamoDB for application data, and AWS CDK for infrastructure provisioning. With these services, we tried to avoid keeping unnecesary infrastrcuture running continously.

For s3, I would use lifecycle policies to transition older objects to lower-cost storage classes and delete temporary or absolute files based on the application's retention requirements

For compute and application workloads, I would monitor usage and execution patterns and make sure resources were appropriately sized. For CloudWatch, I would avoid keeping logs indefinitely and configure appropriate retention.

I would also monitor AWS spending through Cost Explorer and use AWS Budgets and Cost Anomaly Detection to identify unexpected increases in cost.

# What services would you mention for cost optimization?
                     AWS COST MANAGEMENT
                           |
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
 Cost Explorer         AWS Budgets       Cost Anomaly
                                           Detection
        |
        ↓
 Find expensive service/resource
        |
        ↓
 Optimize resource

 **AWS Cost Explorer**
 Used to answer: where is my money going
 You can break dowm costs by:
 Services, Region, Account, Usage Type, Tags
 Example:
 EC2          ₹40,000
S3           ₹10,000
NAT Gateway  ₹15,000
CloudWatch    ₹8,000
Lambda        ₹5,000

**AWS Budgets**
Used to say: Don't let us get suprised by our bill
Monthly Budget = ₹1,00,000

80% → Warning
90% → Critical
100% → Escalation

You can configure notifications through SNS/email and take controlled automated actions where appropriate.

**AWS Cost Anomaly Detection**
It looks for unusal spending patterns
Normal daily spend
₹2,000
₹2,100
₹1,900
₹2,050

Suddenly

₹8,500

# What precautions did you take?

This is where you can sound much more senior.

Say:

I would take preventive as well as reactive measures.

Preventive

Before deployment:

Choose appropriate AWS service
Avoid over-provisioning
Configure lifecycle policies
Configure log retention
Use autoscaling where appropriate
Set budgets
Configure anomaly detection
Apply resource tagging
Review architecture for unnecessary data transfer
Remove unused resources
Reactive

When cost increases:

Alert
 ↓
Cost Explorer
 ↓
Identify service
 ↓
Identify resource
 ↓
Check usage
 ↓
Find root cause
 ↓
Optimize
 ↓
Monitor again


# S3 cost optimization — YOUR BEST EXAMPLE

Since you specifically mentioned S3, learn this answer.

In S3, I would avoid keeping every object in S3 Standard indefinitely. Based on access patterns and retention requirements, I would use lifecycle rules to transition objects to lower-cost storage classes such as Standard-IA or Glacier, and delete temporary data after its retention period.

I would also monitor storage growth, remove unnecessary objects, clean up incomplete multipart uploads, and use appropriate storage classes for different workloads.

Example:

Excel upload
    ↓
S3 Standard
    ↓
After 30 days
    ↓
Infrequent Access
    ↓
After 90/180 days
    ↓
Glacier
    ↓
After retention period
    ↓
Delete

Don't give exact 30/90-day values as if they were your company's actual configuration. Say "for example" or "depending on retention requirements."

# Honda IDP example
In Honda IDP, S3 was used for Excel file upload and download. Because these files can include temporary processing data, one cost consideration is to avoid keeping unnecessary files forever. A lifecycle policy can automatically transition or delete files after the business-required retention period.

Presigned URLs also allow clients to upload/download directly to S3 instead of unnecessarily routing large files through the backend, which can reduce application-server processing and bandwidth requirements.

# Lambda cost optimization

Your projects use Lambda extensively.

Lambda cost is primarily influenced by:

Number of invocations
        +
Execution duration
        +
Memory allocation

So I'd say:

For Lambda, I would optimize execution time, avoid unnecessary invocations, batch operations where appropriate, and choose an appropriate memory configuration. I would also investigate whether a Lambda is being triggered unexpectedly or repeatedly.

Example:

Before:

Lambda
5 seconds × 1 million invocations

After:

Lambda
1 second × 1 million invocations

Reducing unnecessary execution time can reduce cost.

# CloudWatch cost optimization

This is a good one because you actually used CloudWatch.

Say:

For CloudWatch, one thing I would monitor is log volume and retention. Debug-level logs can become expensive if they're generated at high volume in production and retained indefinitely.

I would use appropriate log levels and retention policies and avoid unnecessary verbose logging in production.

For example:

Development
DEBUG logs

Production
INFO / WARN / ERROR

And:

7 days
30 days
90 days

depending on requirements.
