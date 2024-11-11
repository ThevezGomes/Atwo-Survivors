""""Métodos de IA que serão utilizados pelos inimigos"""
from game import *
from main_character import Player
import config

class AI:
    def __init__(self, game, enemy):
        self.game = game
        self.enemy = enemy # Inimigo em questão que está buscando alguém pra atacar
        self.list_of_entities = self.game.entities # Lista de todas as entidades do jogo
        self.target = None # O alvo do inimigo

    def distance_vector(self, player): # Retorna a distância entre o inimigo e uma determinada entidade

        self.delta_x = player.rect.x - self.enemy.rect.x
        self.delta_y = player.rect.y - self.enemy.rect.y
        squared_vector_norm = self.delta_x ** 2 + self.delta_y **2

        return squared_vector_norm 

    def target_detector(self): # Detecta o alvo a partir das entidades em jogo
        for s in self.list_of_entities:
            if  isinstance(s, Player):
                if self.distance_vector(s) <= config.enemy_fov:
                    self.target = s


    def enemy_pursue(self):

        constant = config.enemy_speed / self.distance_vector(self.target)

        self.enemy.x_change = constant * self.delta_x
        self.enemy.y_change = constant * self.delta_y
