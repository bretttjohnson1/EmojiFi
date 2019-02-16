SHELL:=/bin/bash
PROJECT:=code_chain
run:
	python emojifi_site/manage.py runserver 0:8000

migrate:
	emojifi_site/manage.py migrate

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
	python -m nltk.downloader -d ./emojifi_site/emojifi/analyzer/nltkdata/ all

clean:
	rm -rf venv/
	rm -rf *.egg-info

pre-commit:
	pre-commit install
	pre-commit install-hooks
