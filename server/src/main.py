from flask import Flask, Blueprint

from src.restx_config import app, api
from src.api.download import ns as download_namespace

def init(flask_app):
    api.add_namespace(download_namespace)

if __name__ == '__main__':
    app.run()
