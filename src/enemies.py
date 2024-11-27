"""Inimigos do jogo"""
import pygame
import math
import random
import config
from main_character import Player
from enemy_ai import Enemy_AI
import sprites
import repositorio_sprites as rs

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, kind, x, y):

        # Invocação
        self.game = game
        self._layer = config.layers["enemy_layer"]
        self.groups = self.game.all_sprites, self.game.enemies
        self.kind = kind
        self.speed = config.enemy_speed[self.kind]
        self.health = config.max_health["enemies"][kind]
        
        self.damage = False
        self.damage_time = 0
        self.damage_index = 0
        self.damage_reason = None
        # self.death = False
        # self.death_time = 0
        # self.death_index = 0

        # Invocar IA

        self.ai = Enemy_AI(self)
  
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Configurações básicas de posição e escala
        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = 32 * config.tilesize
        self.height = 32 * config.tilesize
        self.facing = self.ai.facing
        self.animation_loop = 1


        # Mudança de posição
        self.x_change = 0
        self.y_change = 0

        # Forma a aparência do inimigo (Animação há de ser implementada ainda)
        self.keys_animations = list(self.game.sprites.enemy_animations[self.kind]["walk_animations"].keys())
        self.image = self.game.sprites.enemy_animations[self.kind]["walk_animations"][self.keys_animations[0]][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.damage:
            self.damage_animation()
        else:
            self.x_change, self.y_change = self.ai.enemy_pursue()
            self.facing = self.ai.facing
            self.animate()
    
            self.rect.x += self.x_change
            self.collide_blocks("x")
            self.rect.y += self.y_change
            self.collide_blocks("y")
    
            self.x_change = 0
            self.y_change = 0
            
            self.check_health()
            self.despawn()

    def attack(self):
        pass

    def collide_blocks(self, direction):
        # Para cada direcao, se o personagem colide com o cenario, entao ajusta a posicao do jogador para fora do objeto colidido
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    
    def animate(self):

        [self.walk_down_animations, self.walk_up_animations, self.walk_right_animations, self.walk_left_animations]  = self.game.sprites.enemy_animations[self.kind]["walk_animations"].values()

        # Para cada direcao que o personagem olha, ajusta a animacao correspondente e o tamanho da imagem
        if self.facing == "down":
             if self.y_change == 0:
                 self.image = self.walk_down_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_down_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(self.walk_down_animations) - 1):
                     self.animation_loop = 1
            
        if self.facing == "up":
             if self.y_change == 0:
                 self.image = self.walk_up_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_up_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(self.walk_up_animations) - 1):
                     self.animation_loop = 1
                     
        if self.facing == "right":
             if self.x_change == 0:
                 self.image = self.walk_right_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_right_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(self.walk_right_animations) - 1):
                     self.animation_loop = 1
                     
        if self.facing == "left":
             if self.x_change == 0:
                 self.image = self.walk_left_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_left_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(self.walk_left_animations) - 1):
                     self.animation_loop = 1
                     
    def check_health(self):
        if self.health <= 0:
            try:
                self.game.enemies_list.remove(self)
            except ValueError:
                pass
            self.kill()
            self.game.player.xp += config.enemy_xp[self.kind]
            
            
    def despawn(self):
        if not self.ai.track_player:
            current_time = pygame.time.get_ticks()
            if current_time - self.ai.time_untracked > config.despawn_delay:
                try:
                    self.game.enemies_list.remove(self)
                except ValueError:
                    pass
                self.kill()
                
        
    def damage_animation(self):
        self.health -= config.damage["itens"][self.damage_reason.item][self.damage_reason.level] * (1 + self.game.buffs["attack"])
        [self.hurt_down_animations, self.hurt_up_animations, self.hurt_right_animations, self.hurt_left_animations] = self.game.sprites.enemy_animations[self.kind]["hurt_animations"].values()
        if self.facing == "down":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_down_animations):
                    self.image = self.hurt_down_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
                

        if self.facing == "up":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_up_animations):
                    self.image = self.hurt_up_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
               
        if self.facing == "right":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_right_animations):
                    self.image = self.hurt_right_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
                
        if self.facing == "left":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_left_animations):
                    self.image = self.hurt_left_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
                    
class Boss(Enemy):
    def __init__(self, game, kind, x, y, name, last_boss=False):
        super().__init__(game, kind, x, y)
        self.name = name
        self.last_boss = last_boss
        
    def check_health(self):
        if self.health <= 0:
            self.kill()
            if self.last_boss:
                self.game.game_over("Parabéns, você venceu!")
            else:
                self.game.player.xp += config.enemy_xp[self.kind]
                self.game.spawned_boss = False
                self.game.allow_spawn_enemies = True