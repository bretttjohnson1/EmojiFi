SHELL:=/bin/bash
PROJECT:=code_chain
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
clean:
	rm -rf venv/
	rm -rf *.egg-info

pre-commit:
	pre-commit install
	pre-commit install-hooks
