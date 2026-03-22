import json

def lambda_handler(event, context):
    try:
        name = "World"

        # Caso venha de API Gateway
        if "queryStringParameters" in event and event["queryStringParameters"]:
            name = event["queryStringParameters"].get("name", "World")

        response = {
            "message": f"Hello {name} from AWS Lambda!",
            "input_event": event
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }