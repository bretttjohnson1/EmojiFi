import os
import json
import shutil
import emoji
from emojisearch.paths import EMOJI_FILES_DIR
from emojisearch.paths import EMOJI_FILES_DIR_FALLBACK

from emojisearch.paths import EMOJI_JSON_FILE
from emojisearch.paths import EMOJI_MEANINGS_DIR

from emojisearch.search_engine_setup.search_file_generator.emoj_json import generate_search_files_from_emoji_json
from emojisearch.search_engine_setup.search_file_generator.emoji_meanings import generate_search_files_from_emoji_meanings


def delete_all_files(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)


def generate_search_files():
    for directory in [EMOJI_FILES_DIR, EMOJI_FILES_DIR_FALLBACK]:
        delete_all_files(directory)
    generate_search_files_from_emoji_json(EMOJI_JSON_FILE, EMOJI_FILES_DIR)
    generate_search_files_from_emoji_meanings(EMOJI_MEANINGS_DIR, EMOJI_FILES_DIR_FALLBACK)


if __name__ == '__main__':
    generate_search_files()
