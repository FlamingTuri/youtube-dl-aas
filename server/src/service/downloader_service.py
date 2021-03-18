import youtube_dl
from src.youtube_dl_progress_hook import YoutubeDlProgressHook
from src.config import Config

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