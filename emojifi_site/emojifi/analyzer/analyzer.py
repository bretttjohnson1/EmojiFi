import requests
from functools import lru_cache
import re
import os
import string
from emoji_search import search

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

STOPWORD_PATH = 'stopwords.txt'
PRE_URL = "https://emojifinder.com/ajax.php?action=search&query="
POST_URL = "&fbclid=IwAR2ISsQB4n2lkpYeyfKgtGGa2Yhj-xQS_0uu8WJ3Bqa7wZNQl6hj_a6CF5w"


@lru_cache(maxsize=1)
def load_stopwords():
    """ Reads the stopwords file and loads it into a set """
    with open(os.path.join(BASE_PATH, STOPWORD_PATH)) as f:
        return set(f.read().splitlines())


def next_word(text):
    """ Generator yielding the next word in a text """
    for word in text.split():
        yield word


def is_valid_word(word, stopwords):
    """ Returns whether a word is valid:
        (non-stop word and no character other than a-zA-Z)"""
    return word in stopwords and word.isalpha()


def emojifi_text(text):
    """ Emojifies text by inserting emojis around valid words """
    result = []
    stopwords = load_stopwords()

    for word in next_word(text):
        result.append(_emojifi_word(word, stopwords))

    return ' '.join(result)


def _has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def _emojifi_word(word, stopwords):
    """ Returns a word concat with an emoji if the word requires one """
    emoji = ''

    if word not in stopwords and not _has_numbers(word):
        stripped_word = word.translate(str.maketrans('', '', string.punctuation))
        display_code = search_emoji(stripped_word)

        if display_code:
            emoji = display_code

    return word + ' ' + emoji + ' '


def word_to_display_code(word):
    """ Returns the emoji display code of a word, or None, from the API call """
    if not word:
        return None

    url = PRE_URL + word + POST_URL
    emoji_data = requests.get(url).json()
    results = emoji_data["results"]

    if results:
        return _plaintext_hex_to_unicode(results[0]["Code"].split(' ')[0])

    return None


def search_emoji(word):
    results = search(word+'*')
    if results:
        return _plaintext_hex_to_unicode(results[0]["title"])
    else:
        return None


def _plaintext_hex_to_unicode(code):
    return chr(int(code, 16))
