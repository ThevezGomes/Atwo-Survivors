import pygame as pg
import sys
from pytmx.util_pygame import load_pygame
from pytmx import pytmx  # Certifique-se de que a importação de pytmx está correta

class Tile(pg.sprite.Sprite):
    """
    Classe que representa cada tile no mapa.

    Atributos:
        image (pygame.Surface): Superfície gráfica do tile.
        rect (pygame.Rect): Retângulo delimitador da superfície, usado para posicionamento e colisão.
    """

    def __init__(self, pos, surf, groups):
        """
        Inicia um novo tile.

        Argumentos:
            pos (tuple): Posição do canto superior esquerdo do tile no mapa (x, y).
            surf (pygame.Surface): Superfície gráfica a ser usada para o tile.
            groups (list): Lista de grupos onde o tile será adicionado.
        """
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

    def scale(self, width, height):
        """
        Redimensiona o tile para uma nova largura e altura.

        Args:
            width (int): Nova largura do tile.
            height (int): Nova altura do tile.
        """
        self.image = pg.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def transform_tile_image(tile_image, gid):
        """
        Aplica transformações na imagem do tile com base no GID (Global ID).

        As transformações incluem:
        - Virar horizontalmente.
        - Virar verticalmente.
        - Rotação diagonal (90 graus).

        Argumentos:
            tile_image (pygame.Surface): Superfície gráfica do tile.
            gid (int): Global ID do tile, contendo informações de transformação.

        Retorna:
            pygame.Surface: Imagem transformada.
        """
        # Extraindo as flags de transformação dos bits do GID
        flipped_horizontally = bool(gid & 0x80000000)  # Verifica o bit mais à esquerda (flip horizontal)
        flipped_vertically = bool(gid & 0x40000000)    # Verifica o bit para flip vertical
        flipped_diagonally = bool(gid & 0x20000000)    # Verifica o bit para rotação diagonal

        # Cria a instância de TileFlags com as flags extraídas
        tile_flags = pytmx.TileFlags(flipped_horizontally, flipped_vertically, flipped_diagonally)

        # Aplica as transformações usando as flags
        if tile_flags.flipped_horizontally or tile_flags.flipped_vertically:
            tile_image = pg.transform.flip(tile_image, tile_flags.flipped_horizontally, tile_flags.flipped_vertically)

        if tile_flags.flipped_diagonally:
            tile_image = pg.transform.rotate(tile_image, 90)

        return tile_image

    def transform_object_image(obj, gid, offset_x, offset_y):
        """
        Aplica transformações na imagem associada a um objeto do mapa.

        As transformações incluem ajustes de posição e rotação com base nas flags do GID.

        Argumentoss:
            obj (pytmx.TiledObject): Objeto do mapa contendo a imagem e informações de posicionamento.
            gid (int): Global ID do objeto, contendo informações de transformação.
            offset_x (int): Deslocamento horizontal para centralizar o objeto no mapa.
            offset_y (int): Deslocamento vertical para centralizar o objeto no mapa.

        Retorna:
            Tile: atribuição do Tile representando o objeto transformado.
        """
        # Aplica transformações na imagem associada ao objeto
        obj_image = Tile.transform_tile_image(obj.image, gid)

        # Calcula a posição do objeto com o offset
        pos = (obj.x - offset_x, obj.y - offset_y)

        # Cria o sprite de objeto
        tiled_obj_sprite = Tile(pos, obj_image, [self.all_sprites])
        return tiled_obj_sprite
