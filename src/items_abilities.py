"""Armazena todos os itens e habilidades do jogo"""
from props import *
from game import *
        
class ItemsArmazenamento:
    def __init__(self):
        self.itens = {"energy_ball": Item("energy_ball","Bola de energia", "Destroi tudo no caminho.", max_level=5)}