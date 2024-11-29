import pygame
from main_character import *
from config import *
from main_character import *
import math

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
        elif self.item_type == 'Starpotion':
            self.image = pygame.image.load('../assets/drop_itens_sprites/starpotion.png').convert_alpha()
        elif self.item_type == 'Hugepotion':
            self.image = pygame.image.load('../assets/drop_itens_sprites/hugepotion.png').convert_alpha()
        elif self.item_type == 'Giantpotion':
            self.image =pygame.image.load('../assets/drop_itens_sprites/Giantpot.png')
        else:
            self.image = pygame.Surface((20, 20)) 

        # Ajustando o tamanho da imagem
        self.image = pygame.transform.scale(self.image, (35, 35))  # Ajusta o tamanho
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect(center=(x, y))  # Define a posição do item
    
    def update(self):
        current_time = pygame.time.get_ticks()
        time_left = self.lifetime - (current_time - self.spawn_time)
    
        if self.item_type == 'Giantpotion':
            intensity = (math.sin(current_time / 500)+1) * 0.5

             #Verifica se a imagem original existe
            if hasattr(self, "original_image") and self.original_image:
                # Cria uma cópia da imagem original
                self.image = self.original_image.copy()

                # Cria uma superfície para o brilho
                color_overlay = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
                color_overlay.fill((0, 0, 0, int(255 * intensity)))

                # Aplica a sobreposição com blend
                self.image.blit(color_overlay, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

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
            if player.health + (player.max_health // 2) > player.max_health:
                player.health = player.max_health
            else:
                player.health += (player.max_health // 2)
        elif self.item_type == 'Baconfruit':
            if player.health + (player.max_health) > player.max_health:
                player.health = player.max_health
            else:
                player.health += (player.max_health) 
        elif self.item_type == 'Starpotion':
            player.xp += player.xp +player.xp *0.4   
        elif self.item_type == 'Hugepotion':
            player.xp += player.xp +player.xp *0.6 
        elif self.item_type == 'Giantpotion':
            player.xp += player.xp * 3


        