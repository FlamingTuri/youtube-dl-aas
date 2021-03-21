from pathlib import Path
from datetime import datetime

class Config:

    __default_download_folder = Path.home().joinpath('Downloads', 'youtube-dl')

    __time_format = '%Y-%m-%d h%H m%M s%S'

    def get_download_folder(self, temporary: bool = False) -> str:
        if temporary:
            now = datetime.now().strftime(self.__time_format)
            return str(self.__default_download_folder.joinpath(now))
        else:
            return str(self.__default_download_folder)

    def get_as_path_in_download_folder(self, path: str, download_folder: str = __default_download_folder) -> str:
        return str(self.__default_download_folder.joinpath(path))
