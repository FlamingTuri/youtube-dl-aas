import youtube_dl
from pathlib import Path
from flask import Flask, request, abort, jsonify
from marshmallow import ValidationError

from src.youtube_dl_progress_hook import YoutubeDlProgressHook
from src.download_entry_schema import DownloadEntrySchema

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
        schema = DownloadEntrySchema()
        try:
            result = schema.load(body)
            with youtube_dl.YoutubeDL(default_ydl_opts) as ydl:
                ydl.download(result.urls)
                return progress_hook.get_download_file_location()
        except ValidationError as err:
            return jsonify(err.messages), 400
    else:
        abort(bad_request_code, 'body must be in json format')
