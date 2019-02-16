SHELL:=/bin/bash
PROJECT:=code_chain
run:
	emojifi_site/manage.py runserver 0:8000

migrate:
	emojifi_site/manage.py migrate

test:
	( \
		source venv/bin/activate; \
		tox; \
	)
install:
	python3.6 -m venv venv
	( \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)
clean:
	rm -rf venv/
	rm -rf *.egg-info

pre-commit:
	pre-commit install
	pre-commit install-hooks
