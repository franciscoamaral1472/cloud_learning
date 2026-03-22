# AWS Lambda Hello World

Simple AWS Lambda function in Python simulating a basic API endpoint.

## Features
- Handles query parameters (API Gateway style)
- Returns structured JSON response
- Basic error handling

## Example Event

```json
{
  "queryStringParameters": {
    "name": "Francisco"
  }
}

## Logging

This function includes basic structured logging for:

- Lambda execution start
- Incoming event payload
- Generated response
- Error tracking

These logs can be viewed in AWS CloudWatch when deployed.