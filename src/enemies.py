"""Inimigos do jogo"""

import pygame
import math
import random
import config
from main_character import Player
from enemy_ai import AI

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        # Invocação
        self.game = game
        self._layer = config.enemy_layer
        self.groups = self.game.all_sprites, self.game.enemies

        pygame.sprite.Sprite.__init__(self, self.groups)

        # Configurações básicas de posição e escala
        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = config.tilesize
        self.height = config.tilesize

        # Mudança de posição
        self.x_change = 0
        self.y_change = 0

        # Forma a aparência do inimigo (Animação há de ser implementada ainda)
        self.image = pygame.Surface((self.x, self.y), 0, 0, "Red")

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # Atributos básicos de perseguição e IA
        self.fov = config.enemy_fov
        self.target = None
        self.targeted_entity = None

        self.game.entities.add(self)


    def movement(self):

        AI.enemy_pursue(self.game, self)

        # Implementar IA que vai programar movimento dos inimigos
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

        pass

    def update(self):
        self.movement()

    def ataque(self):
        pass

    def collide_blocks(self, direction):
        # Para cada direcao, se o personagem colide com o cenario, entao ajusta a posicao do jogador para fora do objeto colidido
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += config.player_speed
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= config.player_speed
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += config.player_speed
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= config.player_speed

    



