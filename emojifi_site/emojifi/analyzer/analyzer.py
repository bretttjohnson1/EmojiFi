import requests
from functools import lru_cache
import re
import emoji
import os
import string
import nltk
from nltk.stem import WordNetLemmatizer
from emojisearch import search

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
STOPWORD_PATH = 'stopwords.txt'
PRE_URL = "https://emojifinder.com/ajax.php?action=search&query="
POST_URL = "&fbclid=IwAR2ISsQB4n2lkpYeyfKgtGGa2Yhj-xQS_0uu8WJ3Bqa7wZNQl6hj_a6CF5w"
SUBSTRING_TO_EMOJI = {
    'ae': '00C6',
    'ab': '1F18E',
    'cl': '1F191',
    'cool': '1F192',
    'ok': '1F197',
    'ng': '1F196',
}
LETTER_TO_EMOJI = {
    'a': '1F170',
    'b': '1F171',
    'c': '1F172',
    'm': '24C2',
    'o': '1F17E',
    'p': '1F17F',
    'x': '274E',
}

# NLTK path pointing
nltk.data.path.append(os.path.join('emojifi_site', 'emojifi', 'analyzer', 'nltkdata'))


# Initialize the lemmer at compile time
LEM_FUNC = WordNetLemmatizer().lemmatize
LEM_FUNC('a', pos='v') # Forces the lemmatizer to load at start


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


def clappifi_text(text):
    """ Emojifies text by inserting claps around every word """
    return emoji.emojize(' :clap: ', use_aliases=True).join(text.split())


def memeifi_text(text):
    """ Emojifies text by inserting emojis around valid words """
    result = []

    for word in next_word(text):
        result.append(_memeifi_word(word))

    return ' '.join(result)


def _memeifi_word(word):
    wordy = word
    result = []
    for ss in SUBSTRING_TO_EMOJI:
        wordy = wordy.replace(ss, _plaintext_hex_to_unicode(SUBSTRING_TO_EMOJI[ss]))

    for c in wordy:
        if c in LETTER_TO_EMOJI:
            result.append(_plaintext_hex_to_unicode(LETTER_TO_EMOJI[c]))
        else:
            result.append(c)
    return ''.join(result)


def _has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def _emojifi_word(word, stopwords):
    """ Returns a word concat with an emoji if the word requires one """
    emoji = ''

    if word not in stopwords and not _has_numbers(word):
        cpy = word
        try:
            cpy = LEM_FUNC(word, pos='v')
        except Exception:
            pass

        stripped_word = cpy.translate(str.maketrans('', '', string.punctuation))
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
    results = search(word)
    if results:
        return _plaintext_hex_to_unicode(results["title"])
    else:
        return None


def _plaintext_hex_to_unicode(code):
    return chr(int(code, 16))
