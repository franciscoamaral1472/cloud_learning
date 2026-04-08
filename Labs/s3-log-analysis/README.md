# S3 Log Analysis Lab

## Objective
Analyze simulated S3 access logs to identify suspicious activity.

## Scenario
A public S3 bucket is being accessed. We want to detect:
- Unusual IP addresses
- High frequency access
- Unauthorized actions

## Approach
- Logs stored in JSON format
- Queries simulate AWS Athena usage
- Identify anomalies based on patterns

## Key Findings
- Repeated access from unknown IP
- Multiple GET requests in short time window

## Skills Demonstrated
- Log analysis
- Cloud security fundamentals
- Detection mindset