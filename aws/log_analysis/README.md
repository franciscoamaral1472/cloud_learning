# Log Analysis Lab (Cloud Mindset)

## Objective
Simulate analysis of application logs stored in S3 using a cloud-native approach.

## Scenario
Application logs are stored in JSON format. We need to:
- Identify failed login attempts
- Detect potential brute-force attacks

## Cloud Equivalent
- Storage: Amazon S3
- Query: Amazon Athena
- Processing: AWS Lambda / Glue

## Key Concepts
- Log analysis
- Security monitoring
- Detection of suspicious behavior

## Next Steps
- Upload logs to S3
- Query using Athena
- Automate detection with Lambda

## Detection Engine

A simple detection engine was implemented to classify suspicious IP activity:

- HIGH risk: >= 3 failed login attempts
- MEDIUM risk: 1-2 failed attempts

The output is stored in JSON format, simulating integration with security tools or SIEM systems.