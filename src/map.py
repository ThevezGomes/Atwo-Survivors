import pygame as pg
import sys
from pytmx.util_pygame import load_pygame
import os

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf=None, groups=None, rect=None):
        super().__init__(*groups)
        self.image = surf or pg.Surface((1, 1), pg.SRCALPHA)  # Invisível por padrão
        if rect:
            self.rect = rect  # Usa o retângulo fornecido
        else:
            self.rect = self.image.get_rect(topleft=pos)  # Calcula o retângulo baseado na imagem e posição

    def scale(self, width, height):
        self.image = pg.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)



"""
class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

    def scale(self, width, height):
        self.image = pg.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks

"""