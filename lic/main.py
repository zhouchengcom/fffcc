import logging

from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_mongoengine import MongoEngine

from .minioclient import MinioInit

from .api.debugenv import mod as debugmod
from .api.project import mod as projcetmod
from .api.report import mod as uploadmod
from .api.task import mod as taskmod
from .api.proxy import mod as proxymod
from .api.label import mod as labelmod
from .config import SetConfig
from .user import InitFlaskSecurity
from .admin import InitAdmin
app = Flask(__name__)

if "gunicorn.error" in logging.Logger.manager.loggerDict:
    logging.root = logging.getLogger("gunicorn.error")
    app.logger.addHandler(logging.getLogger("gunicorn.error"))

if not app.config.from_envvar('LICCONFIG', silent=True):
    app.config.from_pyfile('../licconfig.py')



CORS(app)


app.register_blueprint(uploadmod, url_prefix='/api/report')

InitAdmin(app)