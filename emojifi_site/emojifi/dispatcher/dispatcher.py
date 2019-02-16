import json
from ..analyzer.analyzer import emojifi_text as emojifi_text_by_search
from ..analyzer.analyzer import clappifi_text as emojifi_text_by_clap

TYPE_TO_DISPATCH_FUNC = {
    'clap': emojifi_text_by_clap,
    'search': emojifi_text_by_clap,
}


def dispatch_request(request):
    """ Dispatches the POST request to the appropriate analyzer functions """
    json_request = json.loads(request.body.decode('utf-8'))
    text = json_request['text']

    if 'type' in json_request:
        dispatch_func = TYPE_TO_DISPATCH_FUNC[json_request['type']]
        obj = EmojifiCompositon(text, dispatch_func)
    else:
        obj = EmojifiCompositon(text, emojifi_text_by_search)

    return _emojifi(obj)


def _emojifi(obj):
    return obj.dispatch_func(obj.text)


class EmojifiCompositon:
    def __init__(self, text, dispatch_func):
        self.text = text
        self.dispatch_func = dispatch_func
