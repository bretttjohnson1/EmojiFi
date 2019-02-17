import nltk
import os
import operator
from nltk.corpus import wordnet
from emojisearch import search


# NLTK path pointing
nltk.data.path.append(os.path.join('emojifi_site', 'emojifi', 'analyzer', 'nltkdata'))


def valid_word_to_emoji(word):
    """ Assumes the word has been cleaned and is valid (e.g. not a stop word) """
    similar_words = [synset.name().split('.')[0] for synset in wordnet.synsets(word)]
    freqs = dict()

    for w in similar_words:
        results = search(w)

        for result in results:
            code = result["title"]
            if code in freqs:
                freqs[code] += 1
            else:
                freqs[code] = 1

    if not freqs:
        return ''

    return max(freqs.items(), key=operator.itemgetter(1))[0]
