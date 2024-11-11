"""Inimigos do jogo"""

import pygame
import math
import random
import config

class Enemie(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        # Invocação
        self.game = game
        self._layer = config.player_layer
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        # Configurações básicas de posição e escala
        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = config.tilesize
        self.height = config.tilesize

        # Forma a aparência do inimigo
        self.image = pygame.Surface((self.x, self.y), 0, 0, "Red")

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

    def movement(self):
        # Implementar IA que vai programar movimento dos inimigos
        if False: # Esquerda
            self.x -= config.enemie_speed
        if False: # Direita
            self.x += config.enemie_speed
        if False: # Cima
            self.y -= config.enemie_speed
        if False: # Baixo
            self.y += config.enemie_speed
        pass

    def ataque(self):
        pass

    def collision(self):
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



