from io import BytesIO

class File:

    def __init__(self, name: str, content: BytesIO):
        self.__name = name
        self.__content = content

    @property
    def name(self) -> str:
        return self.__name

    @property
    def content(self) -> BytesIO:
        return self.__content
