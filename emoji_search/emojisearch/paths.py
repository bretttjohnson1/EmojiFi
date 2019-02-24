import os.path

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def joined_with_base(path):
    return os.path.join(BASE_PATH, path)


def joined_with_generated(path):
    return os.path.join(joined_with_base('generated/'), path)


def joined_with_data(path):
    return os.path.join(joined_with_base('data/'), path)


GENERATED_PATH = joined_with_generated('')
DATA_PATH = joined_with_data('')

STOPWORD_PATH = joined_with_data('stopwords.txt')

EMOJI_MEANINGS_DIR = joined_with_data('emoji_meanings')
EMOJI_JSON_FILE = joined_with_data('emojis.json')

INDEX_DIR = joined_with_generated('index_directory')
INDEX_DIR_FALLBACK = joined_with_generated('index_directory_fallback')

EMOJI_FILES_DIR = joined_with_generated('emoji_search_files')
EMOJI_FILES_DIR_FALLBACK = joined_with_generated('emoji_search_files_fallback')
