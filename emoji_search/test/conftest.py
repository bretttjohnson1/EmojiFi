import pytest
from pyfakefs.fake_filesystem_unittest import Patcher
from emojisearch.paths import GENERATED_PATH
from emojisearch.paths import DATA_PATH

from emojisearch.create_whoosh_index import create_indexes


@pytest.fixture
def setup_fake_filesystem():
    with Patcher() as patcher:
        patcher.fs.add_real_directory(DATA_PATH)
        patcher.fs.add_real_directory('/usr/local/lib/nltk_data')
        patcher.fs.create_dir(GENERATED_PATH)
