import os.path
from os import listdir
from os.path import isfile, join
from whoosh import index
from whoosh.fields import Schema, TEXT

from emojisearch.paths import INDEX_DIR
from emojisearch.paths import INDEX_DIR_FALLBACK
from emojisearch.paths import EMOJI_FILES_DIR
from emojisearch.paths import EMOJI_FILES_DIR_FALLBACK

from emojisearch.search_engine_setup.emoji_file import EmojiFile

schema = Schema(
    emoji=TEXT(stored=True),
    name=TEXT(stored=True),
    content=TEXT(stored=True),
)


def create_index(index_dir, files_dir):
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)

    index_writer = index.create_in(index_dir, schema).writer()

    files_names_to_index = [join(files_dir, f) for f in listdir(files_dir) if isfile(join(files_dir, f))]

    for file_path in files_names_to_index:
        emoji_file = EmojiFile.read(file_path)
        index_writer.add_document(
            emoji=emoji_file.unicode_emoji,
            name=emoji_file.name,
            content=emoji_file.search_content,
        )

    index_writer.commit()


def create_indexes():
    create_index(INDEX_DIR, EMOJI_FILES_DIR)
    create_index(INDEX_DIR_FALLBACK, EMOJI_FILES_DIR_FALLBACK)


if __name__ == '__main__':
    create_indexes()
