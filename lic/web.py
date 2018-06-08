import logging

from flask import Flask
from flask_cors import CORS

from flask.logging import default_handler


from .config import SetConfig
# from .admin import InitAdmin


# root.addHandler(mail_handler)

app = Flask(__name__)


if "gunicorn.error" in logging.Logger.manager.loggerDict:
    logging.root = logging.getLogger("gunicorn.error")
    app.logger.addHandler(logging.getLogger("gunicorn.error"))


    
# if "gunicorn.error" in logging.Logger.manager.loggerDict:
#     logging.root = logging.getLogger("gunicorn.error")
#     app.logger.addHandler(logging.getLogger("gunicorn.error"))

if not app.config.from_envvar('LICCONFIG', silent=True):
    app.config.from_pyfile('../licconfig.py')



CORS(app)

logging.info("start aaaa")
app.logger.info("dsfsdf")

# app.register_blueprint(uploadmod, url_prefix='/api/report')

# InitAdmin(app)