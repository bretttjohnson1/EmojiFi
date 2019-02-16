import json
from django.http import HttpRequest
from ..analyzer.analyzer import emojifi_text as emojify_text_by_search
from ..analyzer.analyzer import clappifi_text

type_to_dispatch_func = {
    'clap': clappifi_text,
    'search': emojify_text_by_search,
}


def dispatch_request(request: HttpRequest):
    """ Dispatches the POST request to the appropriate analyzer functions """
    json_request = json.loads(request.body.decode('utf-8'))
    text = json_request['text']

    if 'type' in json_request:
        dispatch_func = type_to_dispatch_func[json_request['type']]
        obj = EmojifiCompositon(text, dispatch_func)
    else:
        obj = EmojifiCompositon(text, emojify_text_by_search)

    return _emojifi(obj)


def _emojifi(obj):
    return obj.dispatch_func(obj.text)


class EmojifiCompositon:
    def __init__(self, text, dispatch_func):
        self.text = text
        self.dispatch_func = dispatch_func
