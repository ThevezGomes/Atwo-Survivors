import pygame as pg
import sys
from pytmx.util_pygame import load_pygame
from pytmx import pytmx  # Certifique-se de que a importação de pytmx está correta

# Classe para representar cada tile no mapa
class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

    def scale(self, width, height):
        """Escala o tile para as dimensões fornecidas"""
        self.image = pg.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    # Função para aplicar transformações nos tiles
    def transform_tile_image(tile_image, gid):
   
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
        # Aplica transformações na imagem associada ao objeto
        obj_image = transform_object_image(obj.image, gid)

        # Calcula a posição do objeto com o offset
        pos = (obj.x - offset_x, obj.y - offset_y)

        # Cria o sprite de objeto
        tiled_obj_sprite = Tile(pos, obj_image, [self.all_sprites])

        