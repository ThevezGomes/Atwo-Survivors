import pygame
from abc import ABC, abstractmethod

class Button:
    def __init__(self, x, y, width, height, fg, content, fontsize, image_path='../assets\img\GenericButton.png', image_path_hover='../assets\img\GenericButtonActive.png'):
        # Define a fonte e outras variáveis
        self.font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', fontsize)  # Fonte do texto
        self.content = content
        self.fg = fg
        self.image_path = image_path  # Caminho para a imagem normal
        self.image_path_hover = image_path_hover  # Caminho para a imagem de hover

        # Rect do botão
        self.rect = pygame.Rect(x, y, width, height)

        # Carregar a imagem normal e a imagem de hover
        self.image = pygame.image.load(self.image_path)  # Carregar a imagem normal
        self.image = pygame.transform.scale(self.image, (width, height))  # Redimensionar a imagem para o tamanho do botão

        self.image_hover = pygame.image.load(self.image_path_hover)  # Carregar a imagem de hover
        self.image_hover = pygame.transform.scale(self.image_hover, (width, height))  # Redimensionar a imagem de hover

        self.current_image = self.image  # Inicializa com a imagem normal

    def draw(self, screen):
        # Desenhar o botão com a imagem selecionada
        screen.blit(self.current_image, self.rect.topleft)

        # Renderiza o texto centralizado no botão
        text = self.font.render(self.content, True, self.fg)
        text_rect = text.get_rect()  # Pega o retângulo do texto sem centralizar
        text_rect.centerx = self.rect.centerx  # Centraliza horizontalmente
        text_rect.centery = self.rect.centery - 5  # Centraliza verticalmente

        screen.blit(text, text_rect)


    def update(self, mouse_pos):
        # Altera a imagem do botão se o mouse estiver sobre ele
        if self.rect.collidepoint(mouse_pos):
            self.current_image = self.image_hover  # Muda para a imagem de hover
        else:
            self.current_image = self.image  # Muda para a imagem normal

    def is_pressed(self, pos, pressed):
        # Verifica se o botão foi clicado
        return self.rect.collidepoint(pos) and pressed[0]
    
class hub:
    def __init__(self, x, y, slot_size, max_slots, type_hub):
        self.x = x  # Posição horizontal do inventário
        self.y = y  # Posição vertical do inventário
        self.slot_size = slot_size  # Tamanho de cada slot no inventário
        self.max_slots = max_slots  # Número máximo de slots no inventário
        self.items = []  # Lista para armazenar os itens do inventário

        # Imagem do slot (pode ser um fundo para os itens)
        self.slot_image = pygame.image.load('../assets/img/HotbarSkillBackground1.png')
        self.slot_image = pygame.transform.scale(self.slot_image, (slot_size, slot_size))

        # Define o layout ('horizontal' ou 'vertical')
        self.type_hub = type_hub

    def add_item(self, item_name, item_image_path, max_level=5):
        # Verifica se o item já está no inventário
        for item in self.items:
            if item['name'] == item_name:
                # Se o item já está no inventário, aumenta o nível até o limite
                if item['level'] < max_level:
                    item['level'] += 1
                return

        # Se o item não está no inventário e há espaço, adiciona
        if len(self.items) < self.max_slots:
            item_image = pygame.image.load(item_image_path)
            item_image = pygame.transform.scale(item_image, (self.slot_size - 10, self.slot_size - 10))
            self.items.append({'name': item_name, 'image': item_image, 'level': 1, 'max_level': max_level})

    def draw(self, screen):
        # Desenha cada slot do inventário
        for i in range(self.max_slots):
            # Ajusta o posicionamento dos slots com base no tipo de hub
            if self.type_hub == 'inventory':
                slot_x = self.x + i * (self.slot_size + 5)
                slot_y = self.y
            if self.type_hub == 'skills_hub':
                slot_x = self.x
                slot_y = self.y + i * (self.slot_size + 5)

            screen.blit(self.slot_image, (slot_x, slot_y))

            # Se houver um item neste slot, desenha ele e seu nível
            if i < len(self.items):
                item_x = slot_x + (self.slot_size - self.items[i]['image'].get_width()) // 2
                item_y = slot_y + (self.slot_size - self.items[i]['image'].get_height()) // 2
                screen.blit(self.items[i]['image'], (item_x, item_y))

                # Exibir o nível do item
                font = pygame.font.Font(None, 24)
                level_text = font.render(f"Nv. {self.items[i]['level']}", True, pygame.Color('white'))
                screen.blit(level_text, (item_x, item_y - 10))

            if self.type_hub == 'inventory':
                if i == self.selected_item_index:
                    pygame.draw.rect(screen, pygame.Color('yellow'), (slot_x, slot_y, self.slot_size, self.slot_size), 3)

class Inventory(hub):
    def __init__(self, x, y, slot_size, max_slots):
        super().__init__(x, y, slot_size, max_slots, type_hub="inventory")
        self.selected_item_index = 0

    def selection_event(self, event):
        # Verifica se uma tecla numérica foi pressionada
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                slot_num = event.key - pygame.K_1  # Converte tecla para índice de slot
                if 0 <= slot_num < self.max_slots:
                    self.selected_item_index = slot_num if slot_num < len(self.items) else None

class Skills_hub(hub):
    def __init__(self, x, y, slot_size, max_slots):
        super().__init__(x, y, slot_size, max_slots, type_hub='skills_hub')

class Bar(ABC):
    def __init__(self, max, border_color, background_color, color, width, height, x, y):
        self.max = max
        self.amount = max
        self.border_color = border_color
        self.background_color = background_color
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, screen):
        pass

class HealthBar(Bar):
    def __init__(self, max, border_color, background_color, color, width, height, x, y):
        super().__init__(max, border_color, background_color, color, width, height, x, y)

    def draw(self, screen):
        filled = self.width * (self.amount / self.max)

        # Desenha a borda (ajustando as coordenadas para a borda)
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x - 3, self.y - 3, self.width + 6, self.height + 6))
        # Desenha o fundo da barra
        background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        background_surface.fill(self.background_color)  # Cor de fundo com alpha
        screen.blit(background_surface, (self.x, self.y))
        # Desenha a parte preenchida da barra
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x + (self.width - filled), self.y, filled, self.height))

class ExperienceBar(Bar):
    def __init__(self, max, border_color, background_color, color, width, height, x, y, level):
        super().__init__(max, border_color, background_color, color, width, height, x, y)
        self.level = level
        self.amount = 0  # Inicia a quantidade de experiência em 0

    def draw(self, screen):
        filled = self.amount / self.max  # Calcula o preenchimento da barra de experiência

        # Desenha a borda (ajustando as coordenadas para a borda)
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x-(self.width/2) - 3, self.y - 3, self.width + 6, self.height + 6))
        # Desenha o fundo da barra
        background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        background_surface.fill(self.background_color)  # Cor de fundo com alpha
        screen.blit(background_surface, (self.x-(self.width/2), self.y))
        # Desenha a parte preenchida da barra
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x-(self.width/2), self.y, self.width * filled, self.height)) 

        # Exibe o nível atual
        font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 24)
        level_text = font.render(f'Lvl: {self.level}', True, (255, 255, 255))
        
        # Calcula a posição para centralizar o texto
        text_width = level_text.get_width()
        text_x = self.x - (text_width / 2)  # Subtrai a metade da largura do texto da posição central da barra
        
        # Calcula a posição para centralizar o texto verticalmente
        text_y = self.y + (self.height / 2) - (level_text.get_height() / 2)  # Posição vertical centralizada

        # Posiciona o texto centralizado na barra de experiência
        screen.blit(level_text, (text_x, text_y))

class TimeGame:
    def __init__(self, x, y):
        self.font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 32)
        self.x = x
        self.y = y
        self.events = {}
        self.time_paused = False
        self.elapsed_time = 0  # Tempo acumulado de pausa

    def start(self):
        self.start_time = pygame.time.get_ticks()

    def add_event(self, time_seconds, func):
        self.events[time_seconds * 1000] = func

    def pause(self):
        self.elapsed_time += pygame.time.get_ticks() - self.start_time  # Adiciona o tempo decorrido antes da pausa
        self.time_paused = True

    def resume(self):
        self.start_time = pygame.time.get_ticks()  # Reinicia o tempo de início para considerar o tempo restante
        self.time_paused = False

    def update(self, screen):
        if not self.time_paused:
            current_time = pygame.time.get_ticks()
            total_elapsed = current_time - self.start_time + self.elapsed_time  # Inclui o tempo pausado
            
            # Atualiza o timer na tela
            minutes = total_elapsed // 60000
            seconds = (total_elapsed % 60000) // 1000
            timer_text = self.font.render(f'{minutes:02}:{seconds:02}', True, (255, 255, 255))
            text_size = timer_text.get_size()
            timer_x = self.x - (text_size[0]/2)
            screen.blit(timer_text, (timer_x, self.y))

            # Checa e dispara eventos de tempo
            for event_time, func in list(self.events.items()):
                if total_elapsed >= event_time:
                    func()
                    del self.events[event_time]
