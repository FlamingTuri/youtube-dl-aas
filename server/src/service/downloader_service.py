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

    def download(self, urls: set, ydl_opts: dict = None, temporary: bool = False) -> list: 
        download_folder = self.config.get_download_folder(temporary)
        outtmpl = self.config.get_as_path_in_download_folder(default_output_template, download_folder)
        default_ydl_opts = { 'outtmpl': outtmpl }
        if ydl_opts is None or not ydl_opts:
            ydl_opts = default_ydl_opts
        else:
            ydl_opts.update(default_ydl_opts)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
            # ideally the downloaded files should be returned, however, 
            # due to https://github.com/ytdl-org/youtube-dl/issues/5710,
            # it is not possible and the download location is returned instead
            return download_folder

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
