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

    @ns.doc('downloads videos on filesystem', responses={
        200: 'Success',
        400: 'Validation Error'
    })
    @ns.expect(download)
    #@ns.marshal_with(download, code=200)
    def post(self):
        body = api.payload
        print(body)
        print(type(body))
        urls = body.get('urls')
        print(urls)
        with youtube_dl.YoutubeDL(default_ydl_opts) as ydl:
            ydl.download(urls)
            return progress_hook.get_downloaded_files_locations()
