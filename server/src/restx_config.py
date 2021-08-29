import logging
import os
import sys
from flask import Flask, render_template
from flask_restx import Api
from flask_cors import CORS

log = logging.getLogger(__name__)

pyinstaller_temp_folder = getattr(sys, '_MEIPASS', None)

def resource_path(relative_path):
    if pyinstaller_temp_folder == None:
        # not running in pyinstaller bundle
        return relative_path
    else:
        return os.path.join(pyinstaller_temp_folder, relative_path)

resources_folder = 'resources'
app = Flask(
    __name__,
    static_folder=resource_path(os.path.join(resources_folder, 'home')),
    template_folder=resource_path(os.path.join(resources_folder, 'templates'))
)
app.config['RESTX_VALIDATE'] = True
app.config['CORS_EXPOSE_HEADERS'] = 'Content-Disposition'
CORS(app)

api = Api(version='1.0', title='Youtube dl as a service API', doc='/swagger')
api.init_app(app)


@app.route('/home', methods=['GET'])
@app.route('/home/', methods=['GET'])
def index():
    return render_template('index.html')

@api.errorhandler
def default_error_handler(error: Exception):
    # log.exception(error)
    return {'message': str(error)}, 500
