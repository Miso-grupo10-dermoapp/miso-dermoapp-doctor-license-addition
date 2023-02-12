import json
from db_service import *


def handler(event, context):
    # dbop = insert_item('test')
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": event
            }
        ),
    }