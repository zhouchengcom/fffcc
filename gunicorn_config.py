bind = '0.0.0.0:9988'
workers = 4
worker_class = 'gevent'
worker_connections = 100
accesslog = "log/access.log"
errorlog = '-'
loglevel = 'debug'
daemon = False
timeout = 120