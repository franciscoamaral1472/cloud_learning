# IAM Least Privilege - S3 Read Only Policy

## Objective
This example demonstrates the principle of least privilege in AWS IAM.

Instead of granting broad access such as `AmazonS3FullAccess`, this policy only allows:

- listing a specific S3 bucket
- reading objects from a specific prefix inside that bucket

## Why this matters
In cloud security, permissions should always be restricted to the minimum required actions and resources.

This reduces:
- accidental exposure of sensitive data
- privilege escalation opportunities
- blast radius in case of credential compromise

## Allowed actions
- `s3:ListBucket` on:
  - `example-security-logs-bucket`
- `s3:GetObject` on:
  - `example-security-logs-bucket/logs/*`

## Use case
A security analyst or log analysis process may need to read logs stored in S3 without being able to:
- upload files
- delete files
- access other buckets
- modify permissions

## Security note
This is a simple example for learning purposes.  
In production, policies should be adapted to:
- real bucket names
- exact prefixes
- role-based access
- monitoring and audit requirements