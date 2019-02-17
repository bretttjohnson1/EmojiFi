import os.path
from os import listdir
from os.path import isfile, join
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
import nltk
from nltk.stem import WordNetLemmatizer

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR = join(BASE_PATH, 'index_directory')
FILES_DIR = join(BASE_PATH, 'emoji_search_files')

INDEX_DIR_FALLBACK = join(BASE_PATH, 'index_directory_fallback')
FILES_DIR_FALLBACK = join(BASE_PATH, 'emoji_search_files_fallback')



# NLTK path pointing
nltk.data.path.append(os.path.join('emojifi_site', 'emojifi', 'analyzer', 'nltkdata'))


def create_index(index_dir, files_dir):
    schema = Schema(
        title=TEXT(stored=True),
        content=TEXT(stored=True),
        textdata=TEXT(stored=True),
    )

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    ix = index.create_in(index_dir, schema)

    writer = ix.writer()

    files_names_to_index = [join(files_dir, f) for f in listdir(files_dir) if isfile(join(files_dir, f))]

    for file_name in files_names_to_index:
        with open(file_name, 'r') as file:
            print(file_name)
            base_name = os.path.basename(file_name)
            emoji_desc = ''.join(file.readlines())

            # NLTK lemmatize the name and description, since we lem the input word in analyzer
            emoji_desc = ' '.join([WordNetLemmatizer().lemmatize(w, pos='v') for w in emoji_desc.split()])

            print('title', base_name)
            print('content', emoji_desc)
            writer.add_document(
                title=str(base_name),
                content=emoji_desc,
                textdata=emoji_desc,
            )

    writer.commit()


if __name__ == '__main__':
    create_index(INDEX_DIR, FILES_DIR)
    create_index(INDEX_DIR_FALLBACK, FILES_DIR_FALLBACK)
