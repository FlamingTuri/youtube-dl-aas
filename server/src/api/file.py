from src.service.downloader_service import DownloaderService
from src.restx_config import api
from flask_restx import Resource, fields
from flask import send_from_directory, send_file

ns = api.namespace('youtube-dl', description='Download operations')

downloader_service = DownloaderService()

@ns.route('/file/<name>')
class File(Resource):

    def get(self, name):
        try:
            download_folder = downloader_service.config.get_download_folder()
            return send_from_directory(download_folder, filename=name, as_attachment=True)
        except FileNotFoundError:
            return abort(404)


@ns.route('/files')
class Files(Resource):

    def post(self):
        body = api.payload

        if not body:
            return abort(404)

        requested_files = set(body)

        zipfile_name = 'ZipFile.zip'

        zip_file = downloader_service.zip_files(requested_files)

        return send_file(
            zip_file,
            mimetype='application/zip',
            as_attachment=True,
            attachment_filename=zipfile_name
        )
