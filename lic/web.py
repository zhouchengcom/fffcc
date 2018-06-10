import logging

from flask import Flask, redirect
from flask_cors import CORS

from flask.logging import default_handler

from .config import SetConfig
# from .admin import InitAdmin

from .api.friend import mod as fmod
from .api.contancts import mod as cmod
from .api.login import mod as lmod

# root.addHandler(mail_handler)

app = Flask(__name__)

app.config['TRAP_BAD_REQUEST_ERRORS'] = True

if "gunicorn.error" in logging.Logger.manager.loggerDict:
    logging.root = logging.getLogger("gunicorn.error")
    app.logger.addHandler(logging.getLogger("gunicorn.error"))
    app.logger.setLevel(logging.getLogger("gunicorn.error").level)
 



if not app.config.from_envvar('LICCONFIG', silent=True):
    app.config.from_pyfile('../licconfig.py')


CORS(app)


# 
app.register_blueprint(fmod)
app.register_blueprint(cmod)
app.register_blueprint(lmod)

# InitAdmin(app)
@app.route('/')
def index():
    return redirect("baidu.com")