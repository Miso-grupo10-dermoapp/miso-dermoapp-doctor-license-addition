import json


def return_error_response(errorMessage, httpCode):
    return {
        "statusCode": httpCode,
        "body": json.dumps(
            {
                "message": errorMessage
            }
        ),
    }


def return_status_ok(responseBody):
    return {
        "statusCode": 200,
        "body": json.dumps(responseBody),
    }

