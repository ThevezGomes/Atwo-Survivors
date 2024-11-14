import pygame

class Item:
    def __init__(self, name, description, sprite_path, level= 1, max_level = 5):
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        self.level = level
        self.max_level = max_level
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = sprite_path
        self.image = pygame.image.load(self.sprite)

class Ability:
    def __init__(self, name, description, sprite_path, level= 1, max_level = 5):
        self.name = name  # Nome da habilidade
        self.description = description  # Descrição da habilidade
        self.level = level
        self.max_level = max_level
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = sprite_path