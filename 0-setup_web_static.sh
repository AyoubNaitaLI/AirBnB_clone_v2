#!/usr/bin/env bash
# Preparing the servers
host=$(hostname);
sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80 ;
    listen [::]:80;
    root /var/www/html;
    index index.html;
    server_name _;
    add_header X-Served-By $host;
    error_page 404 /custom_404.html;
    location = /custom_404.html {
    	root /var/www/html;
	internal;
    }
    location /redirect_me {
	return 301 /;
    }
    location /hbnb_static/ {
	alias /data/web_static/current/;
    }
}" | sudo tee /etc/nginx/sites-available/default;
sudo service nginx restart
