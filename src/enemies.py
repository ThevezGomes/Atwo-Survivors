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
    def __init__(self, game, kind, x, y):

        # Invocação
        # Define propriedades essenciais para os inimigos
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
        self.animation_speed = config.enemy_animation_speed[self.kind]
        self.damage_animation_speed = config.enemy_damage_animation_speed[self.kind]
        
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

        # Forma a aparência do inimig
        self.keys_animations = list(self.game.sprites.enemy_animations[self.kind]["walk_animations"].keys())
        self.image = self.game.sprites.enemy_animations[self.kind]["walk_animations"][self.keys_animations[0]][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # Atualiza animações de dano caso o inimigo tome dano
        if self.damage:
            self.damage_animation()
        else:
            # Altera o deslocamento do inimigo
            self.x_change, self.y_change = self.ai.enemy_pursue()
            self.facing = self.ai.facing
            # Atualiza as animações do inimigo
            self.animate()
    
            # Atualiza a posição do inimigo e verifica colisão
            self.rect.x += self.x_change
            self.collide_blocks("x")
            self.rect.y += self.y_change
            self.collide_blocks("y")
    
            self.x_change = 0
            self.y_change = 0
            
            # Se tiver perseguindo o player, ataca
            if self.ai.track_player:
                self.atacar(self.game)
            
            # Verifica se o inimigo está vivo e despawna inimigos parados e distantes
            self.check_health()
            self.despawn()

            # Atualiza velocidade do inimigo e vida conforme aumenta a dificuldade
            self.speed = self.speed * self.game.difficulty_ratio
            self.health = self.health * self.game.difficulty_ratio

    def atacar(self, game):
        if config.enemies_attack_list[self.kind] != []:
            # Escolhe um ataque aleatório para atacar
            if not self.attacking:
                self.attacking = True
                attack = random.choice(config.enemies_attack_list[self.kind])
                EnemyAttack(game, attack, self)
                self.attack_time = pygame.time.get_ticks()
            # Aplica delay no ataque
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.attack_time > config.enemy_attack_delay[self.kind]:
                    self.attacking = False

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

        # Para cada direcao que o inimigo olha, ajusta a animacao correspondente e o tamanho da imagem
        if self.facing == "down":
             if self.y_change == 0:
                 self.image = self.walk_down_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_down_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += self.animation_speed
                 if self.animation_loop >= (len(self.walk_down_animations) - 1):
                     self.animation_loop = 1
            
        if self.facing == "up":
             if self.y_change == 0:
                 self.image = self.walk_up_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_up_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += self.animation_speed
                 if self.animation_loop >= (len(self.walk_up_animations) - 1):
                     self.animation_loop = 1
                     
        if self.facing == "right":
             if self.x_change == 0:
                 self.image = self.walk_right_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_right_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += self.animation_speed
                 if self.animation_loop >= (len(self.walk_right_animations) - 1):
                     self.animation_loop = 1
                     
        if self.facing == "left":
             if self.x_change == 0:
                 self.image = self.walk_left_animations[0]
             else:
                 # Cria o loop de animacao
                 self.image = self.walk_left_animations[math.floor(self.animation_loop)]
                 # Ajusta a velocidade com que o loop ocorre nessa direcao
                 self.animation_loop += self.animation_speed
                 if self.animation_loop >= (len(self.walk_left_animations) - 1):
                     self.animation_loop = 1
                     
    def check_health(self):
        # Verifica se o inimigo foi morto, se morrer, remove o inimigo e adiciona o xp ao player
        if self.health <= 0:
            try:
                self.game.enemies_list.remove(self)
            except ValueError:
                pass
            self.kill()
            self.game.player.xp += config.enemy_xp[self.kind]
            
            
    def despawn(self):
        # Se o inimigo parar de seguir o jogador por conta da grande distância, apaga o inimigo
        if not self.ai.track_player:
            current_time = pygame.time.get_ticks()
            # Aplica delay no despawn
            if current_time - self.ai.time_untracked > config.despawn_delay:
                try:
                    self.game.enemies_list.remove(self)
                except ValueError:
                    pass
                self.kill()
                
        
    def damage_animation(self):
        # Remove da vida do inimigo o dano tomado, considerando os buffs
        self.health -= config.damage["itens"][self.damage_reason.item][self.damage_reason.level] * (1 + self.game.buffs["attack"])
        [self.hurt_down_animations, self.hurt_up_animations, self.hurt_right_animations, self.hurt_left_animations] = self.game.sprites.enemy_animations[self.kind]["hurt_animations"].values()
        # Cria a animação do inimigo
        if self.facing == "down":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > self.damage_animation_speed:  # Troca de frame a cada 50ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_down_animations):
                    self.image = self.hurt_down_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
                

        if self.facing == "up":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > self.damage_animation_speed:  # Troca de frame a cada 50ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_up_animations):
                    self.image = self.hurt_up_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
               
        if self.facing == "right":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > self.damage_animation_speed:  # Troca de frame a cada 50ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_right_animations):
                    self.image = self.hurt_right_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
                
        if self.facing == "left":
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time > self.damage_animation_speed:  # Troca de frame a cada 50ms
                self.damage_time = current_time
                if self.damage_index < len(self.hurt_left_animations):
                    self.image = self.hurt_left_animations[self.damage_index]
                    self.damage_index += 1
                else:
                    self.damage = False
                    
class Boss(Enemy):
    def __init__(self, game, kind, x, y, name, last_boss=False):
        # Inicializa o boss assim como um inimigo, apenas alterando a IA, o nome e a condição de último boss
        super().__init__(game, kind, x, y)
        self.name = name
        self.last_boss = last_boss
        self.ai = Boss_IA(self)
        
    def check_health(self):
        # Verifica se o boss morreu, se morrer, apaga o boss
        if self.health <= 0:
            self.kill()
            # Se for o último boss, mostra a tela de vitória e aplica a música de vitória
            if self.last_boss:
                self.game.play_sound("victory_sound")
                self.game.game_over("Parabéns, você venceu!")
            else:
                # Adiciona o xp ao player, permite o spawn de inimigos e cancela o evento do boss
                self.game.player.xp += config.enemy_xp[self.kind]
                self.game.spawned_boss = False
                self.game.allow_spawn_enemies = True
               
    def despawn(self):
        # Não despawna o boss
        pass
                
class EnemyAttack(pygame.sprite.Sprite):
    def __init__(self, game, kind, enemy):
        
        # Define propriedades dos ataques dos inimigos
        self.game = game
        self.kind = kind
        self.class_ = "EnemyAttack"
        self.enemy = enemy
        self._layer = config.layers["enemy_layer"]
        self.groups = self.game.all_sprites, self.game.enemy_attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.animation_speed = config.enemy_attack_animation_speed[self.kind]
        
        # Define a imagem inicial do ataque do inimigo
        keys_animations = list(self.game.sprites.enemy_attack_animations[self.kind].keys())
        self.image = self.game.sprites.enemy_attack_animations[self.kind][keys_animations[0]][0]
        
        # Calcula a velocidade e direção do ataque usando vetores
        self.speed = config.enemy_attack_speed[self.kind]
        direction = pygame.math.Vector2(self.game.player.rect.x - self.enemy.rect.x, self.game.player.rect.y - self.enemy.rect.y)
        self.velocity = direction.normalize() * self.speed
        
        # Faz o ataque spawnar fora do inimigo
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
        # Atualiza o movimento do ataque
        self.movement()
        # Atualiza a animação do ataque
        self.animate()
        # Atualiza a posição do ataque e colisão
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.collide_blocks()
        #DAVI
        #self.attack_with_joystick()

        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        # Calcula os deslocamentos nos eixos do ataque
        self.x_change = self.velocity[0]
        self.y_change = self.velocity[1]
        
    def animate(self):        
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
        # Se o ataque colidir, apaga o ataque
        hits = pygame.sprite.spritecollide(self, self.game.collidable_sprites, False)
        if hits:
            self.kill()