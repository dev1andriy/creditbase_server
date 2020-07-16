from common.models import RequestType
from common.serializers.configs import RequestTypeSerializer


def generate_request_type_param(data):
    config = {
        'required': True,
        "name": "requestType",
        "parameterCategory": "General parameters",
        'parameterName': {
            'value': 'Request Type',
            'color': '#707070'
        },
        "hostValue": None,
        "modify": {
            "statesAmount": 2,
            "rewritable": False,
            "data": 1
        },
        "proposedValue": {
            "config": {
                "type": "select",
                "options": RequestTypeSerializer(RequestType.objects.all(), many=True).data
            },
            "data": data
        },
        "print": {
            "statesAmount": 3,
            "rewritable": True,
            "data": 2
        }
    }

    return config