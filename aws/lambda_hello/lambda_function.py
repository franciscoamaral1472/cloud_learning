import json

def lambda_handler(event, context):
    print("Lambda execution started")
    print(f"Received event: {json.dumps(event)}")

    try:
        name = "World"

        # API Gateway style input
        if "queryStringParameters" in event and event["queryStringParameters"]:
            name = event["queryStringParameters"].get("name", "World")

        response = {
            "message": f"Hello {name} from AWS Lambda!"
        }

        print(f"Generated response: {json.dumps(response)}")

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        error_message = {"error": str(e)}
        print(f"Execution failed: {json.dumps(error_message)}")

        return {
            "statusCode": 500,
            "body": json.dumps(error_message)
        }