from src.service.downloader_service import DownloaderService
from src.restx_config import api
from flask_restx import Resource, fields, reqparse
from flask import send_from_directory, send_file

ns = api.namespace('youtube-dl', description='Download operations')

downloader_service = DownloaderService()

@ns.route('/file/<name>')
class File(Resource):

    def get(self, name):
        try:
            file = downloader_service.load_file(name)

            return send_file(
                file.content,
                as_attachment=True,
                attachment_filename=file.name
            )
        except FileNotFoundError:
            return abort(404)

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

        return send_file(
            zip_file.content,
            mimetype='application/zip',
            as_attachment=True,
            attachment_filename=zip_file.name
        )
