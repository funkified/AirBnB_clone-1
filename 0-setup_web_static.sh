#!/usr/bin/env bash
# Setup web servers for the deployment of web_static

apt-get -y update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html>
        <head>
        </head>
        <body>
          Holberton School
        </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i '49i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
