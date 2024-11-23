import pygame
import config
import math

# Classe que separa as imagens em sprites
class Spritesheet:
    def __init__(self, file):
        # Carrrega a imagem
        self.sheet = pygame.image.load(file).convert()

    # Separa o sprite e o aplica em uma superficie
        self.sheet = pygame.image.load(file).convert_alpha()
        
    def get_sprite(self, x, y, width, height, size=config.size):
        sprite = pygame.Surface([width, height], pygame.SRCALPHA)
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        # Define o fundo da imagem para o mesmo fundo do game
        sprite.set_colorkey((0,0,0))
        sprite = pygame.transform.scale(sprite, (size*width/height, size))
        return sprite