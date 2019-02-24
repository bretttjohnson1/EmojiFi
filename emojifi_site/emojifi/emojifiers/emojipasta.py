import emoji
import nltk
import os
import random
import re
import string
import numpy as np


from functools import lru_cache
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from random import randint
from emojifi.analyzer.emojifi_searcher import valid_word_to_emoji_freqs


VOWELS        = ['a', 'e', 'i', 'o', 'u']
B_EMOJI_ALIAS = '1F171'

LEM_FUNC = WordNetLemmatizer().lemmatize
LEM_FUNC('a', pos='v')  # Forces the lemmatizer to load at start


@lru_cache(maxsize=1)
def load_stopwords():
    return set(stopwords.words('english'))


def beeify(word):
    """ Randomly replaces a word's first letter with the B emoji if applicable """
    def is_beeifyable(word):
        """ Determines if a word can be beeifyable """
        return len(word) > 1 and word[0].lower() not in VOWELS

    def can_beeify():
        """ Determines if the random chance to beeify has occured """
        return randint(0, 15) == 0

    @lru_cache(maxsize=1)
    def b_emoji():
        """ Returns the B emoji """
        return _plaintext_hex_to_unicode(B_EMOJI_ALIAS)

    def beeify_valid_word(word):
        """ Beeify's a word, assuming is_beeifyable() and can_beeify() were true """
        return ''.join([b_emoji()] + list(word[1::]))

    if is_beeifyable(word) and can_beeify():
        return beeify_valid_word(word)

    return word


def emojify_text(text):
    """ Emojifies text by inserting emojis around valid words """
    random.seed(5)
    np.random.seed(5)
    result = []
    stopwords = load_stopwords()

    for word in text.split():
        result.append(_emojify_word(word, stopwords))

    return ' '.join(result)


def _emojify_word(word, stopwords):
    """ Returns a word concat with an emoji if the word requires one """
    wordy = word
    emojis = ''

    if word not in stopwords and not _has_numbers(word):
        cleaned_word = clean_word(word)
        freqs = valid_word_to_emoji_freqs(cleaned_word)
        top_n = freqs[0:emojis_collected()]
        emojis = ''.join([emoji.emojize(x) * emojis_repeated() for x in top_n])

    if word:
        wordy = beeify(wordy)

    return wordy + ' ' + emojis + ' '


def _plaintext_hex_to_unicode(code):
    return chr(int(code, 16))


def is_valid_word(word, stopwords):
    """ Returns whether a word is valid:
        (non-stop word and no character other than a-zA-Z)"""
    return word in stopwords and word.isalpha()


def _has_numbers(text):
    """ Checks if any characters in the input text contain numbers """
    return any(char.isdigit() for char in text)


def clean_word(word):
    """ Removes punctuation and lemmatizes the word if applicable """
    try:
        clean = LEM_FUNC(word.lower(), pos='v')
    except Exception:
        clean = word

    return clean.translate(str.maketrans('', '', string.punctuation))


def emojis_collected():
    """ Returns the amount of emojis to collect """
    return 1 + np.random.poisson(.30)


def emojis_repeated():
    """ Returns the amount of times a collection of emojis are to be repeated """
    return 1 + np.random.poisson(.30)
