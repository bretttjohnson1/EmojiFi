import emoji
import nltk
import random
import numpy as np


from random import randint
from emojisearch import search
from emojisearch import stop_words
from functools import lru_cache


VOWELS = {'a', 'e', 'i', 'o', 'u'}
B_EMOJI = emoji.emojize(':B_button_(blood_type):')


def beeify(word):
    """ Randomly replaces a word's first letter with the B emoji if applicable """
    if _is_beeifyable(word) and _can_beeify():
        return B_EMOJI + word[1::]

    return word


def _is_beeifyable(word):
    """ Determines if a word can be beeifyable """
    return len(word) > 1 and word[0].lower() not in VOWELS


def _can_beeify():
    """ Determines if the random chance to beeify has occured """
    return randint(0, 12) == 0


def emojify_text(text):
    """ Emojifies text by inserting emojis around valid words """
    return ' '.join([_emojify_word(w) for w in text.split()])


def _emojify_word(word):
    """ Returns a word concat with an emoji if the word requires one """
    if word.lower() not in stop_words() and not _has_numbers(word):
        return beeify(word) + ' ' + _word_relevant_emojis(word) + ' '

    return word  # Beeifying stopwords looks odd


@lru_cache(maxsize=1000)
def _word_relevant_emojis(word):
    relevant_emojis = search(word)
    collected_emojis = relevant_emojis[0:emojis_collected()]
    return ''.join([x * emojis_repeated() for x in collected_emojis])


def _has_numbers(text):
    """ Checks if any characters in the input text contain numbers """
    return any(char.isdigit() for char in text)


def emojis_collected():
    """ Returns the amount of emojis to collect """
    return 1 + np.random.poisson(.30)


def emojis_repeated():
    """ Returns the amount of times a collection of emojis are to be repeated """
    return 1 + np.random.poisson(.30)
