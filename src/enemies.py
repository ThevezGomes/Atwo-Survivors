"""Inimigos do jogo"""

import pygame
import math
import random
import config
from main_character import Player
from enemy_ai import Enemy_AI

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, kind, x, y):

        # Invocação
        self.game = game
        self._layer = config.enemy_layer
        self.groups = self.game.all_sprites, self.game.enemies
        self.kind = kind
        self.speed = config.enemy_speed[self.kind]

        # Invocar IA

        self.ai = Enemy_AI(self)
  
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Configurações básicas de posição e escala
        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = 32 *config.tilesize
        self.height = 32 * config.tilesize
        self.facing = self.ai.facing
        self.animation_loop = 1


        # Mudança de posição
        self.x_change = 0
        self.y_change = 0

        # Forma a aparência do inimigo (Animação há de ser implementada ainda)
        self.image = self.game.enemy_skeleton_spritesheet.get_sprite(12, 7, 22, 32)
        self.image = pygame.transform.scale(self.image, config.size)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):

        self.x_change, self.y_change = self.ai.enemy_pursue()
        self.facing = self.ai.facing
        self.animate()

        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")

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

    
    def animate(self):
        walk_down_animations = [ self.game.enemy_skeleton_spritesheet_walk_down.get_sprite(  8, 12, 25, 29),
                                 self.game.enemy_skeleton_spritesheet_walk_down.get_sprite( 55, 11, 25, 29),
                                 self.game.enemy_skeleton_spritesheet_walk_down.get_sprite(104, 10, 25, 29),
                                 self.game.enemy_skeleton_spritesheet_walk_down.get_sprite(152, 11, 25, 29),
                                 self.game.enemy_skeleton_spritesheet_walk_down.get_sprite(198, 11, 25, 29),
                                 self.game.enemy_skeleton_spritesheet_walk_down.get_sprite(246, 11, 25, 29)]
         
        walk_up_animations = [ self.game.enemy_skeleton_spritesheet_walk_up.get_sprite( 15, 11, 25, 30),
                               self.game.enemy_skeleton_spritesheet_walk_up.get_sprite( 63, 11, 24, 30),
                               self.game.enemy_skeleton_spritesheet_walk_up.get_sprite(111, 10, 23, 30),
                               self.game.enemy_skeleton_spritesheet_walk_up.get_sprite(159, 11, 25, 30),
                               self.game.enemy_skeleton_spritesheet_walk_up.get_sprite(208, 11, 24, 30),
                               self.game.enemy_skeleton_spritesheet_walk_up.get_sprite(256, 11, 24, 30)]
         
        walk_right_animations = [ self.game.enemy_skeleton_spritesheet_walk_right.get_sprite( 15, 11, 22, 31),
                                  self.game.enemy_skeleton_spritesheet_walk_right.get_sprite( 62, 11, 22, 31),
                                  self.game.enemy_skeleton_spritesheet_walk_right.get_sprite(109, 10, 22, 31),
                                  self.game.enemy_skeleton_spritesheet_walk_right.get_sprite(159, 11, 22, 31),
                                  self.game.enemy_skeleton_spritesheet_walk_right.get_sprite(207, 11, 22, 31),
                                  self.game.enemy_skeleton_spritesheet_walk_right.get_sprite(256, 10, 22, 31)]
         
        walk_left_animations = [ self.game.enemy_skeleton_spritesheet_walk_left.get_sprite(  8, 11, 29, 30),
                                 self.game.enemy_skeleton_spritesheet_walk_left.get_sprite( 54, 11, 29, 30),
                                 self.game.enemy_skeleton_spritesheet_walk_left.get_sprite(102, 10, 29, 30),
                                 self.game.enemy_skeleton_spritesheet_walk_left.get_sprite(152, 11, 29, 30),
                                 self.game.enemy_skeleton_spritesheet_walk_left.get_sprite(202, 11, 29, 30),
                                 self.game.enemy_skeleton_spritesheet_walk_left.get_sprite(250, 10, 29, 30)]

        # Para cada direcao que o personagem olha, ajusta a animacao correspondente e o tamanho da imagem
        if self.facing == "down":
             if self.y_change == 0:
                 self.image = walk_down_animations[0]
                 self.image = pygame.transform.scale(self.image, config.size)
             else:
                 # Cria o loop de animacao
                 self.image = walk_down_animations[math.floor(self.animation_loop)]
                 self.image = pygame.transform.scale(self.image, config.size)
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= 5:
                     self.animation_loop = 1
            
        if self.facing == "up":
             if self.y_change == 0:
                 self.image = walk_up_animations[0]
                 self.image = pygame.transform.scale(self.image, config.size)
             else:
                 # Cria o loop de animacao
                 self.image = walk_up_animations[math.floor(self.animation_loop)]
                 self.image = pygame.transform.scale(self.image, config.size)
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= 5:
                     self.animation_loop = 1
                     
        if self.facing == "right":
             if self.x_change == 0:
                 self.image = walk_right_animations[0]
                 self.image = pygame.transform.scale(self.image, config.size)
             else:
                 # Cria o loop de animacao
                 self.image = walk_right_animations[math.floor(self.animation_loop)]
                 self.image = pygame.transform.scale(self.image, config.size)
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= 5:
                     self.animation_loop = 1
                     
        if self.facing == "left":
             if self.x_change == 0:
                 self.image = walk_left_animations[0]
                 self.image = pygame.transform.scale(self.image, config.size)
             else:
                 # Cria o loop de animacao
                 self.image = walk_left_animations[math.floor(self.animation_loop)]
                 self.image = pygame.transform.scale(self.image, config.size)
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= 5:
                     self.animation_loop = 1

        


