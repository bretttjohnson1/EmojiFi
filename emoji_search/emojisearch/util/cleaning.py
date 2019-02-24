from emojisearch.util.stopwords import stop_words


def cleaned_of_punctuation(content):
    return ''.join(
        char.lower()
        for char in content
        if char.isalpha() or char == ' '
    )


def filter_stop_words(content):
    return ' '.join(
        word
        for word in content.split(' ')
        if word not in stop_words()
    )
