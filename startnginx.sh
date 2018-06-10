nginx -s stop && echo stop
nginx && echo start
tail -f /usr/local/Cellar/nginx/1.15.0/logs/host.access.log