import pygame

class Item:
    def __init__(self, name, description, sprite_path):
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = sprite_path

class Ability:
    def __init__(self, name, description, sprite_path):
        self.name = name  # Nome da habilidade
        self.description = description  # Descrição da habilidade
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = sprite_path