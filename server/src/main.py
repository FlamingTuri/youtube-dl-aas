import youtube_dl
from pathlib import Path
from flask import Flask
from flask import request
from flask import abort

from src.youtube_dl_progress_hook import YoutubeDlProgressHook

progress_hook = YoutubeDlProgressHook()

bad_request_code = 400
default_download_folder = Path.home().joinpath('Downloads', 'youtube-dl')
default_output_template = '%(title)s.%(ext)s'
default_ydl_opts = {
    'progress_hooks': [progress_hook.progress_hook],
    'outtmpl': str(default_download_folder.joinpath(default_output_template))
}

app = Flask(__name__)

base_route = '/youtube-dl'


@app.route('/')
def index():
    return 'Index Page'


@app.route(f'{base_route}/download', methods=['POST'])
def download():
    if request.is_json:
        body = request.get_json()
        url = body.get('url')
        if url is None:
            abort(bad_request_code, '\'url\' key not defined')

        ydl_opts = body.get('options', default_ydl_opts)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            return progress_hook.get_download_file_location()
    else:
        abort(bad_request_code, 'body must be in json format')
