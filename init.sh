# # sudo unlink /etc/nginx/sites-enabled/default
# sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
# sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/gunicorn restart
gunicorn --bind='http://127.0.0.1:8000' hello:app


