#!/usr/bin/env bash
# Setup web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo echo "This better work" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '49i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
