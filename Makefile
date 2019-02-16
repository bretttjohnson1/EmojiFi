SHELL:=/bin/bash
PROJECT:=code_chain

install-all: install nltk migrate

run-aws:
	( \
		source venv/bin/activate; \
		python emojifi_site/manage.py runserver 0:80; \
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

nltk:
	./install_nltk.bash

clean:
	rm -rf venv/
	rm -rf *.egg-info
