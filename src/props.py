"""Módulo que define classes para representar itens, habilidades e consumíveis no jogo."""

import pygame
from repositorio_sprites import *

class Item:
    """Classe que representa um item genérico no jogo."""
    def __init__(self, kind, name, description, level= 1, max_level = 5):
        """
        Inicializa uma nova instância da classe `Item`.

        Args:
            kind (str): O tipo do item.
            name (str): O nome do item.
            description (str): A descrição do item.
            level (int, opcional): O nível do item. Padrão é 1.
            max_level (int, opcional): O nível máximo do item. Padrão é 5.
        """

        self.kind = kind  # Tipo do item
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        self.level = level  # Nivel
        self.max_level = max_level  # Nivel maximo
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = Sprites().attack_sprites[kind]["icon"]
        self.image = pygame.image.load(self.sprite)

class Ability:
    """Classe que representa uma habilidade no jogo, como os buffs."""
    def __init__(self, kind, name, description, buff, level= 1, max_level = 5):
        """
        Inicializa uma nova instância da classe `Ability`.

        Args:
            kind (str): O tipo da habilidade.
            name (str): O nome da habilidade.
            description (str): A descrição da habilidade.
            buff (any): O buff que a habilidade oferece.
            level (int, opcional): O nível da habilidade. Padrão é 1.
            max_level (int, opcional): O nível máximo da habilidade. Padrão é 5.
        """

        self.kind = kind  # Tipo do item
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        self.buff = buff  # Buff
        self.level = level  # Nivel
        self.max_level = max_level  # Nivel maximo
        
        # Carrega o sprite do item a partir de um caminho de imagem
        self.sprite = Sprites().abilities_sprites[kind]
        self.image = pygame.image.load(self.sprite)
        
class Consumible:
    """Classe que representa um consumível no jogo."""
    def __init__(self, kind, name, description):
        """
        Inicializa uma nova instância da classe `Consumible`.

        Args:
            kind (str): O tipo do consumível.
            name (str): O nome do consumível.
            description (str): A descrição do consumível.
        """
        
        self.kind = kind  # Tipo do item
        self.name = name  # Nome do item
        self.description = description  # Descrição do item
        
        self.sprite = Sprites().consumible_sprites[kind]
        self.image = pygame.image.load(self.sprite)