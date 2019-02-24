from emojisearch.search_engine_setup.emoji_file import EmojiFile
import json


def generate_search_files_from_emoji_json(corpus_file_path, emoji_file_directory):

    with open(corpus_file_path) as f:
        emojis_json = json.load(f)

    for name, data in emojis_json.items():
        emoji = data['char']
        description = ' '.join(data['keywords'])
        EmojiFile(emoji, name, description).write(emoji_file_directory)
