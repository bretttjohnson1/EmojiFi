from bs4 import BeautifulSoup
import os
import string
from os import listdir
from os.path import isfile, join
mypath = 'html_docs'

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

STOPWORD_PATH = 'stopwords.txt'


def load_stopwords():
    """ Reads the stopwords file and loads it into a set """
    with open(os.path.join(BASE_PATH, STOPWORD_PATH)) as f:
        return set(f.read().splitlines())


stop_words = load_stopwords()


html_files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
count = 0
for html_file in html_files:

    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, features="html5lib")
    for entry, name_html in zip(soup.body.find_all(text=True), soup.body.find_all('b')):
        name = name_html.text.lower()
        name = ' '.join(filter(lambda x: x not in stop_words, name.split(' ')))
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

            output_file_path = join(BASE_PATH, f'emoji_search_files/{unicode}')
            if not os.path.exists(output_file_path):
                with open(output_file_path, 'w') as emoji_file:
                    emoji_file.write(name+';'+' '.join(desc_list))
                    print(unicode, '#', name, '#', ','.join(desc_list))
            count += 1
print(count,'files')
