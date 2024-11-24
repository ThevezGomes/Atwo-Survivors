import pygame
from repositorio_sprites import *

class Item:
    def __init__(self, kind, name, description, level= 1, max_level = 5):
        self.kind = kind
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        self.level = level
        self.max_level = max_level
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = Sprites().attack_sprites[kind]["icon"]
        self.image = pygame.image.load(self.sprite)

class Ability:
    def __init__(self, kind, name, description, buff, level= 1, max_level = 5):
        self.kind = kind
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        self.buff = buff
        self.level = level
        self.max_level = max_level
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = Sprites().abilities_sprites[kind]
        self.image = pygame.image.load(self.sprite)
        
class Consumible:
    def __init__(self, kind, name, description):
        self.kind = kind
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        
        self.sprite = Sprites().consumible_sprites[kind]
        self.image = pygame.image.load(self.sprite)