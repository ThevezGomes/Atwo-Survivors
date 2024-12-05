"""Módulo para manipulação de sprites"""

import pygame
import config
import math

# Classe que separa as imagens em sprites
class Spritesheet:
    """Classe que carrega e manipula uma spritesheet para extrair e ajustar sprites."""
    def __init__(self, file):
        """
        Inicializa uma nova instância da classe `Spritesheet`.

        Args:
            file (str): Caminho do arquivo da imagem da spritesheet a ser carregada.
        """
        # Carrrega a imagem
        self.sheet = pygame.image.load(file).convert()

    # Separa o sprite e o aplica em uma superficie
        self.sheet = pygame.image.load(file).convert_alpha()
        
    def get_sprite(self, x, y, width, height, size=config.size["player"]):
        """
        Extrai um sprite específico da spritesheet e o redimensiona.

        Args:
            x (int): Coordenada x do canto superior esquerdo do sprite na spritesheet.
            y (int): Coordenada y do canto superior esquerdo do sprite na spritesheet.
            width (int): Largura do sprite na spritesheet.
            height (int): Altura do sprite na spritesheet.
            size (int, optional): Fator de escala para redimensionar o sprite. Default é `config.size["player"]`.

        Returns:
            Surface: O sprite extraído e redimensionado.
        """
        sprite = pygame.Surface([width, height], pygame.SRCALPHA)
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        # Define o fundo da imagem para o mesmo fundo do game
        sprite.set_colorkey((0,0,0))
        # Ajusta o tamanho da imagem
        sprite = pygame.transform.scale(sprite, (size*width/height, size))
        return sprite