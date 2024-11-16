import pygame
import math
import random
import config
import repositorio_sprites as rs

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        # Define propriedades do jogador, como camada e grupo de sprites
        self.game= game
        self._layer = config.layers["player_layer"]
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
        self.image = self.game.sprites.warrior_animations["walk_animations"]["walk_down_animations"][0]
        # Define posicoes do retangulo do jogador
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

    # Atualiza todas as propriedades do jogador, como movimento, animacao, mudanca de posicao e colisao
    def update(self):
        self.movement()
        self.animate()
        self.colete_direction()
        
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
            for sprite in self.game.all_sprites:
                sprite.rect.x += config.player_speed
            self.x_change -= config.player_speed
            self.facing = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= config.player_speed
            self.x_change += config.player_speed
            self.facing = "right"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += config.player_speed
            self.y_change -= config.player_speed
            self.facing = "up"
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= config.player_speed
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
                        sprite.rect.y -= config.player_speed
        
                    
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
                     
    def colete_direction(self):
        self.mouse_direction = "down"
        mouse_position = pygame.mouse.get_pos()
        h = self.game.screen.get_height()
        w = self.game.screen.get_width()
        reta_1 = (h*mouse_position[0])/w
        reta_2 = (h*(-mouse_position[0] + w))/w
        
        if mouse_position[1] >= reta_1 and mouse_position[1] >= reta_2:
            self.mouse_direction = "down"
        if mouse_position[1] <= reta_1 and mouse_position[1] <= reta_2:
            self.mouse_direction = "up"
        if mouse_position[1] <= reta_1 and mouse_position[1] >= reta_2:
            self.mouse_direction = "right"
        if mouse_position[1] >= reta_1 and mouse_position[1] <= reta_2:
            self.mouse_direction = "left"

class Attack(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y, item):
        
        self.game = game
        self._layer = config.layers["player_layer"]
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.item = item
        
        keys_animations = list(self.game.sprites.attack_animations[self.item].keys())
        self.image = self.game.sprites.attack_animations[self.item][keys_animations[0]][0]
        
        # Define tamanho e posicao do ataque
        self.x = x * config.tilesize
        self.y = y * config.tilesize
        self.width = config.tilesize
        self.height = config.tilesize
        
        self.animation_loop = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.animate()
        
    def animate(self):
        direction = self.game.player.mouse_direction
        
        [self.wave_down_animations, self.wave_up_animations, self.wave_right_animations, self.wave_left_animations] = self.game.sprites.attack_animations[self.item].values()
        
        if direction == "down":
            # Cria o loop de animacao
            self.image = self.wave_down_animations[math.floor(self.animation_loop)]
            # Ajusta a velocidade com que o loop ocorre nessa direcao
            self.animation_loop += 0.5
            if self.animation_loop >= (len(self.wave_down_animations)- 1):
                self.kill()
        
        if direction == "up":
            # Cria o loop de animacao
            self.image = self.wave_up_animations[math.floor(self.animation_loop)]
            # Ajusta a velocidade com que o loop ocorre nessa direcao
            self.animation_loop += 0.5
            if self.animation_loop >= (len(self.wave_up_animations)- 1):
                self.kill()
                
        if direction == "right":
            # Cria o loop de animacao
            self.image = self.wave_right_animations[math.floor(self.animation_loop)]
            # Ajusta a velocidade com que o loop ocorre nessa direcao
            self.animation_loop += 0.5
            if self.animation_loop >= (len(self.wave_right_animations)- 1):
                self.kill()
                
        if direction == "left":
            # Cria o loop de animacao
            self.image = self.wave_left_animations[math.floor(self.animation_loop)]
            # Ajusta a velocidade com que o loop ocorre nessa direcao
            self.animation_loop += 0.5
            if self.animation_loop >= (len(self.wave_left_animations)- 1):
                self.kill()
                