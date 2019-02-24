import os.path
import emoji
import uuid


class EmojiFile():

    content_split_symbol = ';;;'

    def __init__(self, unicode_emoji, search_content):
        self.unicode_emoji = unicode_emoji
        self.search_content = search_content

    def write(self, directory):
        file_path = os.path.join(directory, uuid.uuid4().hex)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as emoji_file:
                file_content = f'{self.unicode_emoji}{EmojiFile.content_split_symbol}{self.search_content}'
                emoji_file.write(file_content)

    @staticmethod
    def read(file_path):
        with open(file_path, 'r') as file:
            file_content = ''.join(file.readlines())
            emoji_alias, search_content = file_content.split(EmojiFile.content_split_symbol)

        return EmojiFile(emoji_alias, search_content)
