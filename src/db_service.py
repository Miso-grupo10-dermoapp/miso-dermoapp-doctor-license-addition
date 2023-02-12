import boto3

client = boto3.resource('dynamodb')


def insert_item(body):
    try:
        table = client.Table('Dermoapp-sprint1-doctor-DoctorDetails-W7SV13VH080Q')
        data = table.put_item(
            Item={
                'id': '45678',
                'license': '655756565',
                'specialialties': [
                    {
                        "name": "dermatologist",
                        "verified": True
                    }
                ]
            }
        )
        return data
    except Exception as e:
        return 'cannot persist on db cause: ' + str(e)


def get_item():
    try:
        table = client.Table('dermoapp-v2-Doctor-AZEUNS8HXUN1')
        data = table.get_item(
            Key={
                'id': '123sdsdsd'
            }
        )
        return data
    except Exception as e:
        return 'cannot persist on db cause: ' + str(e)
