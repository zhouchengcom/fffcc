import logging

from flask import Flask
from flask_cors import CORS



from .config import SetConfig
# from .admin import InitAdmin
app = Flask(__name__)

# if "gunicorn.error" in logging.Logger.manager.loggerDict:
#     logging.root = logging.getLogger("gunicorn.error")
#     app.logger.addHandler(logging.getLogger("gunicorn.error"))

if not app.config.from_envvar('LICCONFIG', silent=True):
    app.config.from_pyfile('../licconfig.py')



CORS(app)


# app.register_blueprint(uploadmod, url_prefix='/api/report')

# InitAdmin(app)