import logging
from flask import Flask
from flask_restx import Api
from flask_cors import CORS

log = logging.getLogger(__name__)

app = Flask(__name__)
app.config['RESTX_VALIDATE'] = True
app.config['CORS_EXPOSE_HEADERS'] = 'Content-Disposition'
CORS(app)

api = Api(version='1.0', title='Youtube dl as a service API')
api.init_app(app)

@api.errorhandler
def default_error_handler(error: Exception):
    #log.exception(error)
    return {'message': str(error)}, 500
