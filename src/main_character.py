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
        
        self.facing = "down"
        self.animation_loop = 1
        
        self.image = self.game.main_character_spritesheet.get_sprite(12, 7, 22, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        self.animate()
        
        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")
        
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
            
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    
    def animate(self):
         walk_down_animations = [self.game.main_character_spritesheet_walk_down.get_sprite(12, 7, 22, 32),
                                 self.game.main_character_spritesheet_walk_down.get_sprite(61, 7, 22, 32),
                                 self.game.main_character_spritesheet_walk_down.get_sprite(109, 6, 22, 32),
                                 self.game.main_character_spritesheet_walk_down.get_sprite(157, 6, 22, 32),
                                 self.game.main_character_spritesheet_walk_down.get_sprite(204, 7, 22, 32),
                                 self.game.main_character_spritesheet_walk_down.get_sprite(251, 7, 22, 32),
                                 self.game.main_character_spritesheet_walk_down.get_sprite(299, 6, 22, 32),
                                 self.game.main_character_spritesheet_walk_down.get_sprite(347, 6, 22, 32)]
         
         walk_up_animations = [self.game.main_character_spritesheet_walk_up.get_sprite(13, 7, 22, 32),
                               self.game.main_character_spritesheet_walk_up.get_sprite(60, 7, 22, 32),
                               self.game.main_character_spritesheet_walk_up.get_sprite(108, 6, 22, 32),
                               self.game.main_character_spritesheet_walk_up.get_sprite(156, 6, 22, 32),
                               self.game.main_character_spritesheet_walk_up.get_sprite(205, 7, 22, 32),
                               self.game.main_character_spritesheet_walk_up.get_sprite(255, 7, 22, 32),
                               self.game.main_character_spritesheet_walk_up.get_sprite(303, 6, 22, 32),
                               self.game.main_character_spritesheet_walk_up.get_sprite(351, 6, 22, 32)]
         
         walk_right_animations = [self.game.main_character_spritesheet_walk_right.get_sprite(12, 9, 22, 32),
                                  self.game.main_character_spritesheet_walk_right.get_sprite(60, 9, 22, 32),
                                  self.game.main_character_spritesheet_walk_right.get_sprite(109, 9, 22, 32),
                                  self.game.main_character_spritesheet_walk_right.get_sprite(157, 9, 22, 32),
                                  self.game.main_character_spritesheet_walk_right.get_sprite(204, 9, 22, 32),
                                  self.game.main_character_spritesheet_walk_right.get_sprite(251, 9, 22, 32),
                                  self.game.main_character_spritesheet_walk_right.get_sprite(299, 9, 22, 32),
                                  self.game.main_character_spritesheet_walk_right.get_sprite(347, 9, 22, 32)]
         
         walk_left_animations = [self.game.main_character_spritesheet_walk_left.get_sprite(15, 9, 22, 32),
                                 self.game.main_character_spritesheet_walk_left.get_sprite(64, 9, 22, 32),
                                 self.game.main_character_spritesheet_walk_left.get_sprite(113, 9, 22, 32),
                                 self.game.main_character_spritesheet_walk_left.get_sprite(161, 9, 22, 32),
                                 self.game.main_character_spritesheet_walk_left.get_sprite(207, 9, 22, 32),
                                 self.game.main_character_spritesheet_walk_left.get_sprite(254, 9, 22, 32),
                                 self.game.main_character_spritesheet_walk_left.get_sprite(302, 9, 22, 32),
                                 self.game.main_character_spritesheet_walk_left.get_sprite(350, 9, 22, 32)]
         
         if self.facing == "down":
             if self.y_change == 0:
                 self.image = walk_down_animations[0]
             else:
                 self.image = walk_down_animations[math.floor(self.animation_loop)]
                 self.animation_loop += 0.2
                 if self.animation_loop >= 7:
                     self.animation_loop = 1
            
         if self.facing == "up":
             if self.y_change == 0:
                 self.image = walk_up_animations[0]
             else:
                 self.image = walk_up_animations[math.floor(self.animation_loop)]
                 self.animation_loop += 0.2
                 if self.animation_loop >= 7:
                     self.animation_loop = 1
                     
         if self.facing == "right":
             if self.x_change == 0:
                 self.image = walk_right_animations[0]
             else:
                 self.image = walk_right_animations[math.floor(self.animation_loop)]
                 self.animation_loop += 0.2
                 if self.animation_loop >= 7:
                     self.animation_loop = 1
                     
         if self.facing == "left":
             if self.x_change == 0:
                 self.image = walk_left_animations[0]
             else:
                 self.image = walk_left_animations[math.floor(self.animation_loop)]
                 self.animation_loop += 0.2
                 if self.animation_loop >= 7:
                     self.animation_loop = 1