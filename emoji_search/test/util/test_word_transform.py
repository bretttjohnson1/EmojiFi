from emojisearch.util.word_transform import lemmatize_words
from emojisearch.util.word_transform import synonyms


def test_lemmatize_word():
    assert lemmatize_words(['biking'])[0] == 'bike'


def test_synonyms():
    assert synonyms('good')
