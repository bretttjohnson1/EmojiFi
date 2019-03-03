import json


from emojifi.emojifiers.clap import clappify_text
from emojifi.emojifiers.spongebob import spongebobify_text
from emojifi.emojifiers.emojipasta import emojify_text
from datetime import datetime
import numpy as np
import random

TYPE_TO_DISPATCH_FUNC = {
    'search': emojify_text,
    'clap': clappify_text,
    'spongebob': spongebobify_text,
}


def dispatch_request(request):
    """ Dispatches the POST request to the appropriate analyzer functions """
    json_request = json.loads(request.body.decode('utf-8'))
    text = json_request['text']
    seed_randoms()

    if 'type' in json_request:
        dispatch_func = TYPE_TO_DISPATCH_FUNC[json_request['type']]
    else:
        dispatch_func = emojify_text

    return dispatch_func(text[0:1000])  # Limit to the first 1000 characters


def seed_randoms():
    """
    Seed randoms to create deterministic responses
    """
    current_date = datetime.now()
    seed_value = int(f'{current_date.year}{current_date.month}{current_date.day}{current_date.hour}')
    random.seed(seed_value)
    np.random.seed(seed_value)
