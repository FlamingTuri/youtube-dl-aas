import logging
from flask import Flask, render_template
from flask_restx import Api
from flask_cors import CORS

log = logging.getLogger(__name__)

app = Flask(__name__, static_folder='resources/static', template_folder='resources/templates')
app.config['RESTX_VALIDATE'] = True
app.config['CORS_EXPOSE_HEADERS'] = 'Content-Disposition'
CORS(app)

api = Api(version='1.0', title='Youtube dl as a service API', doc='/swagger')
api.init_app(app)


@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

@api.errorhandler
def default_error_handler(error: Exception):
    # log.exception(error)
    return {'message': str(error)}, 500
