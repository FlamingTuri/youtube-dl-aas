import youtube_dl
from pathlib import Path
from src.youtube_dl_progress_hook import YoutubeDlProgressHook
from src.restx_config import api
from flask_restx import Resource, fields
from src.config import Config
from flask import send_from_directory, safe_join, send_file
import zipfile
import os

ns = api.namespace('youtube-dl', description='Download operations')

download_folder = Config().get_download_folder()

@ns.route('/file/<name>')
class File(Resource):

    def get(self, name):
        try:
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
        with zipfile.ZipFile(zipfile_name,'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in requested_files:
                file_path = safe_join(download_folder, file)
                zipf.write(file_path)
            zipf.close()
        
        with open(zipfile_name, 'rb') as f:
            data = f.readlines()

        result = send_file(
            data,
            mimetype='application/zip',
            as_attachment=True,
            attachment_filename=zipfile_name
        )
        os.remove(zipfile_name)
        return result
        #return Response(data, headers={
        #    'Content-Type': 'application/zip',
        #    'Content-Disposition': 'attachment; filename=%s;' % zipfile_name
        #})     
