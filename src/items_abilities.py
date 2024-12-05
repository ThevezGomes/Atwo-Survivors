"""Armazena todos os itens e habilidades do jogo"""
from props import *
from game import *
        
class ItemsArmazenamento:
    """
    Gerencia todos os itens e habilidades do jogo, incluindo os itens que podem ser usados pelo jogador e os de nível máximo.
    
    A classe armazena os itens e habilidades em dicionários organizados por tipo, permitindo fácil acesso e manipulação.
    
    Atributos:
        itens (dict): Um dicionário contendo itens e habilidades disponíveis, organizados por categorias como "attacks" e "abilities".
        itens_player_max (dict): Um dicionário contendo itens que podem ser consumidos pelo jogador e que representam os itens de nível máximo.
    """
    # Armazena todos os itens que podem aparecer e os itens de nivel maximo
    def __init__(self):
        """
        Inicializa a classe com os itens e habilidades pré-definidos.
        """
        self.itens = {"attacks": {"energy_ball": Item("energy_ball","Bola de energia", "Destroi tudo no caminho.", max_level=5),
                      "demon_sword": Item("demon_sword", "Espada Demoníaca", "O poder do inferno", max_level=5),
                      "shotgun": Item("shotgun", "Escopeta", "Tiro em área", max_level=5)},
                      "abilities": {"nice_boots": Ability("nice_boots", "Botas Legais", "Aumenta a velocidade", "speed", max_level=5),
                      # "divine_blessing": Ability("divine_blessing", "Benção Divina", "Recupera a vida lentamente", "regeneration", max_level=5),
                      "saint_cross": Ability("saint_cross", "Cruz Santa", "Aumenta a vida máxima", "life", max_level=5),
                      "rage_of_the_gods": Ability("rage_of_the_gods", "Fúria dos Deuses", "Aumenta o ataque", "attack", max_level=5),
                      "indestructible_shield": Ability("indestructible_shield", "Escudo Indestrutível", "Aumenta a defesa", "defense", max_level=5),
                      # "Artemis_aim": Ability("Artemis_aim", "Mira de Artemis", "Aumenta o alcance", "range", max_level=5),
                      "Apollo_maestry": Ability("Apollo_maestry", "Mastria de Apolo", "Aumenta a velocidade de disparo", "firing_speed", max_level=5)}
                      }
        self.itens_player_max = {"Baconseed": Consumible("Baconseed", "Semente de Bacon", "Cura metade da vida."),
                                 "Baconfruit": Consumible("Baconfruit", "Bacon maduro", "Cura a vida inteira.")}
