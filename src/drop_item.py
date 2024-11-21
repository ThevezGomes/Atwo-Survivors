import pygame
from main_character import *
from config import *
from main_character import *


class ItemDrop(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type):
        super().__init__()
        self.item_type = item_type  # 
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 15000


        # Definindo a imagem com base no tipo de item
        if self.item_type == 'Baconseed':
            self.image = pygame.image.load('../assets/drop_itens_sprites/Pigtree.png').convert_alpha()
        elif self.item_type == 'Baconfruit':
            self.image = pygame.image.load('../assets/drop_itens_sprites/Bacon.jpg').convert_alpha()
        elif self.item_type == 'Camacho_Supremacy':
            self.image = pygame.image.load('../assets/drop_itens_sprites/CamachoSupremacy.webp').convert_alpha()
        elif self.item_type == 'Carlos_Ivan_Supremacy':
            self.image = pygame.image.load('../assets/drop_itens_sprites/CarlosIvanSupremacy.png').convert_alpha()
        else:
            self.image = pygame.Surface((20, 20))  # Caso nenhum tipo seja válido, cria uma superfície vazia

        # Ajustando o tamanho da imagem
        self.image = pygame.transform.scale(self.image, (35, 35))  # Ajusta o tamanho
        self.rect = self.image.get_rect(center=(x, y))  # Define a posição do item
    
    def update(self):
        current_time = pygame.time.get_ticks()
        time_left = self.lifetime - (current_time - self.spawn_time)
    
        # Muda a transparência nos últimos 2 segundos
        if time_left < 2000:
            alpha = max(0, int(255 * (time_left / 2000)))  # Reduz gradualmente
            self.image.set_alpha(alpha)

        # Remove o item se o tempo de vida expirar
        if time_left <= 0:
            self.kill()
        

    def apply_effect(self, player):
        # Aplica o efeito do item no jogador
        if self.item_type == 'Baconseed':
            player.health += 70 
        elif self.item_type == 'Baconfruit':
            player.health += 140 
        elif self.item_type == 'Camacho_Supremacy':
            player.xp += 60   
        elif self.item_type == 'Carlos_Ivan_Supremacy':
            player.xp += 120


        