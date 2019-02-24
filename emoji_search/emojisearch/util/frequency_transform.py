from nltk.corpus import wordnet
from collections import defaultdict


def search(word):
    """ Assumes the word has been cleaned and is valid (e.g. not a stop word) """
    similar_words = [synset.name().split('.')[0] for synset in wordnet.synsets(word)]
    freqs = defaultdict(int)

    for synonym in similar_words:
        results = search(synonym)

        for result in results:
            code = result["title"]
            if code in freqs:
                freqs[code] += 1
            else:
                freqs[code] = 1

    if not freqs:
        return []
    result = [k for k, v in sorted(freqs.items(), key=lambda x: (x[1], x[0]), reverse=True)]
    return result
