# Log Analysis with S3 + Athena

## Objective
Analyze application security logs stored in S3 using Amazon Athena with minimal operational overhead.

## Architecture
- Logs stored in S3 (JSON format)
- Athena used to query logs directly
- No servers or infrastructure required

## Why Athena?
Athena allows:
- SQL queries directly on S3
- serverless architecture
- no data ingestion required

## Example queries

### 1. Count actions
```sql
SELECT action, COUNT(*) 
FROM phishing_logs
GROUP BY action;