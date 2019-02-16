import praw
import requests

reddit = praw.Reddit('bot')

for item in reddit.inbox.unread(limit=None):
	subject = item.subject.lower()
	if subject == 'username mention' and isinstance(item, praw.models.Comment):
		parent = item.parent()
		payload = {'text': parent.body(),
				   'type': 'search'}
		r = requests.post('127.0.0.1', data=None, json=payload)
		r = requests.get('127.0.0.1')
		payload = r.json()
		reply = item.reply(payload['text'] + '/n /n ^I am a bot. I was made by /u/HotBrass.')
		item.mark_read()