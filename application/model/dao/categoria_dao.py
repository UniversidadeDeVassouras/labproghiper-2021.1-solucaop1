from application.model.entity.video import Video
from application.model.entity.categoria import Categoria

class CategoriaDAO:
    
    def __init__(self):
        video_streetfighter = Video(1, 'Street Fighter', 'Vídeo do Street Fighter', 'img/stf1.jpg', 'video/stf1.mp4', 'video/mp4')
        video_naturo = Video(2, 'Naturo', 'Vídeo de Naruto', 'img/shonen1.jpg', 'video/shonen1.webm', 'video/webm')
        video_desaf_gigantes = Video(3, 'Desafiando Gigantes', 'Vídeo Desafiando Gigantes', 'img/capa_desafiandogigantes.png', 'video/desafiando-gigantes.mp4', 'video/mp4')
        video_mr_sunshine = Video(4, 'Mr. Sunshine', 'Vídeo Mr. Sunshine', 'img/capa_mrsunshine.png', 'video/mr-sunshine.mp4', 'video/mp4')
        categoria_anime = Categoria(1, 'Animes', [video_streetfighter, video_naturo])
        categoria_filme_inter = Categoria(2, 'Filmes Internacionais', [video_mr_sunshine, video_desaf_gigantes])
        self.__categorias = [categoria_anime, categoria_filme_inter]

    def find_all(self):
        return self.__categorias

    def find_video_by_id(self, id:int):
        for categoria in self.__categorias:
            for video in categoria.get_video_list():
                if video.get_id() == id:
                    return video
        return None