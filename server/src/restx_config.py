import logging
from flask import Flask
from flask_restx import Api

log = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(version='1.0', title='Youtube dl as a service API')
api.init_app(app)

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(e)
    return {'message': message}, 500
