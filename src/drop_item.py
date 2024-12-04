import pygame
from main_character import *
from config import *
from main_character import *
import math

class ItemDrop(pygame.sprite.Sprite):
    """
    Classe para representar um item dropado no jogo. 
    Cada item possui um tipo, uma imagem associada, um tempo de vida e pode aplicar efeitos no jogador.

    Args:
        x (int): Coordenada x da posição inicial do item.
        y (int): Coordenada y da posição inicial do item.
        item_type (str): Tipo do item (e.g., 'Baconseed', 'Baconfruit', 'Starpotion', 'Hugepotion').

    Attributes:
        item_type (str): Tipo do item.
        spawn_time (int): Momento (em milissegundos) em que o item foi criado.
        lifetime (int): Tempo de vida total do item, em milissegundos.
        image (pygame.Surface): Imagem que representa o item.
        rect (pygame.Rect): Retângulo delimitador para posicionamento e colisão do item.
    """
    def __init__(self, x, y, item_type):
        
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
        else:
            self.image = pygame.Surface((20, 20)) 

        # Ajustando o tamanho da imagem
        self.image = pygame.transform.scale(self.image, (35, 35))  # Ajusta o tamanho
        self.rect = self.image.get_rect(center=(x, y))  # Define a posição do item
    
    def update(self):

        """
        Atualiza o estado do item, incluindo o controle de tempo de vida e efeitos visuais.
        Remove o item caso seu tempo de vida expire.
        """

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
        
        """
        Aplica o efeito do item no jogador.
        
        Args:
            player (Player): Objeto do jogador que coletou o item.

        Efeitos:
            - Baconseed: Recupera 50% da vida máxima do jogador.
            - Baconfruit: Recupera 100% da vida máxima do jogador.
            - Starpotion: Aumenta o XP atual em 40%.
            - Hugepotion: Aumenta o XP atual em 60%.
        """

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
            player.xp += player.xp +player.xp *0.6 
       
        