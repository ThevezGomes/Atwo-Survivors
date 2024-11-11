"""Inimigos do jogo"""

import pygame
import math
import random
import config
from main_character import Player
import enemy_ai as ai

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
        self.width = 32 *config.tilesize
        self.height = 32 * config.tilesize

        # Mudança de posição
        self.x_change = 0
        self.y_change = 0

        # Forma a aparência do inimigo (Animação há de ser implementada ainda)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(config.red)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



    def update(self):

        self.x_change, self.y_change = ai.enemy_pursue(self)

        # Implementa IA que vai programar movimento dos inimigos

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

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

    



