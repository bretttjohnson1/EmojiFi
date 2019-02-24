from emojisearch.generate_emoji_search_files import generate_search_files
from emojisearch.paths import EMOJI_FILES_DIR
from emojisearch.paths import EMOJI_FILES_DIR_FALLBACK
import os


def test_generate_search_files(setup_fake_filesystem):
    generate_search_files()
    assert len(os.listdir(EMOJI_FILES_DIR)) == 1570
    assert len(os.listdir(EMOJI_FILES_DIR_FALLBACK)) == 690
