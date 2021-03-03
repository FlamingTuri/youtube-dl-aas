import youtube_dl
from pathlib import Path
from src.youtube_dl_progress_hook import YoutubeDlProgressHook
from src.restx_config import api
from flask_restx import Resource, fields


ns = api.namespace('youtube-dl', description='Download operations')

progress_hook = YoutubeDlProgressHook()

bad_request_code = 400
default_download_folder = Path.home().joinpath('Downloads', 'youtube-dl')
default_output_template = '%(title)s.%(ext)s'
default_ydl_opts = {
    'progress_hooks': [progress_hook.progress_hook],
    'outtmpl': str(default_download_folder.joinpath(default_output_template))
}

download = api.model('Download', {
    'urls': fields.List(fields.String(), required = True),
    'ydlOpts': fields.Wildcard(fields.String(), required = False)
})

@ns.route('/download')
class Download(Resource):
    '''TODO'''

    @ns.doc('dowloads video on filesystem')
    @ns.expect(download)
    @ns.marshal_with(download, code=200)
    def post(self):
        print(api.payload)
        return api.payload
        """if request.is_json:
            body = request.get_json()
            schema = DownloadEntrySchema()
            try:
                result = schema.load(body)
                with youtube_dl.YoutubeDL(default_ydl_opts) as ydl:
                    ydl.download(result.urls)
                    return progress_hook.get_download_file_location()
            except ValidationError as err:
                return jsonify(err.messages), 400
        else:
            abort(bad_request_code, 'body must be in json format')"""