#!/usr/bin/env bash
#  a Bash script that sets up your web servers for the deployment of web_static
#!/usr/bin/env bash
#  a Bash script that sets up your web servers for the deployment of web_static
sudo apt -y update
sudo apt -y install nginx
mkdir -p "/data/"
mkdir -p "/data/web_static/"
mkdir -p "/data/web_static/releases/"
mkdir -p "/data/web_static/shared/"
mkdir -p "/data/web_static/releases/test/"
printf "<html>\n\t<head>\n</head>\n<body>\n\t\tHolberton School\n\t</body>\n</html>" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
old_str="server_name _;"
new_str="server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s|${old_str}|${new_str}|g" /etc/nginx/sites-available/default
sudo service nginx restart

