from functools import lru_cache
from nltk.corpus import stopwords


@lru_cache(maxsize=1)
def stop_words():
    """ Reads the stopwords file and loads it into a set """
    return set(stopwords.words('english'))
