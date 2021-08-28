import youtube_dl
from src.models.version_dto import VersionDto


class VersionService:

    def get_version(self) -> VersionDto:
        return VersionDto('TODO', youtube_dl.version.__version__)
