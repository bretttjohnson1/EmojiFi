from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


# Required to ensure that the corpus loads
wordnet.ensure_loaded()


def lemmatize_words(word_list):
    return [lemmatize_word(word) for word in word_list]


def lemmatize_word(word):
    word = WordNetLemmatizer().lemmatize(word, pos='v')
    word = WordNetLemmatizer().lemmatize(word, pos='n')
    return WordNetLemmatizer().lemmatize(word, pos='a')


def synonyms(word):
    return {lemma.name() for synset in wordnet.synsets(word) for lemma in synset.lemmas()}
