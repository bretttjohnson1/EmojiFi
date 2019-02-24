from emojisearch.create_whoosh_index import create_indexes
from emojisearch.paths import INDEX_DIR
from emojisearch.paths import INDEX_DIR_FALLBACK
import os


def test_generate_search_files(setup_fake_filesystem):
    create_indexes()
    assert len(os.listdir(INDEX_DIR)) == 3
    assert len(os.listdir(INDEX_DIR_FALLBACK)) == 3
