import json
from django.http import HttpRequest
from ..analyzer.analyzer import emojifi_text
from ..analyzer.analyzer import clappifi_text


def dispatch_request(request: HttpRequest):
    """ Dispatches the POST request to the appropriate analyzer functions """
    json_request = json.loads(request.body.decode('utf-8'))
    text = json_request['text']

    obj = EmojifiCompositon(text, emojifi_text)

    if json_request['type']:
        dispatch_func = _type_to_dispatch_func(json_request['type'])
        obj = EmojifiCompositon(text, dispatch_func)

    return _emojifi(obj)


def _emojifi(obj):
    return obj.dispatch_func(obj.text)


def _type_to_dispatch_func(type_as_str):
    switch = {'clap': clappifi_text,
              'search': emojifi_text
              }

    return switch['type']


class EmojifiCompositon:
    def __init__(self, text, dispatch_func):
        self.text = text
        self.dispatch_func = dispatch_func
