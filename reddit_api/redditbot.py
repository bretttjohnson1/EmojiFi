import praw
import requests
from time import sleep
import json

reddit = praw.Reddit('bot')

while True:
	for item in reddit.inbox.unread(limit=None):
		subject = item.subject.lower()
		if subject == 'username mention' and isinstance(item, praw.models.Comment):
			parent = item.parent()
			payload = {'text': parent.body,
					   'type': 'search'}
			print(parent.body)
			try:
				r = requests.post('http://3.18.14.202:80/emojifi', data=json.dumps(payload))
				finaltext = r.json()
				print(finaltext['text'])
				reply = item.reply(finaltext['text'] + '\n\n ============================= \n   I am a bot. I was made by /u/HotBrass.'
												   	   ' \n   You can find a frontend at http://bit.do/emojify')
				item.mark_read()
			except Exception:
				pass
	sleep(10)


# 3.18.14.202:80
