import json


def validate_body_license(body):
    try:
        licenseRequest = json.loads(body)
        if validate_property_exist("license_number", licenseRequest) == False:
            raise Exception("license cannot be empty")
    except Exception as err:
        raise Exception("Input request is malformed or missing parameters, details " + str(err))
    return True


def validate_property_exist(property, loadedBody):
    if property in loadedBody:
        if loadedBody[property] is not None:
            return True
        else:
            return False
    else:
        return False
