import praw
import requests
from time import sleep
import json


reddit = praw.Reddit('bot')


def mention_to_payload(mention):
    """ Converts a mention comment to a payload for POST """
    return {'text': mention.parent().body, 'type': 'search'}


def reply_to_mention(mention, payload):
    """ Replies to a mention with the emojify'd text """
    try:
        request_response = requests.post('http://emojifythis.org/emojifi', data=json.dumps(payload))
        json_response = request_response.json()
        mention.reply(json_response['text'] + '\n\n ============================= \n   I am a bot. '
                                          '\n   My source code is at https://github.com/bretttjohnson1/EmojiFi/ '
                                          '\n   Our website is at http://emojifythis.org')
        mention.mark_read()
    except Exception:
        pass


def is_mention(message):
    subject = message.subject.lower()
    return subject == 'username mention' and isinstance(message, praw.models.Comment)


def run_bot():
    while True:
        for message in reddit.inbox.unread(limit=None):
            if is_mention(message):
                payload = mention_to_payload(message)
                reply_to_mention(message, payload)

        sleep(10)


if '__name__' == '__main__':
    run_bot()
