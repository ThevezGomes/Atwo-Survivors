"""Inimigos do jogo"""

import pygame
import math
import random
import config

class Enemie(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = config.player_layer
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = config.tilesize
        self.height = config.tilesize

        self.image = pygame.Surface((self.x, self.y), 0, 0, "Red")