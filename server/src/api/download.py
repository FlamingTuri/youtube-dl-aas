import youtube_dl
from pathlib import Path
from src.youtube_dl_progress_hook import YoutubeDlProgressHook
from src.restx_config import api
from flask_restx import Resource, fields


ns = api.namespace('youtube-dl', description='Download operations')

download = api.model('Download', {
    'urls': fields.List(fields.String(), required = True),
    'ydlOpts': fields.Wildcard(fields.String(), required = False)
})

@ns.route('/download')
class Download(Resource):
    '''TODO'''

    progress_hook = YoutubeDlProgressHook()

    default_download_folder = Path.home().joinpath('Downloads', 'youtube-dl')
    default_output_template = '%(title)s.%(ext)s'

    default_ydl_opts = {
        'progress_hooks': [progress_hook.progress_hook],
        'outtmpl': str(default_download_folder.joinpath(default_output_template))
    }

    @ns.doc('downloads videos on filesystem', responses={
        200: 'Success',
        400: 'Validation Error'
    })
    @ns.expect(download)
    @ns.response(200, 'Success', fields.List(fields.String(example="/path/to/downloaded/file")))
    def post(self):
        body = api.payload
        urls = body.get('urls')

        ydl_opts = body.get('ydlOpts', None)
        if ydl_opts is None:
            ydl_opts = self.default_ydl_opts
        else:
            ydl_opts.update(self.default_ydl_opts)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
            return self.progress_hook.get_downloaded_files_locations()
