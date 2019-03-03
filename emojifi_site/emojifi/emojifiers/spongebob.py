import random
from random import randint


def _radomized_case(text):
    """ Randomizes the case of letters in a string """
    return text.upper() if randint(0, 1) else text.lower()


def spongebobify_text(text):
    """ Spongebobify's text """
    return ''.join(_radomized_case(char) for char in text)
