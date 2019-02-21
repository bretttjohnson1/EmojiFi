#! /bin/bash
read -p "This script is for first time install. Are you sure? " -n 2 -r
echo    # (optional) move to a new line
if [[ !($REPLY =~ ^[Yy]$) ]]
then
    exit
fi
echo "Installing:"

sudo apt-get install build-essential python3-dev -y
sudo apt install make -y
sudo apt-get install -y nginx
sudo ln -s /home/ubuntu/EmojiFi/config/emojifi_nginx.conf /etc/nginx/sites-enabled/
make setup-aws
sudo ln -s /home/ubuntu/EmojiFi/config/emojifi_uwsgi.ini /etc/uwsgi/vassals/
sudo chgrp -R www-data /home/ubuntu/EmojiFi/
sudo chmod -R g+rw /home/ubuntu/EmojiFi/
sudo usermod -a -G www-data ubuntu
sudo apt-get install -y supervisor
sudo ln -s /home/ubuntu/EmojiFi/config/uwsgi_supervisord.conf /etc/supervisor/conf.d/
