import pygame
import math
import random
import config
import repositorio_sprites as rs
from items_abilities import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        # Define propriedades do jogador, como camada e grupo de sprites
        self.game= game
        self._layer = config.layers["player_layer"]
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.speed = config.player_speed
        self.health = config.max_health["player"]
        self.max_health = config.max_health["player"]
        self.level = 1
        self.xp = 0
        self.enemies = []
        self.damage = False
        self.damage_time = 0
        self.damage_index = 0
        self.death = False
        self.death_time = 0
        self.death_index = 0
        self.attacking = False
        self.attack_time = 0

        # Define tamanho e posicao do jogador
        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = config.tilesize
        self.height = config.tilesize

        # Define a variacao da posicao do jogador nos eixos, inicial igual a 0
        self.x_change = 0
        self.y_change = 0

        # Define para onde ele olha e o estado da animacao, inicial igual para baixo e 1, respectivamente
        self.facing = "down"
        self.animation_loop = 1

        # Define a imagem inicial do jogador e ajusta o tamanho dele com a tela
        self.image = self.game.sprites.warrior_animations["walk_animations"]["walk_down_animations"][0]
        # Define posicoes do retangulo do jogador
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

    # Atualiza todas as propriedades do jogador, como movimento, animacao, mudanca de posicao e colisao
    def update(self):
        if self.death:
            self.death_animation()
        elif self.damage:
            self.damage_animation()
        else:
            self.speed = config.player_speed * (1 + self.game.buffs["speed"])
            self.movement()
            self.animate()
            self.collide_enemy()
            
            self.rect.x += self.x_change
            self.collide_blocks("x")
            self.rect.y += self.y_change
            self.collide_blocks("y")
            
            self.x_change = 0
            self.y_change = 0
            
            self.check_xp_level()
            
            
            self.max_health = config.max_health["player"] * (1 + self.game.buffs["life"])

    # Cria o movimento do jogador
    def movement(self):
        # Para cada tecla que ele pressiona, define para onde o personagem vai olhar e a variacao da posicao
        # PRECISA DESCOMENTAR AS PROXIMAS LINHAS DE CODIGO, FAZEM A CAMERA SEGUIR O JOGADOR
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += self.speed
            self.x_change -= self.speed
            self.facing = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= self.speed
            self.x_change += self.speed
            self.facing = "right"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += self.speed
            self.y_change -= self.speed
            self.facing = "up"
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= self.speed
            self.y_change += self.speed
            self.facing = "down"
        
        #Caso for iplementar o controle, uma base para a movimentação
        """
        # Inicializa o joystick (caso ainda não tenha sido iniciado)
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

            # Obtém os valores dos eixos do joystick
            x_axis = joystick.get_axis(0)  # Eixo horizontal (esquerda/direita)
            y_axis = joystick.get_axis(1)  # Eixo vertical (cima/baixo)

            # Movimento do jogador com base no eixo analógico (ajuste o limiar de sensibilidade conforme necessário) DAVI
            if abs(x_axis) > 0.1:
                for sprite in self.game.all_sprites:
                    sprite.rect.x += x_axis * config_mod.player_speed
                self.x_change += x_axis * config_mod.player_speed
                self.facing = "left" if x_axis < 0 else "right"

            if abs(y_axis) > 0.1:
                for sprite in self.game.all_sprites:
                    sprite.rect.y += y_axis * config_mod.player_speed
                self.y_change += y_axis * config_mod.player_speed
                self.facing = "up" if y_axis < 0 else "down"
           """     

    # Ajusta a colisao
    def collide_blocks(self, direction):
        # Para cada direcao, se o personagem colide com o cenario, entao ajusta a posicao do jogador para fora do objeto colidido
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += self.speed
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= self.speed
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += self.speed
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= self.speed
        
                    
    def animate(self):
        # Colecao de todas as imagens de animacao do personagem principal
         [walk_down_animations, walk_up_animations, walk_right_animations, walk_left_animations] = self.game.sprites.warrior_animations["walk_animations"].values()

        # Para cada direcao que o personagem olha, ajusta a animacao correspondente e o tamanho da imagem
         if self.facing == "down":
             if self.y_change == 0:
                 self.image = walk_down_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = walk_down_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(walk_down_animations) - 1):
                     self.animation_loop = 1
            
         if self.facing == "up":
             if self.y_change == 0:
                 self.image = walk_up_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = walk_up_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(walk_up_animations) - 1):
                     self.animation_loop = 1
                     
         if self.facing == "right":
             if self.x_change == 0:
                 self.image = walk_right_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = walk_right_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(walk_right_animations) - 1):
                     self.animation_loop = 1
                     
         if self.facing == "left":
             if self.x_change == 0:
                 self.image = walk_left_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = walk_left_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += 0.2
                 if self.animation_loop >= (len(walk_left_animations) - 1):
                     self.animation_loop = 1
            
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > config.damage_delay:
                self.damage = True   
                self.damage_index = 0
                self.damage_time = pygame.time.get_ticks()
                self.enemies = list(hits)
                
    def damage_animation(self):
        for enemy in self.enemies:
            self.health -= config.damage["enemies"][enemy.kind] * (1 - self.game.buffs["defense"])
        [self.hurt_down_animations, self.hurt_up_animations, self.hurt_right_animations, self.hurt_left_animations] = self.game.sprites.warrior_animations["hurt_animations"].values()
        if self.facing == "down":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                self.damage_index = (self.damage_index + 1)
                if self.damage_index < len(self.hurt_down_animations):
                    self.image = self.hurt_down_animations[self.damage_index]
                else:
                    self.damage = False
                

        if self.facing == "up":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                self.damage_index = (self.damage_index + 1)
                if self.damage_index < len(self.hurt_up_animations):
                    self.image = self.hurt_up_animations[self.damage_index]
                else:
                    self.damage = False
               
        if self.facing == "right":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                self.damage_index = (self.damage_index + 1)
                if self.damage_index < len(self.hurt_right_animations):
                    self.image = self.hurt_right_animations[self.damage_index]
                else:
                    self.damage = False
                
        if self.facing == "left":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > 50:  # Troca de frame a cada 100ms
                self.damage_time = current_time
                self.damage_index = (self.damage_index + 1)
                if self.damage_index < len(self.hurt_left_animations):
                    self.image = self.hurt_left_animations[self.damage_index]
                else:
                    self.damage = False

    def death_animation(self):
        [self.death_down_animations, self.death_up_animations, self.death_right_animations, self.death_left_animations] = self.game.sprites.warrior_animations["death_animations"].values()
        if self.facing == "down":
            current_time = pygame.time.get_ticks()
            if current_time - self.death_time > 100: # Troca de frame a cada 100ms
                self.death_time = current_time
                self.death_index = (self.death_index + 1)
                if self.death_index < len(self.death_down_animations):
                    self.image = self.death_down_animations[self.death_index]  
                else:
                    self.game.draw()
                    self.game.game_over()

        if self.facing == "up":
            current_time = pygame.time.get_ticks()
            if current_time - self.death_time > 100:  # Troca de frame a cada 100ms
                self.death_time = current_time
                self.death_index = (self.death_index + 1)
                if self.death_index < len(self.death_up_animations):
                    self.image = self.death_up_animations[self.death_index]
                else:
                    self.game.draw()
                    self.game.game_over()
               
        if self.facing == "right":
            current_time = pygame.time.get_ticks()
            if current_time - self.death_time > 100:  # Troca de frame a cada 100ms
                self.death_time = current_time
                self.death_index = (self.death_index + 1)
                if self.death_index < len(self.death_right_animations):
                    self.image = self.death_right_animations[self.death_index]
                else:
                    self.game.draw()
                    self.game.game_over()
                
        if self.facing == "left":
            current_time = pygame.time.get_ticks()
            if current_time - self.death_time > 100:  # Troca de frame a cada 100ms
                self.death_time = current_time
                self.death_index = (self.death_index + 1)
                if self.death_index < len(self.death_left_animations):
                    self.image = self.death_left_animations[self.death_index]
                else:
                    self.game.draw()
                    self.game.game_over()
                    
    def atacar(self, game, x, y, item, position, level=1):
        if not self.attacking:
            self.attacking = True
            Attack(game, x, y, item, position, level)
            self.attack_time = pygame.time.get_ticks()
        else:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time > config.itens_delay[item] * (1 - self.game.buffs["firing_speed"]):
                self.attacking = False

        #Davi
        """
        if pygame.joystick.get_count()>0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

            # Botão de ataque (por exemplo, o botão 0 que é geralmente o "A" no controle)
            attack_button = joystick.get_button(0)

            if attack_button and not self.attacking:
                self.attacking = True
                # Chama a função de ataque
                self.atacar(self.game, self.rect.centerx, self.rect.centery, "sword", self.facing)
                self.attack_time = pygame.time.get_ticks()
            """

    def check_xp_level(self):
        if self.xp >= self.levels(self.level):
            self.xp = self.xp - self.levels(self.level)
            self.level += 1
            self.game.level_up = True
            
    def levels(self, level):
        xp_level_1 = 100
        
        return int(xp_level_1*(1.5)**level)
        return 100
        
                
class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y, item, position, level):
        
        self.game = game
        self._layer = config.layers["player_layer"]
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.item = item
        self.level = level
        self.animation_speed = config.item_animation_speed[self.item]
        
        keys_animations = list(self.game.sprites.attack_animations[self.item].keys())
        self.image = self.game.sprites.attack_animations[self.item][keys_animations[0]][0]
        
        self.speed = config.itens_speed[self.item]
        direction = pygame.math.Vector2(position[0] - x, position[1] - y)
        self.velocity = direction.normalize() * self.speed
        
        x_attack = x + direction.normalize()[0] * self.game.player.rect.width
        y_attack = y + direction.normalize()[1] * self.game.player.rect.height
        
        # Define tamanho e posicao do ataque
        self.x = x_attack
        self.y = y_attack
        self.width = config.tilesize
        self.height = config.tilesize
        self.x_change = 0
        self.y_change = 0
        
        self.animation_loop = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.rect.width/2
        self.rect.y = self.y - self.rect.height/2
        
        
    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.collide_blocks()
        #DAVI
        #self.attack_with_joystick()

        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        self.x_change = self.velocity[0]
        self.y_change = self.velocity[1]
        
    def animate(self):        
        [self.attack_animations] = self.game.sprites.attack_animations[self.item].values()
        
        # Cria o loop de animacao
        self.image = self.attack_animations[math.floor(self.animation_loop)]
        angle = self.velocity.angle_to(pygame.math.Vector2(0, -1))  # Alinha com o eixo Y (apontando para cima)
        self.image = pygame.transform.rotate(self.image, angle).convert_alpha()  # Rotaciona o sprite
        # self.rect = self.image.get_rect(center=self.rect.center)  # Atualiza o retângulo
        # Ajusta a velocidade com que o loop ocorre nessa direcao
        self.animation_loop += self.animation_speed
        if self.animation_loop >= (len(self.attack_animations)- 1):
            self.kill()
            
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            for sprite in hits:
                if not sprite.damage:
                    sprite.damage = True
                    sprite.damage_index = 0
                    sprite.damage_reason = self
                    sprite.damage_time = pygame.time.get_ticks() 
                
                
                
    def collide_blocks(self):
        hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
        if hits:
            self.kill()