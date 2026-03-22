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