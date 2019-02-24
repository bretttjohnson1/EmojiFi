from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


# Required to ensure that the corpus loads
wordnet.ensure_loaded()


def lematize_words(word_list):
    return [WordNetLemmatizer().lemmatize(word, pos='v') for word in word_list]


def synonyms(word):
    return {lemma.name() for synset in wordnet.synsets(word) for lemma in synset.lemmas()}
