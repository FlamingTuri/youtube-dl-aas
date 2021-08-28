from src.restx_config import app, api
from src.api.download import ns as download_namespace
from src.api.download_and_send import ns as download_and_send_namespace
from src.api.file import ns as file_namespace
from src.api.doc import ns as doc_namespace


def init(flask_app):
    api.add_namespace(download_namespace)
    api.add_namespace(download_and_send_namespace)
    api.add_namespace(file_namespace)
    api.add_namespace(doc_namespace)


if __name__ == '__main__':
    app.run()
