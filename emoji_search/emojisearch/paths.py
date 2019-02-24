import os.path

_base_path = os.path.dirname(os.path.abspath(__file__))


def joined_with_base(path):
    return os.path.join(_base_path, path)


STOPWORD_PATH = joined_with_base('data/stopwords.txt')

EMOJI_MEANINGS_DIR = joined_with_base('data/emoji_meanings')
EMOJI_JSON_FILE = joined_with_base('data/emojis.json')

INDEX_DIR = joined_with_base('index_directory')
INDEX_DIR_FALLBACK = joined_with_base('index_directory_fallback')

EMOJI_FILES_DIR = joined_with_base('emoji_search_files')
EMOJI_FILES_DIR_FALLBACK = joined_with_base('emoji_search_files_fallback')
