import praw
import pdb
import re
import os

reddit = praw.Reddit('bot')

for item in reddit.inbox.unread(limit=None):
	subject = item.subject.lower()
	if subject == 'username mention' and isinstance(item, praw.models.Comment):
		parent = item.parent()
#		print(parent.body)
		reply = item.reply('Hello!')
		item.mark_read()