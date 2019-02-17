from bs4 import BeautifulSoup
import os
import string
from os import listdir
from os.path import isfile, join
import json
import shutil
import emoji



BASE_PATH = os.path.dirname(os.path.abspath(__file__))

STOPWORD_PATH = 'stopwords.txt'

html_path = os.path.join(BASE_PATH, 'html_docs')

def _plaintext_hex_to_unicode(code):
    return chr(int(code, 16))

def refresh_dir(directory):
    if os.path.exists(join(BASE_PATH, directory)):
        shutil.rmtree(join(BASE_PATH, directory))
    os.mkdir(join(BASE_PATH, directory))


refresh_dir(join(BASE_PATH, f'emoji_search_files'))
refresh_dir(join(BASE_PATH, f'emoji_search_files_fallback'))


def load_stopwords():
    """ Reads the stopwords file and loads it into a set """
    with open(os.path.join(BASE_PATH, STOPWORD_PATH)) as f:
        return set(f.read().splitlines())


stop_words = load_stopwords()


html_files = [join(html_path, f) for f in listdir(html_path) if isfile(join(html_path, f))]
count = 0
for html_file in html_files:

    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, features="html5lib")
    html_names = soup.body.find_all('b')
    for entry in soup.body.find_all(text=True):
        cleaned = entry.strip()
        if 'U+' in cleaned:
            desc, unicode = cleaned.split('\n')
            unicode = unicode.strip(' ').strip('U+')
            desc = desc.lower().strip('“').strip('”')
            desc = ''.join(c for c in desc if c not in {'“','”','.','“','🤜','🤛'})
            desc_set = set(filter(
                lambda word: word not in stop_words,
                desc.split(' '))
            )
            desc_list = [
                word.translate(str.maketrans('', '', string.punctuation))
                for word in desc.split(' ')
            ]
            desc_list = list(filter(
                lambda word: word not in stop_words,
                desc_list
            ))

            name = html_names.pop(0).text.lower()
            name = ' '.join(filter(lambda x: x not in stop_words, name.split(' ')))
            emoji_alias = emoji.demojize(_plaintext_hex_to_unicode(unicode))
            output_file_path = join(BASE_PATH, f'emoji_search_files_fallback/{emoji_alias}')
            if not os.path.exists(output_file_path):
                with open(output_file_path, 'w') as emoji_file:
                    emoji_file.write(' '.join(desc_list))
                    print(emoji_alias, '#', name, '#', ','.join(desc_list))
            count += 1
print(count, 'files')


with open(join(BASE_PATH, 'emojis.json')) as f:
    emojis_json = json.load(f)

for name, data in emojis_json.items():
    emoji_alias = emoji.demojize(data['char'])

    output_file_path = join(BASE_PATH, f'emoji_search_files/{emoji_alias}')
    if not os.path.exists(output_file_path):
        with open(output_file_path, 'w') as emoji_file:
            emoji_file.write(' '.join(data['keywords']))
            print(emoji_alias, '#', name, '#', ','.join(data['keywords']))
