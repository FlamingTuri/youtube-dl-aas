from pathlib import Path

class Config:

    __default_download_folder = Path.home().joinpath('Downloads', 'youtube-dl')

    def get_download_folder(self) -> str:
        return str(self.__default_download_folder)

    def get_as_path_in_download_folder(self, path: str) -> str:
        return str(self.__default_download_folder.joinpath(path))
    