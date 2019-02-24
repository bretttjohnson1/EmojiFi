import random
from random import randint


def _radomized_case(text):
    """ Randomizes the case of letters in a string """
    return text.upper() if randint(0, 1) else text.lower()


def spongebobify_text(text):
    """ Spongebobify's text """
    random.seed(5)
    return ''.join(_radomized_case(char) for char in text)
