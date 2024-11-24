"""Armazena todos os itens e habilidades do jogo"""
from props import *
from game import *
        
class ItemsArmazenamento:
    def __init__(self):
        self.itens = {"attacks": {"energy_ball": Item("energy_ball","Bola de energia", "Destroi tudo no caminho.", max_level=5),
                      "demon_sword": Item("demon_sword", "Espada Demoníaca", "O poder do inferno", max_level=5),
                      "shot_gun": Item("shot_gun", "Escopeta", "Tiro em área", max_level=5)},
                      "abilities": {"nice_boots": Ability("nice_boots", "Botas Legais", "Aumenta a velocidade", "speed", max_level=5),
                      # "divine_blessing": Ability("divine_blessing", "Benção Divina", "Recupera a vida lentamente", "regeneration", max_level=5),
                      "saint_cross": Ability("saint_cross", "Cruz Santa", "Aumenta a vida máxima", "life", max_level=5),
                      "rage_of_the_gods": Ability("rage_of_the_gods", "Fúria dos Deuses", "Aumenta o ataque", "attack", max_level=5),
                      "indestructible_shield": Ability("indestructible_shield", "Escudo Indestrutível", "Aumenta a defesa", "defense", max_level=5),
                      # "Artemis_aim": Ability("Artemis_aim", "Mira de Artemis", "Aumenta o alcance", "range", max_level=5),
                      "Apollo_maestry": Ability("Apollo_maestry", "Mastria de Apolo", "Aumenta a velocidade de disparo", "firing_speed", max_level=5)}
                      }
        self.itens_player_max = {"Baconseed": Consumible("Baconseed", "Semente de Bacon", "Cura metade da vida."),
                                 "Starpotion": Consumible("Starpotion", "Estrela da Sabedoria", "Aumenta a experiência.")}