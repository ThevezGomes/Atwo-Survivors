"""Inimigos do jogo"""
import pygame
import math
import random
import config
from main_character import Player
from enemy_ai import *
import sprites
import repositorio_sprites as rs

class Enemy(pygame.sprite.Sprite):

    """
        Classe que define inimigos a serem inseridos no jogo

        Aqui são programadas a maioria das mecânicas envolvidas nos inimigos (NPC's) do jogo.

        Attributes:

        game: (Objeto da classe Game); Jogo em que os inimigos serão inseridos
        _layer: (int); Camada em que será inserido o inimigo na exibição
        groups = (list, list); Listas que armazenam os inimigos e entidades
        kind = (str); Tipo do inimigo
        class_ = (str); Classificação geral
        fov = (int); Campo de visão do inimigo
        speed = (int); Velocidade de deslocamento do inimigo
        health = (int); Vida máxima do inimigo
        attacking = (bool); Se o personagem está atacando
        attack_time = (int); Tempo de ataque
        damage = (bool); Se houve dano
        damage_time = (int); Tempo de dano
        damage_index = (int); Índice de dano
        damage_reason = (int); Índice de dificuldade do jogo
        ai = (Objeto da classe Enemy_IA); Sistema de movimentação do personagem

    """
    
    def __init__(self, game, kind, x, y):

        """
        Inicializa um novo inimigo.

        Configura os atributos principais, grupos de sprites e a inteligência artificial.

        Parâmetros:
            game (Game): Objeto principal do jogo.
            kind (str): Tipo de inimigo (usado para acessar configurações específicas).
            x (int): Posição inicial do inimigo no eixo X.
            y (int): Posição inicial do inimigo no eixo Y.
        """
        # Invocação
        self.game = game
        self._layer = config.layers["enemy_layer"] 
        self.groups = self.game.all_sprites, self.game.enemies
        self.kind = kind
        self.class_ = "Enemy"
        self.fov = config.enemy_fov[self.kind]
        self.speed = config.enemy_speed[self.kind]
        self.health = config.max_health["enemies"][kind]
        self.attacking = False
        self.attack_time = 0
        
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

        """
        Atualiza o estado do inimigo em cada frame.

        Realiza as ações do inimigo, como perseguir o jogador (utilizando os recursos de IA), atacar, 
        verificar colisões e animações, além de monitorar sua saúde e remoção do jogo.
        """

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
            
            if self.ai.track_player:
                self.atacar(self.game)
            
            self.check_health()
            self.despawn()

            self.speed = self.speed * self.game.difficulty_ratio
            self.health = self.health * self.game.difficulty_ratio

    def atacar(self, game):

        """
        Realiza um ataque contra o jogador.

        Verifica se o inimigo pode atacar com base no tempo de recarga. Caso seja possível, 
        cria uma instância de `EnemyAttack`.

        Parâmetros:
            game (Game): Objeto principal do jogo.
        """

        if config.enemies_attack_list[self.kind] != []:
            if not self.attacking:
                self.attacking = True
                attack = random.choice(config.enemies_attack_list[self.kind])
                EnemyAttack(game, attack, self)
                self.attack_time = pygame.time.get_ticks()
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.attack_time > config.enemy_attack_delay[self.kind]:
                    self.attacking = False

    def collide_blocks(self, direction):

        """
        Gerencia colisões do inimigo com blocos do cenário.

        Ajusta a posição do inimigo ao colidir com objetos sólidos.

        Parâmetros:
        direction (str): Direção da colisão ("x" ou "y").
        """
        
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

        """
        Controla a animação do inimigo com base na direção e movimento.

        Alterna entre os frames de animação dependendo da direção em que o inimigo está olhando
        e se está em movimento ou parado.
        """

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

        """
        Verifica se o inimigo ainda tem pontos de vida.

        Caso o inimigo tenha sido derrotado, remove-o do jogo e adiciona experiência ao jogador.
        """

        if self.health <= 0:
            try:
                self.game.enemies_list.remove(self)
            except ValueError:
                pass
            self.kill()
            self.game.player.xp += config.enemy_xp[self.kind]
            
            
    def despawn(self):
            
        """
        Remove o inimigo do jogo se ele estiver fora do campo de visão do jogador por muito tempo.

        Esta funcionalidade ajuda a liberar memória e evitar inimigos desnecessários.
        """

        if not self.ai.track_player:
            current_time = pygame.time.get_ticks()
            if current_time - self.ai.time_untracked > config.despawn_delay:
                try:
                    self.game.enemies_list.remove(self)
                except ValueError:
                    pass
                self.kill()
                
        
    def damage_animation(self):

        """
        Executa a animação de dano ao inimigo.

        Reduz a saúde do inimigo e alterna entre os frames de animação de dano, 
        dependendo da direção em que ele está olhando.
        """
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

        """
        Inicializa um inimigo do tipo Boss.

        Configura atributos específicos do Boss, como nome e status de "último chefe".

        Parâmetros:
            game (Game): Objeto principal do jogo.
            kind (str): Tipo do Boss.
            x (int): Posição inicial no eixo X (em tiles).
            y (int): Posição inicial no eixo Y (em tiles).
            name (str): Nome do Boss.
            last_boss (bool): Indica se este é o último Boss do jogo (padrão: False).
        """
        super().__init__(game, kind, x, y)
        self.name = name
        self.last_boss = last_boss
        self.ai = Boss_IA(self)
        
    def check_health(self):
            
        """
        Verifica se o Boss ainda está vivo.

        Caso seja derrotado, realiza ações específicas, como tocar um som de vitória 
        ou permitir o spawn de outros inimigos.
        """

        if self.health <= 0:
            self.kill()
            if self.last_boss:
                self.game.play_sound("victory_sound")
                self.game.game_over("Parabéns, você venceu!")
            else:
                self.game.player.xp += config.enemy_xp[self.kind]
                self.game.spawned_boss = False
                self.game.allow_spawn_enemies = True
               
    def despawn(self):
        """
        Evita que o Boss seja removido automaticamente do jogo.

        Este método sobrescreve o comportamento padrão da classe `Enemy`.
        """
        pass
                
class EnemyAttack(pygame.sprite.Sprite):

    
    def __init__(self, game, kind, enemy):

        """
        Inicializa um ataque do inimigo.

        Configura os atributos e grupos de sprites do ataque, incluindo a direção
        e a velocidade com base na posição do jogador.

        Parâmetros:
        game (Game): Objeto principal do jogo.
        kind (str): Tipo do ataque (usado para acessar animações e configurações específicas).
        enemy (Enemy): Referência ao inimigo que realizou o ataque.
        """
        
        self.game = game
        self.kind = kind
        self.class_ = "EnemyAttack"
        self.enemy = enemy
        self._layer = config.layers["enemy_layer"]
        self.groups = self.game.all_sprites, self.game.enemy_attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.animation_speed = config.enemy_attack_animation_speed[self.kind]
        
        keys_animations = list(self.game.sprites.enemy_attack_animations[self.kind].keys())
        self.image = self.game.sprites.enemy_attack_animations[self.kind][keys_animations[0]][0]
        
        self.speed = config.enemy_attack_speed[self.kind]
        direction = pygame.math.Vector2(self.game.player.rect.x - self.enemy.rect.x, self.game.player.rect.y - self.enemy.rect.y)
        self.velocity = direction.normalize() * self.speed
        
        x_attack = self.enemy.rect.x + direction.normalize()[0] * self.enemy.rect.width
        y_attack = self.enemy.rect.y + direction.normalize()[1] * self.enemy.rect.height
        
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

        """
        Atualiza o estado do ataque em cada frame.

        Controla o movimento, animação, e detecção de colisões do ataque.
        """

        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.collide_blocks()
        #DAVI
        #self.attack_with_joystick()

        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        """
        Define o movimento do ataque com base na direção do jogador.

        Calcula os deslocamentos nos eixos X e Y para cada frame.
        """
        self.x_change = self.velocity[0]
        self.y_change = self.velocity[1]
        
    def animate(self):
        """
        Controla a animação do ataque.

        Alterna os frames de animação e rotaciona o sprite com base na direção do ataque.
        """                
        [self.attack_animations] = self.game.sprites.enemy_attack_animations[self.kind].values()
        
        # Cria o loop de animacao
        self.image = self.attack_animations[math.floor(self.animation_loop)]
        angle = self.velocity.angle_to(pygame.math.Vector2(0, -1))  # Alinha com o eixo Y (apontando para cima)
        self.image = pygame.transform.rotate(self.image, angle).convert_alpha()  # Rotaciona o sprite
        # self.rect = self.image.get_rect(center=self.rect.center)  # Atualiza o retângulo
        # Ajusta a velocidade com que o loop ocorre nessa direcao
        self.animation_loop += self.animation_speed
        if self.animation_loop >= (len(self.attack_animations)- 1):
            self.kill()              
                
    def collide_blocks(self):
        """
        Detecta colisões do ataque com blocos do cenário.

        Remove o ataque do jogo caso colida com um bloco sólido.
        """

        hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
        if hits:
            self.kill()