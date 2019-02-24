from emojisearch import stop_words
from emojisearch.util.word_transform import lemmatize_words
from emojisearch.search_engine_setup.emoji_file import EmojiFile
from emojisearch.util.cleaning import cleaned_of_punctuation
from emojisearch.util.cleaning import filter_stop_words

from os import listdir
from os.path import isfile
from os.path import join
from bs4 import BeautifulSoup


def _plaintext_hex_to_unicode(code):
    return chr(int(code, 16))


loaded_stop_words = stop_words()


def cleaned_description(description):
    description = cleaned_of_punctuation(description)
    description_words = filter_stop_words(description)

    return ' '.join(lemmatize_words(description_words.split(' ')))


def search_file_entry_generator(html_file):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, features="html5lib")
    for entry in soup.body.find_all(text=True):
        cleaned = entry.strip()
        if 'U+' in cleaned:
            description, unicode_hex = cleaned.split('\n')
            unicode_hex = unicode_hex.strip(' ').strip('U+')
            description = cleaned_description(description)
            emoji = _plaintext_hex_to_unicode(unicode_hex)
            yield (emoji, description)


def generate_search_files_from_emoji_meanings(corpus_directory, emoji_file_directory):

    html_files = [
        join(corpus_directory, f)
        for f in listdir(corpus_directory)
        if isfile(join(corpus_directory, f))
    ]

    for html_file in html_files:
        for emoji, description in search_file_entry_generator(html_file):
            EmojiFile(emoji, '', description).write(emoji_file_directory)
