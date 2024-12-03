import pygame
from main_character import *
from config import *
from main_character import *


class ItemDrop(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, game):
        super().__init__()
        self.game = game
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
        elif sel.item == 'Giantpotion':
            self.image =pygame.image.load('../assets/drop_itens_sprites/Giantpot.png')
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
            self.game.play_sound("pig_sound")
            self.game.play_sound("eating_sound")
            if player.health + (player.max_health // 2) > player.max_health:
                player.health = player.max_health
            else:
                player.health += (player.max_health // 2)
        elif self.item_type == 'Baconfruit':
            self.game.play_sound("eating_sound")
            if player.health + (player.max_health) > player.max_health:
                player.health = player.max_health
            else:
                player.health += (player.max_health) 
        elif self.item_type == 'Starpotion':
            self.game.play_sound("xp_potion_sound")
            player.xp += 60   
        elif self.item_type == 'Hugepotion':
            self.game.play_sound("xp_potion_sound")
            player.xp += 120


        