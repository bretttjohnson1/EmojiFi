SHELL:=/bin/bash
PROJECT:=code_chain

install-all: install nltk migrate

run-aws:
	( \
		source venv/bin/activate; \
		python emojifi_site/manage.py runserver 0:80; \
	)

run-bot:
	( \
		source venv/bin/activate; \
		python reddit_api/redditbot.py; \
	)

run:
	( \
		source venv/bin/activate; \
		python emojifi_site/manage.py runserver 0:8000; \
	)

migrate:
	( \
		source venv/bin/activate; \
		emojifi_site/manage.py migrate; \
	)
test:
	( \
		source venv/bin/activate; \
		pytest emojifi_site/emojifi
	)
install:
	python3.6 -m venv venv
	( \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
		pip install -e emoji_search/ \
	)
index-data:
	( \
		source venv/bin/activate; \
		python emoji_search/emojisearch/generate_emoji_search_files.py; \
		python emoji_search/emojisearch/create_whoosh_index.py; \
	)
nltk:
	./install_nltk.bash

clean:
	rm -rf venv/
	rm -rf *.egg-info
