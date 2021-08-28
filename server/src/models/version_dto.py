class VersionDto:

    def __init__(self, serverVersion: str, youtubeDlVersion: str):
        self.__serverVersion = serverVersion
        self.__youtubeDlVersion = youtubeDlVersion

    @property
    def serverVersion(self) -> str:
        return self.__serverVersion

    @property
    def youtubeDlVersion(self) -> str:
        return self.__youtubeDlVersion
