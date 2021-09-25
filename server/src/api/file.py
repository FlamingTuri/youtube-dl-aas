from flask import send_file, abort
from flask.wrappers import Response
from flask_restx import Resource
from src.config.flask_restx_config import api, ns
from src.models.file_info import FileInfo
from src.service.downloader_service import DownloaderService


downloader_service = DownloaderService()


def send(file_info: FileInfo) -> Response:
    return send_file(
            file_info.content,
            mimetype=file_info.mimetype,
            as_attachment=True,
            attachment_filename=file_info.name
    )


@ns.route('/file/<name>')
class File(Resource):

    @api.param('name', 'The name of a previously downloaded file that should be sent to your device')
    def get(self, name):
        try:
            file = downloader_service.load_file(name)

            return send(file)
        except FileNotFoundError:
            return abort(404)

    @api.param('name', 'The name of a previously downloaded file that should be deleted')
    def delete(self, name):
        try:
            downloader_service.remove_file(name)
            return
        except FileNotFoundError:
            return abort(404)


@ns.route('/files')
class Files(Resource):

    def post(self):
        body = api.payload

        if not body:
            return abort(404)

        requested_files = set(body)

        zip_file = downloader_service.zip_files(requested_files)

        return send(zip_file)
