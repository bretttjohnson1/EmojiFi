from functools import lru_cache
from nltk.corpus import stopwords
from emojisearch.paths import STOPWORD_PATH


@lru_cache(maxsize=1)
def stop_words():
    """ Reads the stopwords file and loads it into a set """
    stop_word_set = set()
    with open(STOPWORD_PATH, 'r') as stop_words_file:
        stop_word_set = stop_word_set.union(set(stop_words_file.readlines()))
    return stop_word_set.union(set(stopwords.words('english')))
