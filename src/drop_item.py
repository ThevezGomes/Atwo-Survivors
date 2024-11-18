import pygame
from main_character import *
from config import * 

class ItemDrop(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type):
        super().__init__()
        self.item_type = item_type  # 'Pigseed', 'Pigtree', 'Camacho_Supremacy', etc.
        
        # Definindo a imagem com base no tipo de item
        if self.item_type == 'Pigseed':
            self.image = pygame.image.load('../assets/drop_itens_sprites/Pigseed.png').convert_alpha()
        elif self.item_type == 'Pigtree':
            self.image = pygame.image.load('../assets/drop_itens_sprites/Pigtree.png').convert_alpha()
        elif self.item_type == 'Camacho_Supremacy':
            self.image = pygame.image.load('../assets/drop_itens_sprites/Camacho_Supremacy.png').convert_alpha()
        elif self.item_type == 'Carlos_Ivan_Supremacy':
            self.image = pygame.image.load('../assets/drop_itens_sprites/Carlos_Ivan_Supremacy.png').convert_alpha()
        else:
            self.image = pygame.Surface((20, 20))  # Caso nenhum tipo seja válido, cria uma superfície vazia

        # Ajustando o tamanho da imagem
        self.image = pygame.transform.scale(self.image, (30, 30))  # Ajusta o tamanho
        self.rect = self.image.get_rect(center=(x, y))  # Define a posição do item
    
    def apply_effect(self, player):
        # Aplica o efeito do item no jogador
        if self.item_type == 'Pigseed':
            player.health = min(player.health + 50, config.max_health["player"])
        elif self.item_type == 'Pigtree':
            player.health = min(player.health + 100, config.max_health["player"])
        elif self.item_type == 'Camacho_Supremacy':
            player.experience += 25  
        elif self.item_type == 'Carlos_Ivan_Supremacy':
            player.experience += 60
