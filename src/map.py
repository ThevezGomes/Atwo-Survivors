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

        Argumentoss:
            width (int): Nova largura do tile.
            height (int): Nova altura do tile.
        """
        self.image = pg.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    