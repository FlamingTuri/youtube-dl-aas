import youtube_dl
from pathlib import Path

default_download_folder = Path.home().joinpath('Downloads', 'youtube-dl')
default_output_template = '%(title)s.%(ext)s'
ydl_opts = {
    'outtmpl': str(default_download_folder.joinpath(default_output_template))
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
