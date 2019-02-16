import os.path
from os import listdir
from os.path import isfile, join
from whoosh import index
from whoosh.fields import Schema, TEXT, ID

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR = join(BASE_PATH, 'index_directory')
FILES_DIR = join(BASE_PATH, 'emoji_search_files')


def create_index():
    schema = Schema(
        title=TEXT(stored=True),
        content=TEXT,
        textdata=TEXT(stored=True),
    )

    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)

    ix = index.create_in(INDEX_DIR, schema)

    writer = ix.writer()

    files_names_to_index = [join(FILES_DIR, f) for f in listdir(FILES_DIR) if isfile(join(FILES_DIR, f))]

    for file_name in files_names_to_index:
        with open(file_name, 'r') as file:
            print(file_name)
            base_name = os.path.basename(file_name)
            file_content = ''.join(file.readlines())
            print('title', base_name)
            print('content', file_content)
            writer.add_document(
                title=str(base_name),
                content=file_content,
                textdata=file_content,
            )

    writer.commit()


if __name__ == '__main__':
    create_index()
