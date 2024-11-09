import pygame
import math
import random
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        self.game= game
        self._layer = config.player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = config.tilesize
        self.height = config.tilesize
        
        self.x_change = 0
        self.y_change = 0
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(config.red)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x_change -= config.player_speed
            self.facing = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x_change += config.player_speed
            self.facing = "right"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y_change -= config.player_speed
            self.facing = "up"
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y_change += config.player_speed
            self.facing = "down"
        