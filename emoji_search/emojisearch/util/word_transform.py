from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


def lematize_words(word_list):
    return [WordNetLemmatizer().lemmatize(word, pos='v') for word in word_list]


def synonyms(word):
    return {synset.name().split('.')[0] for synset in wordnet.synsets(word)}
