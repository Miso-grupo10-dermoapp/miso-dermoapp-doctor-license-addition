import json
from db_service import *


def handler(event, context):
    dbop = insert_item('test')
    if dbop:
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": dbop
                }
            ),
        }