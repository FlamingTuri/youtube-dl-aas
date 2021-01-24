import youtube_dl
from pathlib import Path
from flask import Flask

default_download_folder = Path.home().joinpath('Downloads', 'youtube-dl')
default_output_template = '%(title)s.%(ext)s'
ydl_opts = {
    'outtmpl': str(default_download_folder.joinpath(default_output_template))
}

app = Flask(__name__)

base_route = '/youtube-dl'


@app.route('/')
def index():
    return 'Index Page'


@app.route(f'${base_route}/download', method=['POST'])
def download():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    return 'success'
