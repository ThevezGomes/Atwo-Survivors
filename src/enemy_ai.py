""""Métodos de IA que serão utilizados pelos inimigos"""
from game import *
from main_character import Player
import config
import enemy_config
import math

class Enemy_AI:

    def __init__(self, enemy):
        self.enemy = enemy
        self.game = enemy.game
        self.player = self.game.player
        self.seach_distance = enemy_config.enemy_fov
        self.facing = "down"

    def enemy_pursue(self):

        target = self.target_detector()
        if not isinstance(target, Player):
            return 0, 0
        vector_module = self.distance_vector(target)

        if vector_module > 1 :
            constant = self.enemy.speed / vector_module
        else: constant = 0

        delta_x, delta_y = self.get_deltas(target)

        x_change = constant * delta_x
        y_change = constant * delta_y

        if abs(x_change)> abs(y_change):
            if x_change > 0: self.facing = "right"
            else: self.facing = "left"
        else:
            if y_change > 0: self.facing = "down"
            else: self.facing = "up"

        return x_change, y_change
    

    def target_detector(self): # Verifica se o player está próximo para liberar perseguição

        if self.distance_vector(self.player) <= self.seach_distance and self.distance_vector(self.player) > 40:
                return self.player
        else: return None

    def get_deltas(self, player): # Calcula a distância entre o inimigo e uma entidade
        delta_x = player.rect.x - self.enemy.rect.x
        delta_y = player.rect.y - self.enemy.rect.y

        return delta_x, delta_y


    def distance_vector(self, target): # Retorna a distância entre o inimigo e uma determinada entidade

        if not isinstance(target, Player):
            return 0
        
        delta_x, delta_y = self.get_deltas(target)
        vector_norm = math.sqrt(delta_x ** 2 + delta_y **2)

        return vector_norm 










