class Video:
    
    def __init__(self, id: int, titulo: str, descricao:str, imagem_path: str, video_path: str):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__imagem_path = imagem_path
        self.__video_path = video_path

    def get_id(self) -> int:
        return self.__id
    
    def get_titulo(self) -> str:
        return self.__titulo
    
    def get_descricao(self) -> str:
        return self.__descricao

    def get_imagem_path(self) -> str:
        return self.__imagem_path

    def get_video_path(self) -> str:   
        return self.__video_path