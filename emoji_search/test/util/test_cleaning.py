from emojisearch.util.cleaning import cleaned_of_punctuation
from emojisearch.util.cleaning import filter_stop_words


def test_cleaned_of_punctuation():
    assert cleaned_of_punctuation('t.h,e;"[]') == 'the'


def test_filter_stop_words():
    assert filter_stop_words("it's not a joke") == "joke"
