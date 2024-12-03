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
import random
import numpy as np
from drop_item import * 

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.level_up = False
        self.restart =False
        self.sprites = rs.Sprites()
        self.spawn_time = 0
        self.spawning = False
        self.spawned_boss = False
        self.show_message = False
        self.enemies_list = []
        
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
        
        self.all_itens_classes = ["attacks", "abilities"]
        self.all_itens = ItemsArmazenamento().itens
        self.all_itens_max = ItemsArmazenamento().itens_player_max
        self.update_items = True
        self.update_abilities = True

        #Criação do inventário (posição, tamanho do slot e número de slots)
        self.inventory = Inventory(x=10, y=self.screen.get_height() - 60, slot_size=50, max_slots=5)
        # self.energy_ball = self.all_itens["energy_ball"]
        # self.inventory.add_item(self.energy_ball)
        # self.inventory.add_item(self.espada)
        # self.pocao = Item("Poção", "Cura 5 de vida", "../assets/img/staff36.png")
        # self.inventory.add_item(self.pocao)
        # self.escudo = Item("Escudo", "Um escudo resistente.", "../assets\img\Sorceress Green Skill 07.png")

        #Criação do hub de habilidades (posição, tamanho do slot e número de slots)
        self.skills_hub = Skills_hub(x=10, y=10, slot_size=40, max_slots=5)
        # self.resistencia = Ability("Resistencia", "Aumenta 50% na resistencia", "../assets\img\Sorceress Green Skill 07.png")
        # self.skills_hub.add_item(self.resistencia)
        # self.skills_hub.add_item(self.resistencia)
        # self.cura = Ability("Cura", "Cura 5 de vida ada 5s", "../assets\img\Sorceress Icon 10.png")
        # self.skills_hub.add_item(self.cura)
        # self.vida = Ability("Vida", "Cura 5 de vida ada 5s", "../assets\img\Sorceress Icon 10.png")

        #Timer do jogo
        self.game_timer = TimeGame(x=self.screen.get_width() /2, y=5)
        self.game_timer.add_event(3, self.MessageSpawnBoss)
        #self.game_timer.add_event(5, self.SpawnBoss)

        #Grupo de sprites 
        self.all_sprites = pygame.sprite.LayeredUpdates()
        #Grupo do sprites do item
        self.item_sprites = pygame.sprite.Group() 
        #Grupo do sprites de colisão
        self.collidable_sprites = pygame.sprite.Group()
        
        self.itens = [random.choice(list(self.all_itens.values())), random.choice(list(self.all_itens.values())), random.choice(list(self.all_itens.values()))]

    #Teste de eventos
    #def SpawnBoss(self):
    #    self.spawned_boss = True

    def new(self):
        self.playing = True

        # Define grupos de sprites com propriedades que serao utilizadas
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        #Carrega os tiles e define colisões com base nas camadas
        self.load_map()

        # Cria o jogador na posicao central da tela
        self.player = Player(self, (self.screen.get_width() - config.char_size[0]) // 2, (self.screen.get_height() - config.char_size[1]) // 2)
        
        # Barra de vida
        self.health_bar = HealthBar(max=self.player.max_health, border_color =(40, 34, 31), background_color=(255, 255, 255, 50), color=(163, 31, 13), base_width=250, height=20, x=self.screen.get_width() - 310, y=self.screen.get_height() - 45, character_icon="../assets/img/WarriorIcon.png")
        self.health_bar.amount = self.player.health
        
        # Barra de experiência
        self.experience_bar = ExperienceBar(border_color =(40, 34, 31),  background_color=(255, 255, 255, 50), color=(0, 255, 0), width=200, height=25, x=self.screen.get_width() /2 , y=45, level=self.player.level, xp=self.player.xp)

        # Barra de vida do Boss
        self.boss_bar = BossBar(max=100, border_color =(40, 34, 31), background_color=(255, 255, 255, 50), color=(138, 11, 10), width=300, height=20, x=self.screen.get_width() /2, y=75, boss_name="Grande Esqueleto")

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
        #Atualiza todos os sprites e suas propriedades
        self.all_sprites.update()
        
        #Atualiza a barra de vida do jogador
        self.health_bar.amount = self.player.health 
        self.health_bar.max = self.player.max_health
        self.experience_bar.level = self.player.level
        self.experience_bar.max = self.experience_bar.levels(self.player.level)
        self.experience_bar.amount = self.player.xp
        self.items_list_choice()
        self.game_timer.update() # Atualisa o timer
        self.spawn_enemies()
        self.cheats()
        
        # Detecta colisão com itens
        collided_items = pygame.sprite.spritecollide(self.player, self.item_sprites, True)
        for item in collided_items:
            # Aplica o efeito do item
            item.apply_effect(self.player)  

    def run(self):
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
                if event.key == pygame.K_e:
                    self.buffs["life"] += 0.2
                    
            elif pygame.mouse.get_pressed()[0]:
                if self.inventory.selected_item_index != None:
                    self.mouse_position = pygame.mouse.get_pos()
                    self.player.atacar(self, self.player.rect.x + self.player.rect.width/2, self.player.rect.y + self.player.rect.height/2, self.inventory.items[self.inventory.selected_item_index][0].kind, self.mouse_position, self.inventory.items[self.inventory.selected_item_index][0].level)
                else:
                    self.mouse_position = pygame.mouse.get_pos()
                    self.player.atacar(self, self.player.rect.x + self.player.rect.width/2, self.player.rect.y + self.player.rect.height/2, "wave", self.mouse_position)
            self.inventory.selection_event(event)

        if self.level_up == True:
                self.game_timer.pause() 
                pygame.time.delay(350)
                self.level_up_menu(self.itens)
                self.game_timer.resume()
        
        if self.player.health <= 0:
            self.player.death = True
        
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
        flipped_horizontally = bool(gid & (1 << 31))  # Verifica o flip horizontal
        flipped_vertically = bool(gid & (1 << 30))    # Verifica o flip vertical
        flipped_diagonally = bool(gid & (1 << 29))    # Verifica o flip diagonal (rotação de 90 graus)

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
                        if layer.name == "Colidivel":
                            self.collidable_sprites.add(tile)

        # Itera pelos objetos do mapa
        for obj in self.tmx_data.objects:
            pos = (obj.x - offset_x, obj.y - offset_y)

            # Objetos com imagens (vegetação, pedras, etc.)
            if obj.type in ("Vegetacao", "Pedras", "Lapide", "Cerca", "Poligono", "Montanha") and obj.image:
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
            if obj.type in ("Vegetacao", "Pedras", "Lapide", "Cerca", "Poligono", "Montanha"):
                # Cria um retângulo bloqueado baseado na posição e dimensões do objeto
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.blocked_rects.append(rect)

    def spawn_item(self):
        #Quantidade de tentativas para o item encontra o local ideal para nascer
        spawn_attempts = 12
        spawn_probability = 0.8
            
        if random.random() > spawn_probability:
            return

        for _ in range(spawn_attempts):
            spawn_x = random.randint(-20, 50)
            spawn_y = random.randint(-20, 50)
            spawn_pos = pygame.Rect(spawn_x, spawn_y, 1, 1)

        #Verifica se a posição gerada não bate com a de um objeto
        if not any(spawn_pos.colliderect(rect) for rect in self.blocked_rects):
            item_type = random.choice(["Baconseed", "Baconfruit", "Starpotion", "Hugepotion"])
            item = ItemDrop(spawn_x, spawn_y, item_type)
            
            #Adciona os itens no grupo de sprites
            self.item_sprites.add(item)
            self.all_sprites.add(item)
            return  

    def intro_screen(self):
        intro = True
        title = self.font_title.render('Jogo da A2', True, pygame.Color('white'))
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
                intro = False
                self.new() # Inicia o jogo
                self.game_timer.start() # Inicia o timer do jogo 
            
            quit_button.update(mouse_pos)
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
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

    def game_over(self):
        over = True

        paused_surface = self.screen.copy()  # Captura o estado atual do jogo
        self.blur(paused_surface, 200)

        # Dimensoes da tela
        screen_width, screen_height = self.screen.get_size()

        title = self.font_title.render('Fim de jogo', True, pygame.Color('white'))
        title_rect = title.get_rect(center=(screen_width // 2, ((screen_height - title.get_height()) // 2) -50))

        # Dimensoes do botão
        button_width, button_height = 200, 75

        # Calcula as posição y para centralizar o botao
        button_y = ((screen_height - button_height) // 2 ) +50 # Ajuste para um pouco abaixo do titulo

        # Cria o botao Play centralizado
        restart_button = Button(screen_width//2 - button_width -10, button_y, button_width, button_height, pygame.Color('white'), 'Resetar', 32)
        quit_button = Button(screen_width//2 +10, button_y, button_width, button_height, pygame.Color('white'), 'Sair', 32)

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
                over = False
                self.restart = True
            
            quit_button.update(mouse_pos)
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
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
        # Aplica  um efeito de blur na tela
        blur_overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        blur_overlay.fill((0, 0, 0, n))  # Opacidade a 180
        surface.blit(blur_overlay, (0, 0))

    def pause_menu(self):
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
        
        # Loop de pausa
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = False  # Retomar o jogo
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        self.paused = False  # Retomar o jogo
                    if restart_button.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        self.paused = False  # Retomar o jogo
                        self.restart = True
                    elif exit_button.is_pressed(event.pos, pygame.mouse.get_pressed()):
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
        
        # Loop de pausa
        while self.level_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if item1.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        if self.level_up:
                            self.level_up = False  # Retomar o jogo
                            # TESTES PARA NIVEL MAXIMO
                            if isinstance(itens[0], Item):
                                self.inventory.add_item(itens[0])
                                if itens[0].level == itens[0].max_level:
                                    try:
                                        self.all_itens["attacks"].pop(itens[0].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[0], Ability):
                                self.skills_hub.add_item(itens[0])
                                if itens[0].level == itens[0].max_level:
                                    try:
                                        self.all_itens["abilities"].pop(itens[0].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[0], Consumible):
                                if itens[0].kind == "Baconseed":
                                    if self.player.health + (self.player.max_health // 2) > self.player.max_health:
                                        self.player.health = self.player.max_health
                                    else:
                                        self.player.health += (self.player.max_health // 2)
                                elif itens[0].kind == "Starpotion":
                                    self.player.xp += 10
                    elif item2.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        if self.level_up:
                            self.level_up = False  # Retomar o jogo
                            if isinstance(itens[1], Item):
                                self.inventory.add_item(itens[1])
                                if itens[1].level == itens[1].max_level:
                                    try:
                                        self.all_itens["attacks"].pop(itens[1].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[1], Ability):
                                self.skills_hub.add_item(itens[1])
                                if itens[1].level == itens[1].max_level:
                                    try:
                                        self.all_itens["abilities"].pop(itens[1].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[1], Consumible):
                                if itens[1].kind == "Baconseed":
                                    if self.player.health + (self.player.max_health // 2) > self.player.max_health:
                                        self.player.health = self.player.max_health
                                    else:
                                        self.player.health += (self.player.max_health // 2)
                                elif itens[1].kind == "Starpotion":
                                    self.player.xp += 10
                    elif item3.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        if self.level_up:
                            self.level_up = False  # Retomar o jogo
                            if isinstance(itens[2], Item):
                                self.inventory.add_item(itens[2])
                                if itens[2].level == itens[2].max_level:
                                    try:
                                        self.all_itens["attacks"].pop(itens[2].kind)
                                    except ValueError:
                                        pass
                            if isinstance(itens[2], Ability):
                                self.skills_hub.add_item(itens[2])
                                if itens[2].level == itens[2].max_level:
                                    try:
                                        self.all_itens["abilities"].pop(itens[2].kind)
                                    except ValueError:
                                        pass
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
        if len(self.enemies_list) <= 20:
            if not self.spawning:
                self.spawning = True
                spawn_attempts = 10

                for _ in range(spawn_attempts):
                    spawn_x = (self.screen.get_width() - config.char_size[0]) * random.random()
                    spawn_y = (self.screen.get_height() - config.char_size[1]) * random.random()
                    
                    # Define um retângulo representando a área do inimigo
                    spawn_pos = pygame.Rect(
                        spawn_x,  # Posição x
                        spawn_y,  # Posição y
                        config.char_size[0],  # Largura do inimigo
                        config.char_size[1]   # Altura do inimigo
                    )


                    if not any(spawn_pos.colliderect(rect) for rect in self.blocked_rects):
                        enemy = Enemy(self, "skeleton", spawn_x, spawn_y)  
                        self.enemies_list.append(enemy)
                        break

                #self.enemies_list.append(Enemy(self,"skeleton" ,(self.screen.get_width() - config.char_size[0]) * random.random(), (self.screen.get_height() - config.char_size[1]) * random.random()))
                
                self.spawn_time = pygame.time.get_ticks()
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.spawn_time > config.spawn_delay:
                    self.spawning = False
                    
                    
    def buffs_apply(self):
        for ability in self.skills_hub.items:
            self.buffs[ability[0].buff] = config.buff[ability[0].kind][ability[0].level]

    def MessageSpawnBoss(self):
         # Exibir a mensagem no centro superior da tela
        self.message = "Prepare-se"
        self.show_message = True # Faz a messagem aparecer usando a função draw_message que está no loop do jogo
        self.message_time = pygame.time.get_ticks()  # Registra o tempo em que a mensagem foi exibida
        self.message_duration = 1000 # Define o tempo que a menssagem fica na tela

    def draw_message(self):
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.player.xp += 2100
        if keys[pygame.K_r] and keys[pygame.K_i]:
            self.player.health = self.player.max_health
            
    def items_list_choice(self):
        if len(self.inventory.items) >= self.inventory.max_slots:
            if self.update_items:
                items = {}
                for item in self.inventory.items:
                    items[item[0].kind] = item[0]
                self.all_itens["attacks"] = items
                self.update_items = False
        if len(self.skills_hub.items) >= self.skills_hub.max_slots:
            if self.update_abilities:
                abilities = {}
                for ability in self.skills_hub.items:
                    abilities[ability[0].kind] = ability[0]
                self.all_itens["abilities"] = abilities
                self.update_abilities = False
        if "attacks" in self.all_itens_classes:
            if self.all_itens["attacks"] == {}:
                self.all_itens_classes.remove("attacks")
        if "abilities" in self.all_itens_classes:
            if self.all_itens["abilities"] == {}:
                self.all_itens_classes.remove("abilities")
        if self.all_itens_classes == []:
            self.itens = {}
        if self.itens != {}:
            self.itens = [random.choice(list(self.all_itens[random.choice(self.all_itens_classes)].values())), random.choice(list(self.all_itens[random.choice(self.all_itens_classes)].values())), random.choice(list(self.all_itens[random.choice(self.all_itens_classes)].values()))]
        else:
            self.itens = [random.choice(list(self.all_itens_max.values())), random.choice(list(self.all_itens_max.values())), random.choice(list(self.all_itens_max.values()))]