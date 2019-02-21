SHELL:=/bin/bash

run:
	( \
		source venv/bin/activate; \
		python emojifi_site/manage.py runserver 0:8000; \
	)

run-bot:
	( \
		source venv/bin/activate; \
		python reddit_bot/redditbot.py; \
	)

#Sets up the full project on dev. Call setup-aws if on aws instead.
setup-project: install-python-packages nltk migrate index-data

install-python-packages:
	python3.6 -m venv venv
	( \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
		pip install -e emoji_search/ \
	)

nltk:
	./install_nltk.bash

migrate:
	( \
		source venv/bin/activate; \
		emojifi_site/manage.py migrate; \
		python emojifi_site/manage.py collectstatic; \
	)

index-data:
	( \
		source venv/bin/activate; \
		python emoji_search/emojisearch/generate_emoji_search_files.py; \
		python emoji_search/emojisearch/create_whoosh_index.py; \
	)

#Aws specific build. Should not be called in debug
setup-aws: setup-project install-packages-aws link-configs-aws configure-permissions-aws
	( \
		source venv/bin/activate; \
		python emojifi_site/manage.py collectstatic; \
	)

install-packages-aws:
	sudo apt-get install build-essential python3-dev -y
	sudo apt install make -y
	sudo apt-get install -y nginx
	sudo apt-get install -y supervisor

link-configs-aws:
	sudo ln -s /home/ubuntu/EmojiFi/config/emojifi_nginx.conf /etc/nginx/sites-enabled/
	sudo ln -s /home/ubuntu/EmojiFi/config/emojifi_uwsgi.ini /etc/uwsgi/vassals/
	sudo ln -s /home/ubuntu/EmojiFi/config/uwsgi_supervisord.conf /etc/supervisor/conf.d/

configure-permissions-aws:
	sudo chgrp -R www-data /home/ubuntu/EmojiFi/
	sudo chmod -R g+rw /home/ubuntu/EmojiFi/
	sudo usermod -a -G www-data ubuntu
	sudo apt-get install -y supervisor

clean:
	rm -rf venv/
	rm -rf *.egg-info
