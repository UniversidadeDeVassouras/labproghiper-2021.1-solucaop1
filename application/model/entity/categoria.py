from typing import List
from application.model.entity.video import Video

class Categoria:

    def __init__(self, id: int, nome: str, video_list: List[Video]):
        self.__id = id
        self.__nome = nome
        self.__video_list = video_list
    
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome
    
    def get_video_list(self) -> List[Video]:
        return self.__video_list