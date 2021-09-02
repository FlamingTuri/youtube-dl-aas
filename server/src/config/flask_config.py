import os
import sys
from flask import Flask, render_template
from flask_cors import CORS

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


@app.route('/home', methods=['GET'])
@app.route('/home/', methods=['GET'])
def index():
    return render_template('index.html')

from src.config.flask_restx_config import api

api.init_app(app)
