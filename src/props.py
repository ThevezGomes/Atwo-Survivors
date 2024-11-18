import pygame
from repositorio_sprites import *

class Item:
    def __init__(self, game, kind, name, description, level= 1, max_level = 5):
        self.kind = kind
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        self.level = level
        self.max_level = max_level
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = Sprites().attack_sprites[kind]["icon"]
        self.image = pygame.image.load(self.sprite)
       
    def check_level(self):
        if self.level == self.max_level:
            self.game.all_sprites.pop(self.kind)
            
    def update(self):
        self.check_level()

class Ability:
    def __init__(self, game, kind, name, description, sprite_path, level= 1, max_level = 5):
        self.kind = kind
        self.name = name  # Nome da habilidade
        self.description = description  # Descrição da habilidade
        self.level = level
        self.max_level = max_level
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = sprite_path
        
    def check_level(self):
        if self.level == self.max_level:
            self.game.all_sprites.pop(self.kind)
            
    def update(self):
        self.check_level()