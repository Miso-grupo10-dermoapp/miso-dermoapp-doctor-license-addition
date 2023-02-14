import json
import os

import boto3
from boto3.dynamodb.conditions import Key
import moto
import pytest

import app

TABLE_NAME = "Dermoapp-sprint1-doctor-DoctorDetails"
@pytest.fixture
def lambda_environment():
    os.environ[app.ENV_TABLE_NAME] = TABLE_NAME

@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

@pytest.fixture
def data_table(aws_credentials):
    with moto.mock_dynamodb():
        client = boto3.client("dynamodb", region_name="us-east-1")
        client.create_table(
            AttributeDefinitions=[
                {"AttributeName": "doctor_id", "AttributeType": "S"},
                {"AttributeName": "license_number", "AttributeType": "S"},
            ],
            TableName=TABLE_NAME,
            KeySchema=[
                {"AttributeName": "doctor_id", "KeyType": "HASH"},
                {"AttributeName": "license_number", "KeyType": "RANGE"}
            ],
            BillingMode="PAY_PER_REQUEST"
        )

        yield TABLE_NAME

def test_givenLambdaFunctionCallThenReturnJsonResponse(lambda_environment, data_table):

    event = {
            "resource": "/doctor/{doctor_id}/license",
            "path": "/doctor/123/license",
            "httpMethod": "POST",
            "pathParameters": {
                "doctor_id": "123"
            },
            "body": "{\n    \"license_number\": 234353\n}",
            "isBase64Encoded": False
    }
    response = app.handler(event, [])

    client = boto3.resource("dynamodb", region_name="us-east-1")
    mockTable = client.Table(TABLE_NAME)
    response = mockTable.query(
        KeyConditionExpression= Key('doctor_id').eq('123')
    )
    items = response['Items']
    if items:
        data = items[0]
    assert data is not None
    assert data['doctor_id'] is not None
    assert data['license_number'] is not None
    assert data['doctor_id'] == '123'
    assert data['license_number'] == "234353"