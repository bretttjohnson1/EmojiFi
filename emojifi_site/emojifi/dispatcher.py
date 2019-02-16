import json
from django.http import HttpRequest


def dispatch_request(request: HttpRequest):
    """ Dispatches the POST request to the appropriate analyzer functions """
    json_request = json.loads(request.body.decode('utf-8'))
    emojify_type = json_request['type']
