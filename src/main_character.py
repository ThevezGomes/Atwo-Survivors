import pygame
import math
import random
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        # Define propriedades do jogador, como camada e grupo de sprites
        self.game= game
        self._layer = config.player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

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
        self.image = self.game.main_character_spritesheet.get_sprite(12, 7, 22, 32)
        self.image = pygame.transform.scale(self.image, config.size)

        # Define posicoes do retangulo do jogador
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

    # Atualiza todas as propriedades do jogador, como movimento, animacao, mudanca de posicao e colisao
    def update(self):
        self.movement()
        self.animate()
        
        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")
        
        self.x_change = 0
        self.y_change = 0

    # Cria o movimento do jogador
    def movement(self):
        # Para cada tecla que ele pressiona, define para onde o personagem vai olhar e a variacao da posicao
        # PRECISA DESCOMENTAR AS PROXIMAS LINHAS DE CODIGO, FAZEM A CAMERA SEGUIR O JOGADOR
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            #for sprite in self.game.all_sprites:
                #sprite.rect.x += config.player_speed
            self.x_change -= config.player_speed
            self.facing = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            #for sprite in self.game.all_sprites:
                #sprite.rect.x -= config.player_speed
            self.x_change += config.player_speed
            self.facing = "right"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            #for sprite in self.game.all_sprites:
                #sprite.rect.y += config.player_speed
            self.y_change -= config.player_speed
            self.facing = "up"
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            #for sprite in self.game.all_sprites:
                #sprite.rect.y -= config.player_speed
            self.y_change += config.player_speed
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

            # Movimento do jogador com base no eixo analógico (ajuste o limiar de sensibilidade conforme necessário)
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
                        sprite.rect.x += config.player_speed
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    # Ajusta a camera para nao ser modificada na colisao
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= config.player_speed
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
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
        # Colecao de todas as imagens de animacao do personagem principal
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
                 if self.animation_loop >= 7:
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
                 if self.animation_loop >= 7:
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
                 if self.animation_loop >= 7:
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
                 if self.animation_loop >= 7:
                     self.animation_loop = 1
