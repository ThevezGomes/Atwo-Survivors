"""Módulo responsável por definir as classes e funções relacionadas à interface do jogador no jogo"""
import pygame
from abc import ABC, abstractmethod
import config

class Button:
    """
    Representa um botão interativo na interface do jogo.

    Este botão exibe uma imagem normal e uma imagem de hover quando o cursor do mouse está sobre ele. 
    Ele também permite a verificação de cliques para interação.

    Attributes:
        font (pygame.font.Font): A fonte usada para renderizar o texto no botão.
        content (str): O texto exibido no botão.
        fg (tuple[int, int, int]): A cor do texto no botão em formato RGB.
        image_path (str): O caminho para a imagem do botão em estado normal.
        image_path_hover (str): O caminho para a imagem do botão em estado de hover.
        rect (pygame.Rect): O retângulo que define a área do botão.
        image (pygame.Surface): A superfície da imagem do botão em estado normal.
        image_hover (pygame.Surface): A superfície da imagem do botão em estado de hover.
        current_image (pygame.Surface): A superfície da imagem atualmente exibida.
    """
    def __init__(self, x, y, width, height, fg, content, fontsize, image_path='../assets\img\GenericButton.png', image_path_hover='../assets\img\GenericButtonActive.png'):
        """
        Inicializa um botão com imagens, texto e posicionamento especificados.

        Args:
            x (int): A coordenada x do botão.
            y (int): A coordenada y do botão.
            width (int): A largura do botão.
            height (int): A altura do botão.
            fg (tuple[int, int, int]): A cor do texto no botão em formato RGB.
            content (str): O texto exibido no botão.
            fontsize (int): O tamanho da fonte do texto.
            image_path (str, optional): O caminho para a imagem do botão em estado normal. Padrão: '../assets/img/GenericButton.png'.
            image_path_hover (str, optional): O caminho para a imagem do botão em estado de hover. Padrão: '../assets/img/GenericButtonActive.png'.
        """
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
        """
        Desenha o botão na tela.

        Args:
            screen (pygame.Surface): A superfície onde o botão será desenhado.
        """
        # Desenhar o botão com a imagem selecionada
        screen.blit(self.current_image, self.rect.topleft)

        # Renderiza o texto centralizado no botão
        text = self.font.render(self.content, True, self.fg)
        text_rect = text.get_rect()  # Pega o retângulo do texto sem centralizar
        text_rect.centerx = self.rect.centerx  # Centraliza horizontalmente
        text_rect.centery = self.rect.centery - 5  # Centraliza verticalmente

        screen.blit(text, text_rect)


    def update(self, mouse_pos):
        """
        Atualiza a imagem do botão com base na posição do mouse, quando o mause pass por cima do botão ele muda de cor.

        Args:
            mouse_pos (tuple[int, int]): A posição do mouse na tela.
        """
        # Altera a imagem do botão se o mouse estiver sobre ele
        if self.rect.collidepoint(mouse_pos):
            self.current_image = self.image_hover  # Muda para a imagem de hover
        else:
            self.current_image = self.image  # Muda para a imagem normal

    def is_pressed(self, pos, pressed):
        """
        Verifica se o botão foi clicado.

        Args:
            pos (tuple[int, int]): A posição do clique do mouse.
            pressed (tuple[bool]): Um tuplo representando os estados dos botões do mouse.

        Returns:
            bool: True se o botão foi clicado, caso contrário False.
        """
        # Verifica se o botão foi clicado
        return self.rect.collidepoint(pos) and pressed[0]
    
class Hub:
    """
    Representa uma interface de inventário ou barra de habilidades no jogo.

    A classe Hub pode ser usada para criar diferentes tipos de interfaces, como inventários horizontais ou verticais, permitindo a adição, exibição e organização de itens.

    Attributes:
        x (int): Coordenada horizontal do hub na tela.
        y (int): Coordenada vertical do hub na tela.
        slot_size (int): Tamanho de cada slot do hub.
        max_slots (int): Número máximo de slots disponíveis no hub.
        items (list): Lista de itens armazenados no hub.
        slot_image (pygame.Surface): Imagem de fundo dos slots.
        type_hub (str): Tipo do hub, podendo ser 'inventory' ou 'skills_hub'.
    """
    def __init__(self, x, y, slot_size, max_slots, type_hub):
        """
        Inicializa o hub com a posição, tamanho dos slots, capacidade máxima e tipo de layout.

        Args:
            x (int): Posição horizontal do hub.
            y (int): Posição vertical do hub.
            slot_size (int): Tamanho de cada slot no hub.
            max_slots (int): Número máximo de slots no hub.
            type_hub (str): Tipo do hub, definindo o layout ('inventory' ou 'skills_hub').
        """
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

    def add_item(self, item_n):
        """
        Adiciona um item ao hub, verificando duplicidade e respeitando a capacidade máxima.

        Args:
            item_n (object): O item a ser adicionado, contendo atributos como nome, nível e sprite.
        """
        # Verifica se o item já está no inventário
        for item in self.items:
            if item[0].name == item_n.name:
                # Se o item já está no inventário, aumenta o nível até o limite
                if item[0].level < item_n.max_level:
                    item[0].level += 1
                return

        # Se o item não está no inventário e há espaço, adiciona
        if len(self.items) < self.max_slots:
            item_image = pygame.image.load(item_n.sprite)
            item_image = pygame.transform.scale(item_image, (self.slot_size - 10, self.slot_size - 10))
            self.items.append([item_n, item_image])

    def draw(self, screen):
        """
        Desenha o hub e seus itens na tela.

        Args:
            screen (pygame.Surface): A superfície onde o hub será desenhado.
        """
        # Desenha cada slot do inventário
        for i in range(self.max_slots):
            # Ajusta o posicionamento dos slots com base no tipo de hub
            if self.type_hub == 'inventory':
                slot_x = self.x + i * (self.slot_size + 5)
                slot_y = self.y
            elif self.type_hub == 'skills_hub':
                slot_x = self.x
                slot_y = self.y + i * (self.slot_size + 5)

            screen.blit(self.slot_image, (slot_x, slot_y))

            # Se houver um item neste slot, desenha ele e seu nível
            if i < len(self.items):
                item_x = slot_x + (self.slot_size - self.items[i][1].get_width()) // 2
                item_y = slot_y + (self.slot_size - self.items[i][1].get_height()) // 2
                screen.blit(self.items[i][1], (item_x, item_y))

                # Exibir o nível do item
                font = pygame.font.Font(None, 24)
                level_text = font.render(f"Nv. {self.items[i][0].level}", True, pygame.Color('white'))
                screen.blit(level_text, (item_x, item_y - 10))

            # Se o item estiver selecionado desenha uma borda amarela em volta de seu slot
            if self.type_hub == 'inventory':
                if i == self.selected_item_index:
                    pygame.draw.rect(screen, pygame.Color('yellow'), (slot_x, slot_y, self.slot_size, self.slot_size), 3)
                    
    def item_belonging_check(self, item):
        """
        Verifica se um item específico pertence ao hub.

        Args:
            item (object): O item a ser verificado.

        Returns:
            bool: True se o item pertence ao hub, caso contrário False.
        """
        for objeto in self.items:
            if objeto == item:
                return True
        
        return False

class Inventory(Hub):
    """
    Representa o inventário do jogador, permitindo a seleção de itens.

    Essa classe herda de `Hub` e adiciona funcionalidades específicas para a seleção de itens, incluindo suporte a eventos de teclado e rolagem do mouse.

    Attributes:
        selected_item_index (int or None): O índice do item atualmente selecionado no inventário.
    """
    def __init__(self, x, y, slot_size, max_slots):
        """
        Inicializa o inventário com posição, tamanho dos slots e capacidade máxima.

        Args:
            x (int): Coordenada horizontal do inventário na tela.
            y (int): Coordenada vertical do inventário na tela.
            slot_size (int): Tamanho de cada slot no inventário.
            max_slots (int): Número máximo de slots disponíveis no inventário.
        """
        super().__init__(x, y, slot_size, max_slots, type_hub="inventory")
        self.selected_item_index = None

    def selection_event(self, event):
        """
        Gerencia os eventos de seleção de itens no inventário.

        Permite selecionar itens usando teclas numéricas (1 a 9) ou a rolagem do mouse.

        Args:
            event (pygame.event.Event): Evento capturado do Pygame.
        """
        # Verifica se uma tecla numérica foi pressionada
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                slot_num = event.key - pygame.K_1  # Converte tecla para índice de slot
                if 0 <= slot_num < self.max_slots:
                    self.selected_item_index = slot_num if slot_num < len(self.items) else None
        # Permite a selação de itens usando o scroll
        elif event.type == pygame.MOUSEWHEEL:
            if len(self.items) > 0:
                # Selecionado o índice do item com base no scroll
                self.selected_item_index = (self.selected_item_index or 0) + event.y
                # Garante que apenas seleciones itens validados
                self.selected_item_index %= len(self.items)

class Skills_hub(Hub):
    """
    Representa a barra de habilidades do jogador.

    Essa classe herda de `Hub` e é usada para organizar e exibir as habilidades do jogador de forma vertical.
    """

    def __init__(self, x, y, slot_size, max_slots):
        """
        Inicializa a barra de habilidades com posição, tamanho dos slots e capacidade máxima.

        Args:
            x (int): Coordenada horizontal da barra de habilidades na tela.
            y (int): Coordenada vertical da barra de habilidades na tela.
            slot_size (int): Tamanho de cada slot na barra de habilidades.
            max_slots (int): Número máximo de slots disponíveis na barra de habilidades.
        """
        super().__init__(x, y, slot_size, max_slots, type_hub='skills_hub')

class Bar(ABC):
    """
    Classe abstrata que representa uma barra gráfica, como uma barra de vida ou de xp.

    Attributes:
        max (int): O valor máximo que a barra pode representar.
        amount (int): O valor atual da barra, que não pode exceder o máximo.
        border_color (tuple): Cor da borda da barra em formato RGB.
        background_color (tuple): Cor de fundo da barra em formato RGB.
        color (tuple): Cor da barra que representa o valor atual em formato RGB.
        width (int): Largura total da barra.
        height (int): Altura total da barra.
        x (int): Coordenada horizontal da barra na tela.
        y (int): Coordenada vertical da barra na tela.
    """

    def __init__(self, max, border_color, background_color, color, width, height, x, y):
        """
        Inicializa os atributos básicos de uma barra.

        Args:
            max (int): O valor máximo que a barra pode representar.
            border_color (tuple): Cor da borda da barra (RGB).
            background_color (tuple): Cor de fundo da barra (RGB).
            color (tuple): Cor da barra que representa o valor atual (RGB).
            width (int): Largura total da barra.
            height (int): Altura total da barra.
            x (int): Posição horizontal da barra na tela.
            y (int): Posição vertical da barra na tela.
        """

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
        """
        Método abstrato para desenhar a barra na tela.

        Esse método deve ser implementado nas classes filhas.

        Args:
            screen (pygame.Surface): A superfície do Pygame onde a barra será desenhada.
        """
        pass

class HealthBar(Bar):
    """
    Representa uma barra de saúde do jogador.

    Essa classe herda de `Bar` e inclui a funcionalidade de exibir a barra de saúde do jogador com um ícone ao lado, que representa o personagem.

    Attributes:
        base_width (int): Largura base da barra de saúde.
        character_icon (str): Caminho da imagem do ícone do personagem.
        original_x (int): Posição horizontal original da barra antes do ajuste de largura.
        icon_image (pygame.Surface): Superfície de imagem do ícone do personagem.
    """

    def __init__(self, max, border_color, background_color, color, base_width, height, x, y, character_icon):
        """
        Inicializa os atributos da barra de saúde.

        Args:
            max (int): O valor máximo de saúde que a barra pode representar.
            border_color (tuple): Cor da borda da barra (RGB).
            background_color (tuple): Cor de fundo da barra (RGB).
            color (tuple): Cor da parte preenchida da barra (RGB).
            base_width (int): Largura base da barra de saúde.
            height (int): Altura da barra de saúde.
            x (int): Posição horizontal da barra na tela.
            y (int): Posição vertical da barra na tela.
            character_icon (str): Caminho para a imagem do ícone do personagem.
        """
        super().__init__(max, border_color, background_color, color, base_width, height, x, y)
        self.base_width = base_width  # Largura base da barra
        self.character_icon = character_icon
        self.original_x = x
        self.icon_image = pygame.image.load(character_icon)
        self.icon_image = pygame.transform.scale(self.icon_image, (50, 50))

    def draw(self, screen):
        """
        Desenha a barra de saúde e o ícone do personagem na tela.

        Esse método atualiza o tamanho da barra com base na saúde máxima e exibe a parte preenchida de acordo com a quantidade de saúde atual. Também desenha a borda e o fundo da barra.

        Args:
            screen (pygame.Surface): A superfície do Pygame onde a barra será desenhada.
        """
        # Atualizar o tamanho da barra com base na vida máxima
        self.width = self.base_width * (self.max / config.max_health["player"])

        # Atualiza a posição da barra após o crescimento
        self.x = self.original_x + self.base_width - self.width

        # Calcular o preenchimento proporcional
        filled = self.width * (self.amount / self.max)

        # Desenhar a borda
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x - 3, self.y - 3, self.width + 6, self.height + 6))
        # Desenhar o fundo da barra
        background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        background_surface.fill(self.background_color)  # Cor de fundo com transparência
        screen.blit(background_surface, (self.x, self.y))
        # Desenhar a parte preenchida da barra
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x + (self.width - filled), self.y, filled, self.height))
        # Desenhar o ícone do personagem
        screen.blit(self.icon_image, (self.x + self.width, self.y - 16))

class ExperienceBar(Bar):
    """
    Representa uma barra de experiência do jogador, exibindo o nível e a quantidade de experiência atual.

    Essa classe herda de `Bar` e é usada para mostrar uma barra de progresso da experiência do jogador.

    Attributes:
        level (int): O nível atual do jogador.
        amount (int): A quantidade de experiência acumulada pelo jogador.
    """
    def __init__(self, border_color, background_color, color, width, height, x, y, level, xp):
        """
        Inicializa os atributos da barra de experiência.

        Args:
            border_color (tuple): Cor da borda da barra (RGB).
            background_color (tuple): Cor de fundo da barra (RGB).
            color (tuple): Cor da parte preenchida da barra (RGB).
            width (int): Largura da barra de experiência.
            height (int): Altura da barra de experiência.
            x (int): Posição horizontal da barra na tela.
            y (int): Posição vertical da barra na tela.
            level (int): O nível atual do jogador.
            xp (int): A quantidade de experiência inicial do jogador.
        """
        max = self.levels(level)
        super().__init__(max, border_color, background_color, color, width, height, x, y)
        self.level = level
        self.amount = xp  # Inicia a quantidade de experiência em 0

    def draw(self, screen):
        """
        Desenha a barra de experiência na tela, incluindo a borda, fundo, parte preenchida e o nível do jogador.

        Args:
            screen (pygame.Surface): A superfície do Pygame onde a barra será desenhada.
        """
        # EVITA QUE A BARRA DE EXPERIÊNCIA EXPLODA
        if self.amount > self.max:
            filled = 1
        else:
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
        
    def levels(self, level):
        """
        Calcula o valor máximo de experiência necessário para o nível atual.

        Args:
            level (int): O nível do jogador.

        Returns:
            int: O valor máximo de experiência necessário para o nível dado.
        """
        xp_level_1 = 100
        
        #return int(xp_level_1*(1.5)**level)
        if level <= 50:
            return 100
        elif level > 50:
            return 1000000

class BossBar(Bar):
    """
    Representa a barra de vida de um chefe (boss) em um jogo.

    Essa classe herda de `Bar` e é usada para mostrar uma barra de saúde para um chefe, com a exibição do nome do chefe na parte superior.

    Attributes:
        boss_name (str): O nome do chefe que a barra representa.
    """
    def __init__(self, max, border_color, background_color, color, width, height, x, y, boss_name):
        """
        Inicializa os atributos da barra do chefe.

        Args:
            max (int): O valor máximo de saúde do chefe.
            border_color (tuple): Cor da borda da barra (RGB).
            background_color (tuple): Cor de fundo da barra (RGB).
            color (tuple): Cor da parte preenchida da barra (RGB).
            width (int): Largura da barra.
            height (int): Altura da barra.
            x (int): Posição horizontal da barra na tela.
            y (int): Posição vertical da barra na tela.
            boss_name (str): O nome do chefe que a barra representa.
        """
        super().__init__(max, border_color, background_color, color, width, height, x, y)
        self.boss_name = boss_name

    def draw(self, screen):
        """
        Desenha a barra de saúde do chefe na tela, incluindo a borda, fundo, parte preenchida e o nome do chefe.

        Args:
            screen (pygame.Surface): A superfície do Pygame onde a barra será desenhada.
        """
        filled = self.amount / self.max  # Calcula o preenchimento da barra de experiência

        # Desenha a borda (ajustando as coordenadas para a borda)
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x-(self.width/2) - 3, self.y - 3, self.width + 6, self.height + 6))
        # Desenha o fundo da barra
        background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        background_surface.fill(self.background_color)  # Cor de fundo com alpha
        screen.blit(background_surface, (self.x-(self.width/2), self.y))
        # Desenha a parte preenchida da barra
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x-(self.width/2), self.y, self.width * filled, self.height)) 

        # Exibe o nome do boss
        font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 24)
        name_text = font.render(f"{self.boss_name}", True, (255, 255, 255))
        
        # Calcula a posição para centralizar o texto
        text_width = name_text.get_width()
        text_x = self.x - (text_width / 2)  # Subtrai a metade da largura do texto da posição central da barra
        
        # Calcula a posição para centralizar o texto verticalmente
        text_y = self.y - (self.height / 2) - (name_text.get_height() / 2) - 10  # Posição vertical centralizada

        # Posiciona o texto centralizado na barra
        screen.blit(name_text, (text_x, text_y))

class TimeGame:
    """
    Representa um temporizador de jogo que pode ser pausado, retomado e usado para disparar eventos em momentos específicos.

    Attributes:
        font (pygame.font.Font): Fonte usada para exibir o tempo.
        x (int): Coordenada horizontal para desenhar o temporizador na tela.
        y (int): Coordenada vertical para desenhar o temporizador na tela.
        events (dict): Dicionário que mapeia tempos específicos (em milissegundos) para funções de evento.
        time_paused (bool): Flag que indica se o temporizador está pausado.
        elapsed_time (int): Tempo acumulado de pausa, em milissegundos.
        start_time (int): Tempo em milissegundos no qual o temporizador foi iniciado.
        total_elapsed (int): Tempo total decorrido desde o início, incluindo pausas.
    """
    def __init__(self, x, y):
        """
        Inicializa o temporizador com uma fonte e define as coordenadas de desenho na tela.

        Args:
            x (int): Coordenada horizontal para a exibição do temporizador.
            y (int): Coordenada vertical para a exibição do temporizador.
        """
        self.font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 32)
        self.x = x
        self.y = y
        self.events = {}
        self.time_paused = False
        self.elapsed_time = 0  # Tempo acumulado de pausa
        self.start_time = pygame.time.get_ticks()
        self.total_elapsed = 0

    def start(self):
        """
        Inicia ou reinicia o temporizador, resetando o tempo acumulado de pausa e a hora de início.
        """
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        self.time_paused = False

    def add_event(self, time_seconds, func):
        """
        Adiciona um evento a ser disparado após um tempo específico, usando closure.

        Args:
            time_seconds (int): O tempo em segundos após o qual o evento será disparado.
            func (function): A função a ser chamada quando o tempo especificado for alcançado.
        """
        self.events[time_seconds * 1000] = func

    def pause(self):
        """
        Pausa o temporizador e acumula o tempo decorrido desde a última pausa ou início.
        """
        if not self.time_paused:
            self.elapsed_time += pygame.time.get_ticks() - self.start_time
            self.time_paused = True

    def resume(self):
        """
        Retoma a contagem do temporizador, reiniciando o tempo de início.
        """
        if self.time_paused:
            self.start_time = pygame.time.get_ticks()
            self.time_paused = False

    def update(self):
        """
        Atualiza o temporizador e dispara eventos que atingiram o tempo de execução.
        """
        if not self.time_paused:
            current_time = pygame.time.get_ticks()
            self.total_elapsed = self.elapsed_time + (current_time - self.start_time)

            # Checa e dispara eventos
            for event_time, func in list(self.events.items()):
                if self.total_elapsed >= event_time:
                    func()
                    del self.events[event_time]

    def draw(self, screen):
        """
        Desenha o temporizador na tela.

        Args:
            screen (pygame.Surface): A superfície do Pygame onde o temporizador será desenhado.
        """
        minutes = self.total_elapsed // 60000
        seconds = (self.total_elapsed % 60000) // 1000
        timer_text = self.font.render(f'{minutes:02}:{seconds:02}', True, (255, 255, 255))
        text_size = timer_text.get_size()
        timer_x = self.x - (text_size[0] / 2)
        screen.blit(timer_text, (timer_x, self.y))


class SelectionItem:
    """
    Representa um botão para seleção de um item, aprsentando o nome do item, icon e descrição.

    É usada no menu de selação de item, que é ativado quando o pesonagem sobe de nivél.

    Attributes:
        font_name (pygame.font.Font): Fonte usada para renderizar o nome do item.
        font_description (pygame.font.Font): Fonte usada para renderizar a descrição do item.
        item (object): O item que contém as propriedades como nome, descrição e ícone.
        fg (tuple): Cor do texto (R, G, B).
        image_path (str): Caminho para a imagem de fundo normal do item.
        image_path_hover (str): Caminho para a imagem de fundo do item em estado de hover.
        rect (pygame.Rect): Retângulo que define a posição e as dimensões do item na tela.
        image (pygame.Surface): Superfície da imagem de fundo normal.
        image_hover (pygame.Surface): Superfície da imagem de fundo de hover (não usada).
        current_image (pygame.Surface): A imagem atualmente visível (normal ou de hover).
        item_icon (pygame.Surface): Superfície da imagem do ícone do item.
    """
    def __init__(self, x, y, width, height, fg, item, fontsize):
        """
        Inicializa um botão/item de seleção com as propriedades fornecidas.

        Args:
            x (int): Coordenada x para a posição do item na tela.
            y (int): Coordenada y para a posição do item na tela.
            width (int): Largura do item.
            height (int): Altura do item.
            fg (tuple): Cor do texto (R, G, B).
            item (object): Objeto que contém as propriedades do item, como nome, descrição e ícone.
            fontsize (int): Tamanho da fonte para o texto do item.
        """
        # Define a fonte e outras variáveis
        self.font_name = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', fontsize)  # Fonte do texto
        self.font_description = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', fontsize -5) 
        self.item = item
        self.fg = fg
        self.image_path = '../assets\img\old-paper-sprite.png'  # Caminho para a imagem normal
        self.image_path_hover = '../assets\img\old-paper-sprite.png'  # Caminho para a imagem de hover

        # Rect do botão
        self.rect = pygame.Rect(x, y, width, height)

        # Carregar a imagem normal e a imagem de hover
        self.image = pygame.image.load(self.image_path)  # Carregar a imagem normal
        self.image = pygame.transform.scale(self.image, (width, height))  # Redimensionar a imagem para o tamanho do botão

        #Não esta sendo usado !!
        self.image_hover = pygame.image.load(self.image_path_hover)  # Carregar a imagem de hover
        self.image_hover = pygame.transform.scale(self.image_hover, (width, height))  # Redimensionar a imagem de hover

        self.current_image = self.image  # Inicializa com a imagem normal

        self.item_icon = pygame.image.load(self.item.sprite)  # Carregar a imagem normal
        self.item_icon = pygame.transform.scale(self.item_icon, (width/3, width/3))  # Redimensionar a imagem para o tamanho do botão

    def draw(self, screen):
        """
        Desenha o botão/item de seleção na tela, incluindo a imagem de fundo, ícone, nome e descrição.

        Args:
            screen (pygame.Surface): A superfície do Pygame onde o item será desenhado.
        """
        # Desenhar o botão com a imagem selecionada
        screen.blit(self.current_image, self.rect.topleft)

        # Função para quebrar texto em múltiplas linhas
        def wrap_text(text, font, max_width):
            """
            Quebra o texto em múltiplas linhas para se ajustar à largura máxima do botão.

            Args:
                text (str): O texto a ser quebrado.
                font (pygame.font.Font): A fonte usada para calcular a largura do texto.
                max_width (int): A largura máxima permitida para o texto.

            Returns:
                list: Lista de superfícies de texto quebradas em linhas.
            """
            words = text.split()
            lines = []
            current_line = ""
            for word in words:
                test_line = f"{current_line} {word}".strip()
                if font.size(test_line)[0] <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            lines.append(current_line)

            surfaces = []
            for line in lines:
                surface = font.render(line, True, self.fg)
                surfaces.append(surface)

            return surfaces
        
        # Definir largura máxima do texto
        max_width = self.rect.width - 25  # Margem horizontal

        # Quebrar e renderizar nome e descrição
        name_surfaces = wrap_text(self.item.name, self.font_name, max_width)
        description_surfaces = wrap_text(self.item.description, self.font_description, max_width)

        # Obtem os tamanhos dos elementos
        icon_height = self.item_icon.get_rect().height
        # Calcular a altura total das superfícies de nome
        name_height = 0
        for surface in name_surfaces:
            name_height += surface.get_height()
        # Calcular a altura total das superfícies de descrição
        description_height = 0
        for surface in description_surfaces:
            description_height += surface.get_height()
            
        total_height = icon_height + name_height + description_height + 30  # Inclui espaçamento entre os elementos

        # Calcular o ponto inicial para centralização vertical
        start_y = self.rect.top + (self.rect.height - total_height) // 2

        # Posicionar o ícone
        icon_rect = self.item_icon.get_rect()
        icon_rect.centerx = self.rect.centerx
        icon_rect.top = start_y
        screen.blit(self.item_icon, icon_rect)

        # Desenha o nome
        current_y = icon_rect.bottom + 10
        for surface in name_surfaces:
            rect = surface.get_rect(centerx=self.rect.centerx, top=current_y)
            screen.blit(surface, rect)
            current_y += surface.get_height()

        # Desenha a descrição
        current_y += 10
        for surface in description_surfaces:
            rect = surface.get_rect(centerx=self.rect.centerx, top=current_y)
            screen.blit(surface, rect)
            current_y += surface.get_height()

    #Não esta sendo usado!!!
    def update(self, mouse_pos):
        """
        Atualiza a imagem de fundo do item dependendo da posição do mouse.

        Args:
            mouse_pos (tuple): A posição atual do mouse (x, y).
        """
        # Altera a imagem do botão se o mouse estiver sobre ele
        if self.rect.collidepoint(mouse_pos):
            self.current_image = self.image_hover  # Muda para a imagem de hover
        else:
            self.current_image = self.image  # Muda para a imagem normal

    def is_pressed(self, pos, pressed):
        """
        Verifica se o botão foi clicado com base na posição do mouse e no estado dos botões do mouse.

        Args:
            pos (tuple): A posição do mouse (x, y).
            pressed (tuple): Estado dos botões do mouse.

        Returns:
            bool: Verdadeiro se o botão foi clicado, caso contrário, falso.
        """
        # Verifica se o botão foi clicado
        return self.rect.collidepoint(pos) and pressed[0]