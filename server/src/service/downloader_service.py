import youtube_dl
from src.youtube_dl_progress_hook import YoutubeDlProgressHook
from src.config import Config
from io import BytesIO
import zipfile
from flask import safe_join
import os

class DownloaderService:

    progress_hook = YoutubeDlProgressHook()

    config = Config()
    default_output_template = '%(title)s.%(ext)s'

    default_ydl_opts = {
        'progress_hooks': [progress_hook.progress_hook],
        'outtmpl': config.get_as_path_in_download_folder(default_output_template)
    }

    def download(self, urls: set, ydl_opts: dict = None) -> list: 
        if ydl_opts is None or not ydl_opts:
            ydl_opts = self.default_ydl_opts
        else:
            ydl_opts.update(self.default_ydl_opts)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
            return self.progress_hook.get_downloaded_files_locations()

    def zip_files(self, files: list) -> BytesIO:
        download_folder = self.config.get_download_folder()
        
        in_memory_zip = BytesIO()
        with zipfile.ZipFile(in_memory_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file in files:
                data = zipfile.ZipInfo(safe_join(download_folder, file))
                zf.writestr(data, file)
        in_memory_zip.seek(0)

        return in_memory_zip

    def load_file(self, file: str) -> BytesIO:
        download_folder = self.config.get_download_folder()
        with open(safe_join(download_folder, file), 'rb') as fh:
            return BytesIO(fh.read())

    def remove_file(self, file: str) -> None:
        download_folder = self.config.get_download_folder()
        os.remove(safe_join(download_folder, name))
