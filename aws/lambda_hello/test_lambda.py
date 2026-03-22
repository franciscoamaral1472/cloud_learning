from lambda_function import lambda_handler

event = {
    "queryStringParameters": {
        "name": "Francisco"
    }
}

result = lambda_handler(event, None)
print(result)