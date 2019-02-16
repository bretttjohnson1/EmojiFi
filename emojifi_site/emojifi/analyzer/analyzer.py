from functools import lru_cache


STOPWORD_PATH = 'stopwords.txt'


@lru_cache(maxsize=1)
def load_stopwords():
    """ Reads the stopwords file and loads it into a set """
    with open(STOPWORD_PATH) as f:
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


def _emojifi_word(word, stopwords):
    """ Returns a word concat with an emoji if the word requires one """
    emoji = ''
    if word not in stopwords and word.isalpha():
        emoji = '[emoji]'

    return word + emoji
