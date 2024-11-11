import pygame
import config
import math

# Classe que separa as imagens em sprites
class Spritesheet:
    def __init__(self, file):
        # Carrrega a imagem
        self.sheet = pygame.image.load(file).convert()

    # Separa o sprite e o aplica em uma superficie
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        # Define o fundo da imagem para o mesmo fundo do game
        sprite.set_colorkey((0,0,0))
        return sprite
