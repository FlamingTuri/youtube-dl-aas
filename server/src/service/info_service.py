import socket


class InfoService:

    __host_name = "unknown"

    def __init__(self) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.__host_name = s.getsockname()[0]
        s.close()

    def get_host_name(self) -> str:
        return self.__host_name
