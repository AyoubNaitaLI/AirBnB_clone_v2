# Making directories for static content
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => 'shell',
}
exec { 'install nginx':
  command  => 'sudo apt-get install -y nginx',
  provider => 'shell',
}
exec { 'data':
  command  => 'sudo mkdir -p /data/',
  provider => 'shell',
}
exec { 'data/web_static':
  command  => 'sudo mkdir -p /data/web_static/',
  provider => 'shell',
}
exec { 'releases':
  command  => 'sudo mkdir -p /data/web_static/releases/',
  provider => 'shell',
}
exec { 'shared':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => 'shell',
}
exec { 'test':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => 'shell',
}
exec { 'index.html':
  command  => 'echo "Hello" | sudo tee /data/web_static/releases/test/index.html',
  provider => 'shell',
}
exec { 's_link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell',
}
exec { 'chown':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => 'shell',
}
$hostname = $facts['::environment']['HOSTNAME']
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 ;
    listen [::]:80;
    root /var/www/html;
    index index.html;
    server_name _;
    add_header X-Served-By ${hostname};
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
  }",
}
exec { 'nginx restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
