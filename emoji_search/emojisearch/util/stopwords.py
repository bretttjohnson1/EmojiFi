from emojisearch.paths import STOPWORD_PATH
from functools import lru_cache


@lru_cache(maxsize=1)
def stop_words():
    """ Reads the stopwords file and loads it into a set """
    with open(STOPWORD_PATH) as f:
        return set(f.read().splitlines())
