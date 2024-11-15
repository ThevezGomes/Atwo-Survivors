import pygame as pg
import sys
from pytmx.util_pygame import load_pygame
import os

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

    def scale(self, width, height):
        self.image = pg.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

"""class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks

"""