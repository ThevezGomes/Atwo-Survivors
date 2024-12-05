"""Módulo que define a classe `Game`, que é responsável por gerenciar a lógica do jogo, a criação de elementos do jogo e a execução da mecânica do jogo em si."""

import pygame
import sys
import random
from pytmx.util_pygame import load_pygame
from pytmx import pytmx
from ui import *
from main_character import *
from enemies import *
from sprites import *
from config import *
from props import *
from items_abilities import *
from map import *
import repositorio_sprites as rs
import repositorio_sons as rsound
import random
import numpy as np
import math
from drop_item import * 


class Game:
    """
    Classe central do jogo.
    """
    def __init__(self):
        """
        Inicializa os principais componentes do jogo, incluindo tela, sons, mapas, sprites e inventários.
        """
        # Inicia o pygame, o mixer de sons e a tela
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Define propriedades essenciais para o jogo
        self.clock = pygame.time.Clock()
        self.running = True # Indica se o jogo está em execução.
        self.paused = False # Indica se o jogo está pausado.
        self.level_up = False # Indica se o jogador atingiu o próximo nível.
        self.restart =False # Indica se o jogo deve ser reiniciado.
        self.sprites = rs.Sprites() # Gerencia os sprites do jogo.
        self.sounds = rsound.Sound() # Gerencia os sons do jogo.
        self.spawn_time = 0 # Tempo para spawn de inimigos.
        self.spawning = False # Indica se novos inimigos estão sendo gerados.
        self.allow_spawn_enemies = True # Permite ou bloqueia a geração de inimigos.
        self.spawned_boss = False # Indica se o chefe foi gerado.
        self.show_message = False # Exibe mensagens temporárias na tela.
        self.enemies_list = [] # Lista de inimigos ativos no jogo.
        self.difficulty_ratio = 1 # Multiplicador de dificuldade do jogo.
        self.phase = 1
        self.enemy_number = 20
        self.enemies_alive = 0
        
        # Define os buffs das habilidades
        self.buffs = {
            "attack": 0,
            "defense": 0,
            "firing_speed": 0,
            "range": 0,
            "speed": 0,
            "life": 0,
            "regeneration": 0
            }
        
        # Carrega o mapa .tmx
        self.tmx_data = load_pygame("../assets/Tiled/tmx/Map2.tmx")

        self.font_title = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 54)
        self.font_text = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 32)

        #Imagens da tela inicial
        self.intro_background = pygame.image.load('../assets/img/Loginscreen.png').convert()
        target_height = self.screen.get_height()
        scaled_width = int(self.intro_background.get_width() * (target_height / self.intro_background.get_height()))
        self.intro_background = pygame.transform.scale(self.intro_background, (scaled_width, target_height))
        self.character = pygame.image.load('../assets/img/Warrior.png').convert_alpha()

        self.height_character = 88
        self.width_character = (self.height_character/22)*32
        self.character = pygame.transform.scale(self.character, (self.height_character,self.width_character)) #22x32

        # Cortar a imagem para centralizar horizontalmente na tela
        if scaled_width > self.screen.get_width():
            x_offset = (scaled_width - self.screen.get_width()) // 2
            self.intro_background = self.intro_background.subsurface((x_offset, 0, self.screen.get_width(), target_height))

        # Criar uma superfície escura semi-transparente
        self.dark_overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.dark_overlay.fill((0, 0, 0, 180))  # Escure a tela de fundo
        
        # Armazena os itens e armas que podem aparecer
        self.all_itens_classes = ["attacks", "abilities"]
        self.all_itens = ItemsArmazenamento().itens
        self.all_itens_max = ItemsArmazenamento().itens_player_max
        self.update_items = True
        self.update_abilities = True
        
        self.boss_list = boss_list

        #Criação do inventário (posição, tamanho do slot e número de slots)
        self.inventory = Inventory(x=10, y=self.screen.get_height() - 60, slot_size=50, max_slots=2) # Inventário do jogador com slots para itens.

        #Criação do hub de habilidades (posição, tamanho do slot e número de slots)
        self.skills_hub = Skills_hub(x=10, y=10, slot_size=40, max_slots=3) # Hub para exibição de habilidades disponíveis.

        #Timer do jogo
        self.game_timer = TimeGame(x=self.screen.get_width() /2, y=5)
        self.game_timer.add_event(60, self.increase_number_of_enemies)
        self.game_timer.add_event(120, self.increase_number_of_enemies)
        self.game_timer.add_event(180, self.increase_number_of_enemies)
        self.game_timer.add_event(240, self.increase_number_of_enemies)
        self.game_timer.add_event(295, self.MessageSpawnBoss)
        self.game_timer.add_event(300, self.SpawnBoss(False))
        self.game_timer.add_event(360, self.increase_number_of_enemies)
        self.game_timer.add_event(420, self.increase_number_of_enemies)
        self.game_timer.add_event(480, self.increase_number_of_enemies)
        self.game_timer.add_event(540, self.increase_number_of_enemies)
        self.game_timer.add_event(595, self.MessageSpawnBoss)
        self.game_timer.add_event(600, self.SpawnBoss(True))

        #Grupo de sprites 
        self.all_sprites = pygame.sprite.LayeredUpdates()
        #Grupo do sprites do item
        self.item_sprites = pygame.sprite.Group() 
        #Grupo do sprites de colisão
        self.collidable_sprites = pygame.sprite.Group()

        self.map_width = self.tmx_data.width * self.tmx_data.tilewidth
        self.map_height = self.tmx_data.height * self.tmx_data.tileheight

        # Define uma lista aleatória de itens que podem aparecer no menu de Level Up
        self.itens = [random.choice(list(self.all_itens.values())), random.choice(list(self.all_itens.values())), random.choice(list(self.all_itens.values()))]

    def SpawnBoss(self, final_boss):
        """
        Decora a função Spawnar_Boss()
        """
        def Spawnar_Boss():
            """
            Remove todos os inimigos e gera o chefe no centro da tela.
            """
            # Despawna todos os inimigos e spawna o boss
            pygame.mixer.music.stop()
            self.despawn_all_enemies()
            boss_kind = random.choice(self.boss_list)
            while not self.spawned_boss:
                angle = random.uniform(0, 2 * math.pi)
                radius = (self.screen.get_height() ** 2 + self.screen.get_width() ** 2) ** 0.5 / 8
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                
                spawn_pos = pygame.Rect((x + self.player.rect.x + self.player.rect.width / 2), 
                (y + self.player.rect.y + self.player.rect.height / 2), char_size_colision[0], char_size_colision[1])
                
                if not any(spawn_pos.colliderect(rect) for rect in self.blocked_rects):
                    self.spawned_boss = True
            self.boss = Boss(self, boss_kind, (x + self.player.rect.x + self.player.rect.width / 2), (y + self.player.rect.y + self.player.rect.height / 2), boss_name[boss_kind], final_boss)
            # Barra de vida do Boss
            self.boss_bar = BossBar(max=config.max_health["enemies"][boss_kind], border_color =(40, 34, 31), background_color=(255, 255, 255, 50), color=(138, 11, 10), width=300, height=20, x=self.screen.get_width() /2, y=75, boss_name=self.boss.name)
            pygame.mixer.music.load(music_theme[boss_kind])
            pygame.mixer.music.play(loops=-1)
        return Spawnar_Boss   

    def new(self):
        """
        Inicializa um novo estado de jogo, configurando grupos de sprites, o jogador, e as barras de status.
        """

        self.playing = True # Define como True para indicar que o jogo está em execução.
        pygame.mixer.music.load("../assets/sounds/ambient_theme.mp3")
        pygame.mixer.music.play(loops=-1)

        # Define grupos de sprites com propriedades que serao utilizadas
        self.all_sprites = pygame.sprite.LayeredUpdates() # Grupo de todos os sprites no jogo.
        self.blocks = pygame.sprite.LayeredUpdates() # Grupo de blocos do mapa com propriedades de colisão.
        self.enemies = pygame.sprite.LayeredUpdates() # Grupo de sprites de inimigos.
        self.enemy_attacks = pygame.sprite.LayeredUpdates() # Grupo de sprites de ataques inimigos.
        self.attacks = pygame.sprite.LayeredUpdates() # Grupo de sprites dos ataques do jogador.

        # Carrega os tiles e define colisões com base nas camadas
        self.load_map()

        # Cria o jogador na posicao central da tela
        self.player = Player(self, (self.screen.get_width() - config.char_size[0]) // 2, (self.screen.get_height() - config.char_size[1]) // 2) # Instância do jogador posicionada no centro da tela.
        
        # Barra de vida do jogador
        self.health_bar = HealthBar(max=self.player.max_health, border_color =(40, 34, 31), background_color=(255, 255, 255, 50), color=(163, 31, 13), base_width=250, height=20, x=self.screen.get_width() - 310, y=self.screen.get_height() - 45, character_icon="../assets/img/WarriorIcon.png")
        self.health_bar.amount = self.player.health
        
        # Barra de experiência
        self.experience_bar = ExperienceBar(border_color =(40, 34, 31),  background_color=(255, 255, 255, 50), color=(0, 255, 0), width=200, height=25, x=self.screen.get_width() /2 , y=45, level=self.player.level, xp=self.player.xp)

        self.blocked_polygons = [obj for obj in self.tmx_data.objects if obj.name == "Poligono"]

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.inventory.draw(self.screen) # Adciona o inventario a tela do jogo
        self.skills_hub.draw(self.screen)
        self.health_bar.draw(self.screen) # Adciona a barra de vida na tela
        # Adiciona a barra de experiência apenas se não tiver um Boss
        if self.spawned_boss == False:
            self.experience_bar.draw(self.screen) # Adciona a barra de experiência na tela
        # Se tiver um boss então adciona a barra de vida do boss
        else:
            self.boss_bar.draw(self.screen)
        self.game_timer.draw(self.screen) # Adciona o timer ao jogo
        self.draw_message() # Em caso de haver uma mensagem, adciona a mensagem na tela
        self.clock.tick(60)
        self.buffs_apply()

        pygame.display.update()

    def update(self):
        """
        Renderiza todos os elementos visuais do jogo na tela.
        """

        #Atualiza todos os sprites e suas propriedades
        self.all_sprites.update()
        
        #Atualiza a barra de vida do jogador
        self.health_bar.amount = self.player.health 
        self.health_bar.max = self.player.max_health 
        # Atualiza a barra de experiência do jogador
        self.experience_bar.level = self.player.level
        self.experience_bar.max = self.experience_bar.levels(self.player.level)
        self.experience_bar.amount = self.player.xp
        # Atualiza os itens que apareceram no menu de Level Up
        self.items_list_choice()
        self.game_timer.update() # Atualiza o timer
        
        # Spawna os inimigos
        if self.allow_spawn_enemies:
            self.spawn_enemies()
        self.cheats()
        
        # Atualiza a barra de vida do boss
        if self.spawned_boss:
            self.boss_bar.amount = self.boss.health
        
        # Detecta colisão com itens
        collided_items = pygame.sprite.spritecollide(self.player, self.item_sprites, True)
        for item in collided_items:
            # Aplica o efeito do item
            item.apply_effect(self.player)  

    def run(self):
        """
        Executa o loop principal do jogo, processando eventos, atualizando estados e chamando métodos de atualização e draw.

        Changed Attributes:
        running (bool): Atualizado para False quando o jogo deve ser encerrado.
        paused (bool): Alternado para pausar ou retomar o jogo.
        level_up (bool): Verificado para exibir o menu de level up.
        player.death (bool): Definido como True se a saúde do jogador for zero.
        player.game_over_sound (bool): Ativado quando o jogador morre.
        spawned_boss (bool): Verificado para pausar o temporizador quando um chefe está presente.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Define running como False para encerrar o loop principal
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused  # Alterna o estado de pausa
                    if self.paused:
                        self.game_timer.pause() # Pausa o relogio
                        self.pause_menu()  # Chama o menu de pausa
                        self.game_timer.resume() # Retorna o relogio
            
            # Cria o ataque do jogador quando é apertado o botao direito do mouse
            elif pygame.mouse.get_pressed()[0]:
                # Ataca com o ataque base se nada tiver selecionado
                if self.inventory.selected_item_index != None:
                    self.mouse_position = pygame.mouse.get_pos()
                    self.player.atacar(self, self.player.rect.x + self.player.rect.width/2, self.player.rect.y + self.player.rect.height/2, self.inventory.items[self.inventory.selected_item_index][0].kind, self.mouse_position, self.inventory.items[self.inventory.selected_item_index][0].level)
                # Ataca com a arma selecionada
                else:
                    self.mouse_position = pygame.mouse.get_pos()
                    self.player.atacar(self, self.player.rect.x + self.player.rect.width/2, self.player.rect.y + self.player.rect.height/2, "wave", self.mouse_position)
            self.inventory.selection_event(event)

        # Chama o menu de Level Up quando subir de nível
        if self.level_up == True:
                self.game_timer.pause() 
                pygame.time.delay(350)
                self.level_up_menu(self.itens)
                self.game_timer.resume()
        
        # Se o jogador tiver com a vida zerada, ativa a morte do jogador e o som de game over
        if self.player.health <= 0:
            self.player.death = True
            self.player.game_over_sound = True
        
        # Chance contínua de spawnar itens durante o jogo
        if random.random() < 0.01:  
            self.spawn_item()

        # Evento do Boss
        if self.spawned_boss == True:
            self.game_timer.pause()
        
        self.update()
        self.draw()

        self.clock.tick(60)  # Controle de FPS
   
    def transform_tile_image(self, tile_image, gid):
        """
        Recebe os tiles do mapa e verifica se recebem o flip dentro do tmx
        """
        
        flipped_horizontally = bool(gid & (1 << 31))  # Verifica o rotação horizontal
        flipped_vertically = bool(gid & (1 << 30))    # Verifica o rotação vertical
        flipped_diagonally = bool(gid & (1 << 29))    # Verifica o rotação diagonal (rotação de 90 graus)

        # Limpa os bits de transformação para obter o GID base
        gid &= 0x1FFFFFFF

        # Aplica rotação se necessário (diagonal flip é equivalente a uma rotação de 90 graus)
        if flipped_diagonally:
            tile_image = pygame.transform.rotate(tile_image, 90)

        # Aplica flip horizontal e vertical
        if flipped_horizontally or flipped_vertically:
            tile_image = pygame.transform.flip(tile_image, flipped_horizontally, flipped_vertically)

        return tile_image

    def load_map(self):
        """
        Carrega e inicializa o mapa do jogo a partir de um arquivo TMX, incluindo a adição de tiles, objetos e áreas de colisão.
        """

        # Coordenadas do centro do mapa e da tela
        target_x, target_y = 1260, 1610
        
        #Coordenadas do centro da tela
        screen_center_x, screen_center_y = 460, 454

        # Calcula o deslocamento necessário para centralizar
        offset_x = target_x - screen_center_x
        offset_y = target_y - screen_center_y

        # Itera pelas camadas visíveis do mapa
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):  # Camadas baseadas em tiles
                for x, y, gid in layer:
                    if gid == 0:  # Ignora tiles vazios
                        continue

                    # Obtém a superfície do tile do GID
                    tile_image = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile_image:
                        # Aplica as transformações usando a função transform_tile_image
                        tile_image = self.transform_tile_image(tile_image, gid)

                        # Calcula a posição no mapa
                        pos = (x * self.tmx_data.tilewidth - offset_x, y * self.tmx_data.tileheight - offset_y)

                        # Cria o sprite do tile
                        tile = Tile(pos, tile_image, [self.all_sprites])

                        # Adiciona ao grupo de colisões se for colidível
                        if layer.name in ("Objetos", "Fundo"):
                            self.collidable_sprites.add(tile)

        # Itera pelos objetos do mapa
        for obj in self.tmx_data.objects:
            pos = (obj.x - offset_x, obj.y - offset_y)

            # Objetos com imagens (vegetação, pedras, etc.)
            if obj.type in ("Montanha", "Vegetacao", "Pedras", "Lapide", "Cerca") and obj.image:
                image = obj.image

                if hasattr(obj, 'gid') and obj.gid:
                    image = self.transform_tile_image(image, obj.gid)

                # Cria o tile e ajusta o tamanho
                tile = Tile(pos, image, [self.all_sprites, self.collidable_sprites])
                tile.scale(obj.width, obj.height)

                # Adiciona ao grupo de colisão
                self.collidable_sprites.add(tile)

        #Para os itens não nascerem na posição de um objeto 
        self.blocked_rects = []  # Lista de áreas bloqueadas como retângulos
        for obj in self.tmx_data.objects:
            if obj.type in ("Montanha", "Vegetacao", "Pedras", "Lapide", "Cerca"):
                # Cria um retângulo bloqueado baseado na posição e dimensões do objeto
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.blocked_rects.append(rect)

    def spawn_item(self):
        """
        Carrega e spawna os itens do ItemDrop
        """
        
        spawn_attempts = 8  # Número máximo de tentativas
        spawn_probability = 0.7  # Probabilidade de spawn

        # Controla a probabilidade de spawn
        if random.random() > spawn_probability:
            return

        # Dimensões do mapa
        map_width = self.tmx_data.width * self.tmx_data.tilewidth
        map_height = self.tmx_data.height * self.tmx_data.tileheight

        # Calcula o deslocamento da câmera
        offset_x, offset_y = self.calculate_camera_offset()

        for _ in range(spawn_attempts):
            # Gera coordenadas aleatórias dentro dos limites do mapa
            spawn_x = random.randint(offset_x, map_width - offset_x)
            spawn_y = random.randint(offset_y, map_height - offset_y)

            # Cria um retângulo representando a posição do item
            item_rect = pygame.Rect(spawn_x, spawn_y, 1, 1)

            # Verifica se a posição gerada não colide com objetos bloqueados
            if not self.is_position_blocked(item_rect):
                # Define o tipo de item a ser spawnado
                item_type = random.choice(["Baconseed", "Baconfruit", "Starpotion", "Hugepotion"])

                # Cria e posiciona o item
                item = ItemDrop(spawn_x, spawn_y, item_type, self)

                # Adiciona o item aos grupos de sprites
                self.item_sprites.add(item)
                self.all_sprites.add(item)

                # Sai do loop após posicionar o item
                break


    def is_position_blocked(self, item_rect):
        """
        Verifica colisão com retângulos bloqueados inseridos no mapa
        """

        if any(item_rect.colliderect(rect) for rect in self.blocked_rects):
            return True

        # Verifica colisão com polígonos bloqueados
        for polygon in self.blocked_polygons:
            if self.check_polygon_collision(item_rect, polygon):
                return True

        return False


    def check_polygon_collision(self, item_rect, polygon):
        """
        Certifica-se de que o objeto tem o atributo 'as_points'
        """

        if not hasattr(polygon, "as_points"):
            return False

        # Obtém os pontos do polígono como uma lista de tuplas
        polygon_points = polygon.as_points  # Sem os parênteses

        # Verifica se algum vértice do polígono está dentro do retângulo
        if any(item_rect.collidepoint(point) for point in polygon_points):
            return True

        # Verifica se o centro do retângulo está dentro do polígono
        center_x = item_rect.x + item_rect.width // 2
        center_y = item_rect.y + item_rect.height // 2
        if self.is_point_in_polygon((center_x, center_y), polygon_points):
            return True

        return False


    def is_point_in_polygon(self, point, polygon_points):
        """
        Algoritmo de Ponto no Polígono (Ray Casting)
        """

        x, y = point
        n = len(polygon_points)
        inside = False

        p1x, p1y = polygon_points[0]
        for i in range(n + 1):
            p2x, p2y = polygon_points[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside
    
    def calculate_camera_offset(self):
        """ 
        Calcula o deslocamento da câmera com base nas coordenadas do alvo e da tela
        """

        target_x, target_y = 1260, 1610  # Coordenadas do alvo no mapa
        screen_center_x, screen_center_y = 460, 454  # Centro da tela
        offset_x = target_x - screen_center_x
        offset_y = target_y - screen_center_y
        return offset_x, offset_y

    def intro_screen(self):
        """
        Exibe a tela de introdução do jogo com opções para iniciar ou sair.
        """

        # Define que a tela de intro deve aparecer
        intro = True
        title = self.font_title.render('Atwo Survivors', True, pygame.Color('white'))
        title_rect = title.get_rect(topleft=(10, 10))

        # Dimensoes da tela
        screen_width, screen_height = self.screen.get_size()

        # Centraliza o titulo horizontalmente e posiciona no topo
        title_rect = title.get_rect(center=(screen_width // 2, screen_height // 4))

        # Dimensoes do botão
        button_width, button_height = 150, 65

        # Calcula as posições x e y para centralizar o botao
        button_x = (screen_width - button_width) // 2 + 100
        button_y = (screen_height - button_height) // 2  # Ajuste para um pouco abaixo do titulo

        # Cria o botao Play centralizado
        play_button = Button(button_x, button_y, button_width, button_height, pygame.Color('white'), 'Jogar', 32)
        quit_button = Button(button_x, button_y + button_height + 20, button_width, button_height, pygame.Color('white'), 'Sair', 32)
        
        pygame.mixer.music.load("../assets/sounds/main_theme.mp3")
        pygame.mixer.music.play(loops=-1)

        # Loop da tela de introção, espera que uma das opções seja escolida para iniciar o jogo ou fechar ele
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            # Atualiza o botão e verifica se foi clicado
            play_button.update(mouse_pos)
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                self.play_sound("button_sound")
                pygame.mixer.music.stop()
                intro = False
                self.new() # Inicia o jogo
                self.game_timer.start() # Inicia o timer do jogo 
            
            quit_button.update(mouse_pos)
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.play_sound("button_sound")
                intro = False
                self.running = False
            
            # Desenha o fundo, título e botão
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))
            self.screen.blit(title, title_rect)
            play_button.draw(self.screen)
            quit_button.draw(self.screen)
            
            # Desenhar personagem e rótulo "Guerreiro"
            button_x_caracter = button_x -150
            button_y_caracter = button_y

            button_x_caracter_label = button_x_caracter + 45
            button_y_caracter_label = button_y_caracter + self.height_character + 50

            self.screen.blit(self.character, (button_x_caracter, button_y_caracter))
            character_label = self.font_text.render("Guerreiro", True, pygame.Color('white'))
            character_label_rect = character_label.get_rect(center=(button_x_caracter_label, button_y_caracter_label))
            self.screen.blit(character_label, character_label_rect)
            
            # Atualiza a tela
            self.clock.tick(60)
            pygame.display.flip()

    def game_over(self, mensage="Fim de jogo"):
        """
        Exibe a tela de 'Game Over' quando o jogo termina, oferecendo opções para reiniciar ou sair.
        """
        
        # Define que a tela de Game Over deve aparecer
        over = True
        pygame.mixer.music.stop()

        paused_surface = self.screen.copy()  # Captura o estado atual do jogo
        self.blur(paused_surface, 200)

        # Dimensoes da tela
        screen_width, screen_height = self.screen.get_size()

        title = self.font_title.render(mensage, True, pygame.Color('white'))
        title_rect = title.get_rect(center=(screen_width // 2, ((screen_height - title.get_height()) // 2) -50))

        # Dimensoes do botão
        button_width, button_height = 200, 75

        # Calcula as posição y para centralizar o botao
        button_y = ((screen_height - button_height) // 2 ) +50 # Ajuste para um pouco abaixo do titulo

        # Cria o botao Play centralizado
        restart_button = Button(screen_width//2 - button_width -10, button_y, button_width, button_height, pygame.Color('white'), 'Resetar', 32)
        quit_button = Button(screen_width//2 +10, button_y, button_width, button_height, pygame.Color('white'), 'Sair', 32)

        # Loop da tela de Game Over, espera que um dos botões seja apertado para fechar o jogo ou iniciar uma nova partida
        while over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    over = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            # Atualiza o botão e verifica se foi clicado
            restart_button.update(mouse_pos)
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.play_sound("button_sound")
                over = False
                self.restart = True
            
            quit_button.update(mouse_pos)
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.play_sound("button_sound")
                over = False
                self.running = False
            
            # Desenha o fundo, título e botão
            self.screen.blit(paused_surface, (0, 0))
            self.screen.blit(title, title_rect)

            # Atualiza e desenha os botões
            restart_button.update(pygame.mouse.get_pos())
            quit_button.update(pygame.mouse.get_pos())
            restart_button.draw(self.screen)
            quit_button.draw(self.screen)

            # Atualiza a tela
            self.clock.tick(60)
            pygame.display.flip()

    def blur(self, surface, n):
        """
        Aplica um efeito de desfoque (blur) em uma superfície, sendo usado para escurecer a tela do jogo quando ele esta pausado.
        """

        # Aplica  um efeito de blur na tela
        blur_overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        blur_overlay.fill((0, 0, 0, n))  # Opacidade a 180
        surface.blit(blur_overlay, (0, 0))

    def pause_menu(self):
        """
        Exibe o menu de pausa, permitindo que o jogador retome o jogo, reinicie ou saia.
        """

        # Congela o jogo e exibe o menu de pausa
        paused_surface = self.screen.copy()  # Captura o estado atual do jogo
        self.blur(paused_surface, 180)
        
        # Carregar e centralizar o fundo do menu
        menu_background = pygame.image.load('../assets\img\SimplePanel01.png').convert_alpha()
        menu_background = pygame.transform.scale(menu_background, (400, 400))
        menu_rect = menu_background.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        
        # Configuração do título do menu
        title_font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 40)
        title_text = title_font.render("Menu de Pausa", True, pygame.Color('white'))
        title_rect = title_text.get_rect(center=(menu_rect.centerx, menu_rect.top + 70))
        
        # Criação dos botões "Retomar" e "Sair" usando a classe Button
        button_width, button_height = 200, 65
        button_spacing = 20
        
        resume_button = Button(menu_rect.centerx - button_width // 2, menu_rect.top + 120, button_width, button_height, pygame.Color('white'), 'Retomar', 24)
        restart_button = Button(menu_rect.centerx - button_width // 2, resume_button.rect.bottom + button_spacing, button_width, button_height, pygame.Color('white'), 'Resetar', 24)
        exit_button = Button(menu_rect.centerx - button_width // 2, restart_button.rect.bottom + button_spacing, button_width, button_height, pygame.Color('white'), 'Sair', 24)
        
        pygame.mixer.music.pause()
        pygame.mixer.stop()
        
        # Loop de pausa: substitui temporariamente o loop principal do jogo, impedindo qualquer atualização.
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = False  # Retomar o jogo
                        pygame.mixer.music.unpause()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        # Aplica o som de botao
                        self.play_sound("button_sound")
                        self.paused = False  # Retomar o jogo
                        pygame.mixer.music.unpause()
                    if restart_button.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        # Aplica o som de botao
                        self.play_sound("button_sound")
                        self.paused = False  # Retomar o jogo
                        self.restart = True
                        pygame.mixer.music.stop()
                    elif exit_button.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        # Aplica o som de botao
                        self.play_sound("button_sound")
                        self.running = False
                        pygame.quit()
                        sys.exit()

            # Desenha a tela de pausa
            self.screen.blit(paused_surface, (0, 0))
            self.screen.blit(menu_background, menu_rect.topleft) # Desenha o fundo do menu
            self.screen.blit(title_text, title_rect) # Desenha o título
            
            # Atualiza e desenha os botões
            resume_button.update(pygame.mouse.get_pos())
            restart_button.update(pygame.mouse.get_pos())
            exit_button.update(pygame.mouse.get_pos())
            resume_button.draw(self.screen)
            restart_button.draw(self.screen)
            exit_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
           
    def level_up_menu(self, itens):
        """
        Exibe o menu de level up para o jogador, permitindo a seleção de uma habilidade ou item.

        Args:
        itens (list): Uma lista de três itens ou habilidades que o jogador pode escolher.
        """

        # Congela o jogo e exibe o menu de level up
        paused_surface = self.screen.copy()  # Captura o estado atual do jogo
        self.blur(paused_surface, 180)

        # Configuração dos botões de escolha
        button_width, button_height = 200, 300
        button_spacing = 20  # Espaçamento entre os itens

        # Configuração do título
        title_font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 40)
        title_text = title_font.render("Escolha uma habilidade:", True, pygame.Color('white'))
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, (self.screen.get_height() // 2) - (button_height // 2) - 50))  # Centraliza no topo da tela

        # Define a coordenada Y para todos os itens, mantendo-os na mesma linha
        y_pos = (self.screen.get_height() // 2) - (button_height // 2)   # Ajuste para a posição Y desejada

        # Coordenada X para centralizar os botões na tela
        x_center = self.screen.get_width() // 2

        # Criando os itens, posicionando-os lado a lado
        item2 = SelectionItem(x_center - (button_width / 2), y_pos, button_width, button_height, pygame.Color('black'), itens[1], 24)
        item1 = SelectionItem(item2.rect.left - button_spacing - button_width, y_pos, button_width, button_height, pygame.Color('black'), itens[0], 24)
        item3 = SelectionItem(item2.rect.right + button_spacing, y_pos, button_width, button_height, pygame.Color('black'), itens[2], 24)
        
        self.play_sound("level_up")
        
        # Loop de level up, interrope o jogo até qua uma opção seja selecionada
        while self.level_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Primeiro Item Selecionado
                    if item1.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        # Aplica o som de botao
                        self.play_sound("button_sound")
                        # Evita upar mais de uma vez
                        if self.level_up:
                            self.level_up = False  # Retomar o jogo
                            # Coloca o item selecionado no seu inventario
                            if isinstance(itens[0], Item):
                                self.inventory.add_item(itens[0])
                                # Se o item tiver no maximo remove o item da lista de itens que podem aparecer
                                if itens[0].level == itens[0].max_level:
                                    try:
                                        self.all_itens["attacks"].pop(itens[0].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[0], Ability):
                                self.skills_hub.add_item(itens[0])
                                # Se o item tiver no maximo remove o item da lista de itens que podem aparecer
                                if itens[0].level == itens[0].max_level:
                                    try:
                                        self.all_itens["abilities"].pop(itens[0].kind)
                                    except ValueError:
                                        pass
                            # Se for um consumivel, aplica o consumivel
                            if isinstance(itens[0], Consumible):
                                if itens[0].kind == "Baconseed":
                                    if self.player.health + (self.player.max_health // 2) > self.player.max_health:
                                        self.player.health = self.player.max_health
                                    else:
                                        self.player.health += (self.player.max_health // 2)
                                elif itens[0].kind == "Starpotion":
                                    self.player.xp += 10
                    # Segundo Item Selecionado
                    elif item2.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        # Aplica o som de botao
                        self.play_sound("button_sound")
                        # Evita upar mais de uma vez
                        if self.level_up:
                            self.level_up = False  # Retomar o jogo
                            # Adiciona o item no seu inventário
                            if isinstance(itens[1], Item):
                                self.inventory.add_item(itens[1])
                                # Se o item tiver no maximo remove o item da lista de itens que podem aparecer
                                if itens[1].level == itens[1].max_level:
                                    try:
                                        self.all_itens["attacks"].pop(itens[1].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[1], Ability):
                                self.skills_hub.add_item(itens[1])
                                # Se o item tiver no maximo remove o item da lista de itens que podem aparecer
                                if itens[1].level == itens[1].max_level:
                                    try:
                                        self.all_itens["abilities"].pop(itens[1].kind)
                                    except ValueError:
                                        pass
                            # Se for consumivel, aplica o consumivel
                            if isinstance(itens[1], Consumible):
                                if itens[1].kind == "Baconseed":
                                    if self.player.health + (self.player.max_health // 2) > self.player.max_health:
                                        self.player.health = self.player.max_health
                                    else:
                                        self.player.health += (self.player.max_health // 2)
                                elif itens[1].kind == "Starpotion":
                                    self.player.xp += 10
                    # Terceiro Item Selecionado
                    elif item3.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        # Aplica o som de botao
                        self.play_sound("button_sound")
                        # Evita que upa mais de uma vez
                        if self.level_up:
                            self.level_up = False  # Retomar o jogo
                            # Adiciona o item ao seu inventário
                            if isinstance(itens[2], Item):
                                self.inventory.add_item(itens[2])
                                # Se o item tiver no maximo remove o item da lista de itens que podem aparecer
                                if itens[2].level == itens[2].max_level:
                                    try:
                                        self.all_itens["attacks"].pop(itens[2].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[2], Ability):
                                self.skills_hub.add_item(itens[2])
                                # Se o item tiver no maximo remove o item da lista de itens que podem aparecer
                                if itens[2].level == itens[2].max_level:
                                    try:
                                        self.all_itens["abilities"].pop(itens[2].kind)
                                    except ValueError:
                                        pass
                            # Se for um consumivel, aplica o consumivel
                            if isinstance(itens[2], Consumible):
                                if itens[2].kind == "Baconseed":
                                    if self.player.health + (self.player.max_health // 2) > self.player.max_health:
                                        self.player.health = self.player.max_health
                                    else:
                                        self.player.health += (self.player.max_health // 2)
                                elif itens[2].kind == "Starpotion":
                                    self.player.xp += 10

            # Desenha a tela de pausa
            self.screen.blit(paused_surface, (0, 0))
            self.screen.blit(title_text, title_rect) # Desenha o título
            
            # Atualiza e desenha os botões
            item1.update(pygame.mouse.get_pos())
            item1.draw(self.screen)
            item2.update(pygame.mouse.get_pos())
            item2.draw(self.screen)
            item3.update(pygame.mouse.get_pos())
            item3.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
            
    def spawn_enemies(self):
        """
        Gerencia a criação e adição de inimigos à lista de inimigos no jogo.
        """

        # Enquanto tiver menos que o limite de inimigos
        if len(self.enemies_list) < self.enemy_number:
            if not self.spawning:
                self.spawning = True
                enemies_to_spawn = config.enemy_list[self.phase-1]
                # Escolhe aleatoriamente o inimigo para spawn
                enemy_kind = random.choice(enemies_to_spawn)
                angle = random.uniform(0, 2 * math.pi)
                radius = (self.screen.get_height() ** 2 + self.screen.get_width() ** 2) ** 0.5 / 2
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                
                spawn_pos = pygame.Rect((x + self.player.rect.x + self.player.rect.width / 2), 
                (y + self.player.rect.y + self.player.rect.height / 2), char_size_colision[0], char_size_colision[1])
                
                if not any(spawn_pos.colliderect(rect) for rect in self.blocked_rects):
                    # Spawna o inimigo
                    self.enemies_list.append(Enemy(self,
                                              enemy_kind,
                                              (x + self.player.rect.x + self.player.rect.width / 2), 
                                              (y + self.player.rect.y + self.player.rect.height / 2)))
                    self.enemies_alive += 1
    
                    self.spawn_time = pygame.time.get_ticks()
            # Adiciona um delay entre cada spawn de inimigo
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.spawn_time > config.spawn_delay:
                    self.spawning = False

    def buffs_apply(self):
        """
        Aplica os buffs ativos ao jogador com base no nível de suas habilidades.
        """
        # Altera o valor dos buffs conforme o nível da habilidade
        for ability in self.skills_hub.items:
            self.buffs[ability[0].buff] = config.buff[ability[0].kind][ability[0].level]

    def MessageSpawnBoss(self):
        """
        Exibe uma mensagem de alerta no início do aparecimento de um chefe.
        """
         # Exibir a mensagem no centro superior da tela
        self.message = "Prepare-se"
        self.play_sound("boss_coming")
        self.show_message = True # Faz a messagem aparecer usando a função draw_message que está no loop do jogo
        self.message_time = pygame.time.get_ticks()  # Registra o tempo em que a mensagem foi exibida
        self.message_duration = 3000 # Define o tempo que a menssagem fica na tela

    def draw_message(self):
        """
        Desenha uma mensagem na tela se a variável `show_message` estiver ativada.
        """

        # Se show_message for True, exibe a mensagem
        if self.show_message:
            # Posiciona a menssagem na tela
            font = pygame.font.Font('../assets/fonts/PixelifySans-Regular.ttf', 34)
            text_surface = font.render(self.message, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, 150))  # Centralizado no topo

            # Verificar se o tempo já passou
            if pygame.time.get_ticks() - self.message_time >= self.message_duration:
                self.show_message = False  # Remove a mensagem após o termino do tempo

            # Desenhar a mensagem na tela
            self.screen.blit(text_surface, text_rect)
            
    def cheats(self):
        """
        Aplica cheats no jogo quando teclas específicas são pressionadas.

        Este método verifica se certas combinações de teclas são pressionadas para conceder benefícios ao jogador. 
        Atualmente, existem dois cheats disponíveis:
        
        1. Pressionar 'Q' aumenta a experiência do jogador.
        2. Pressionar 'R' e 'I' simultaneamente restaura a saúde do jogador ao máximo.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_y] and keys[pygame.K_u]:
            self.player.xp += 2100
        if keys[pygame.K_r] and keys[pygame.K_i]:
            self.player.health = self.player.max_health
            
    def items_list_choice(self):
        """
        Seleciona e atualiza a lista de itens disponíveis para o menu de Level Up.

        Este método é responsável por escolher os itens que serão exibidos no menu de Level Up com base na condição do inventário 
        e das habilidades do jogador. Ele também gerencia quais itens devem ser removidos ou atualizados, de acordo com a capacidade máxima
        do inventário e das habilidades.
        """

        # Se o inventario de armas tiver cheio, coloca apenas os itens que já estão no inventário para aparecerem
        if len(self.inventory.items) >= self.inventory.max_slots:
            if self.update_items:
                items = {}
                for item in self.inventory.items:
                    items[item[0].kind] = item[0]
                self.all_itens["attacks"] = items
                self.update_items = False
        # Se o inventario de habilidades tiver cheio, coloca apenas os itens que já estão no inventário para aparecerem        
        if len(self.skills_hub.items) >= self.skills_hub.max_slots:
            if self.update_abilities:
                abilities = {}
                for ability in self.skills_hub.items:
                    abilities[ability[0].kind] = ability[0]
                self.all_itens["abilities"] = abilities
                self.update_abilities = False
        # Se todos os ataques já estão no máximo, remove os ataques dos itens que podem aparecer        
        if "attacks" in self.all_itens_classes:
            if self.all_itens["attacks"] == {}:
                self.all_itens_classes.remove("attacks")
        # Se todos as habilidades já estão no máximo, remove as habilidades dos itens que podem aparecer
        if "abilities" in self.all_itens_classes:
            if self.all_itens["abilities"] == {}:
                self.all_itens_classes.remove("abilities")
        # Se todos itens estiverem no máximo, remove todos itens
        if self.all_itens_classes == []:
            self.itens = {}
            
        # Se tiver itens que não estão no máximo, escolhe itens para aparecerem no menu de Level Up
        if self.itens != {}:
            self.itens = [random.choice(list(self.all_itens[random.choice(self.all_itens_classes)].values())), random.choice(list(self.all_itens[random.choice(self.all_itens_classes)].values())), random.choice(list(self.all_itens[random.choice(self.all_itens_classes)].values()))]
        # Se todos os itens já estiverem no máximo, escolhe itens de nível máximo para aparecerem no menu de Level Up
        else:
            self.itens = [random.choice(list(self.all_itens_max.values())), random.choice(list(self.all_itens_max.values())), random.choice(list(self.all_itens_max.values()))]
           
    def despawn_all_enemies(self):
        """
        Despawn de todos os inimigos presentes na lista de inimigos.
        """
        # Impede o nascimento de inimigos
        self.allow_spawn_enemies = False
        # Remove todos os inimigos
        for enemy in self.enemies_list:
            # try:
            #     self.enemies_list.remove(enemy)
            # except ValueError:
            #     pass
            enemy.kill()
        self.enemies_list = []
        self.enemies_alive = 0
        
    def play_sound(self, sound, checker=True):
        """
        Toca um som específico se o parâmetro `checker` for True.
        """
        # Caso seja validado, toca o som recebido
        if checker:
            self.sounds.all_sounds[sound].play()
           
    def increase_number_of_enemies(self):
        self.enemy_number += 5
