""""Métodos de IA que serão utilizados pelos inimigos"""
from game import *
from main_character import Player
import config
import math

def target_detector(enemy): # Detecta o alvo a partir das entidades em jogo
    player = enemy.game.player

    if distance_vector(enemy, player) <= config.enemy_fov:
            return player
    else: return None

def get_deltas(enemy, player):
    delta_x = player.rect.x - enemy.rect.x
    delta_y = player.rect.y - enemy.rect.y
     
    return delta_x, delta_y


def distance_vector(enemy, player): # Retorna a distância entre o inimigo e uma determinada entidade

    if player == None: return (0,0), 0

    delta_x = get_deltas(enemy,player)[0]
    delta_y = get_deltas(enemy,player)[1]
    vector_norm = math.sqrt(delta_x ** 2 + delta_y **2)

    print("coordenadas inimigo",enemy.rect.x, enemy.rect.y)
    print("coordenadas jogador",player.rect.x, player.rect.y)
    print("vetor distância",delta_x, delta_y)
    print("-----------------------------")

    return vector_norm 

def enemy_pursue(enemy):

    game = enemy.game
    target = target_detector(enemy)
    vector_module = distance_vector(enemy, target)
    print("vector_module:", vector_module)

    if vector_module > 1 :
        constant = config.enemy_speed / vector_module
    else: constant = 0

    print("constant", constant)

    x_change = constant * get_deltas(enemy, target)[0]
    y_change = constant * get_deltas(enemy, target)[1]

    print("delta_x",get_deltas(enemy, target)[0])
    print("delta_y",get_deltas(enemy, target)[1])


    return x_change, y_change







