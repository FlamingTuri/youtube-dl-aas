from youtube_dl import YoutubeDL
from models.doc_dto import DocDto


class DocService:

    def get_youtube_dl_doc(self) -> DocDto:
        return DocDto(YoutubeDL.__doc__)
