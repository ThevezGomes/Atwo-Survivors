import pygame
import sys
from pytmx.util_pygame import load_pygame
from ui import *
from main_character import *
from enemies import *
from sprites import *
from config import *
from props import *
from map import *
import repositorio_sprites as rs

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

        #Criação do inventário (posição, tamanho do slot e número de slots)
        self.inventory = Inventory(x=50, y=self.screen.get_height() - 100, slot_size=50, max_slots=5)
        self.espada = Item("Espada", "Uma espada afiada.", "../assets\img\sword1.png")
        self.inventory.add_item(self.espada)
        self.inventory.add_item(self.espada)
        self.pocao = Item("Poção", "Cura 5 de vida", "../assets/img/staff36.png")
        self.inventory.add_item(self.pocao)
        self.escudo = Item("Escudo", "Um escudo resistente.", "../assets\img\Sorceress Green Skill 07.png")

        #Criação do hub de habilidades (posição, tamanho do slot e número de slots)
        self.skills_hub = Skills_hub(x=10, y=10, slot_size=40, max_slots=5)
        self.resistencia = Ability("Resistencia", "Aumenta 50% na resistencia", "../assets\img\Sorceress Green Skill 07.png")
        self.skills_hub.add_item(self.resistencia)
        self.skills_hub.add_item(self.resistencia)
        self.cura = Ability("Cura", "Cura 5 de vida ada 5s", "../assets\img\Sorceress Icon 10.png")
        self.skills_hub.add_item(self.cura)
        self.vida = Ability("Vida", "Cura 5 de vida ada 5s", "../assets\img\Sorceress Icon 10.png")

        # Barra de experiência
        self.experience_bar = ExperienceBar(max=100, border_color =(40, 34, 31),  background_color=(255, 255, 255, 50), color=(0, 255, 0), width=200, height=25, x=self.screen.get_width() /2 , y=45, level= 3)
        self.experience_bar.amount += 60

        #Timer do jogo
        self.game_timer = TimeGame(x=self.screen.get_width() /2, y=5)
        #self.game_timer.add_event(5, self.itemdrop)
        #self.game_timer.add_event(7, self.morte)

        #Grupo de sprites e colisão
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.collidable_sprites = pygame.sprite.Group()

    #Teste de eventos
    #def itemdrop(self):
    #    self.item1 = self.espada
    #    self.item2 = self.escudo
    #    self.item3 = self.vida

        # Lista de itens
    #    self.itens = [self.item1, self.item2, self.item3]

    #    self.level_up = True

    #def morte(self):
    #    self.health_bar.amount -= 100

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
        
        self.enemy1 = Enemy(self,"skeleton" ,(self.screen.get_width() - config.char_size[0]) // 4, (self.screen.get_height() - config.char_size[1]) // 4)
        
        # Barra de vida
        self.health_bar = HealthBar(max=config.max_health["player"], border_color =(40, 34, 31), background_color=(255, 255, 255, 50), color=(0, 255, 0), width=200, height=25, x=self.screen.get_width() - 210, y=self.screen.get_height() - 35)
        self.health_bar.amount = self.player.health

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.inventory.draw(self.screen) # Adciona o inventario a tela do jogo
        self.skills_hub.draw(self.screen)
        self.health_bar.draw(self.screen) # Adciona a barra de vida na tela
        self.experience_bar.draw(self.screen) # Adciona a barra de experiência na tela
        self.game_timer.update(self.screen) # Adciona o timer ao jogo
        self.clock.tick(60)


        pygame.display.update()

    def update(self):
        #Atualiza todos os sprites e suas propriedades
        self.all_sprites.update()
        self.health_bar.amount = self.player.health

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
                self.inventory.selection_event(event)
            elif pygame.mouse.get_pressed()[0]:
                if self.player.mouse_direction == "up":
                    Attack(self, self.player.rect.x, self.player.rect.y - config.char_size[1], "wave")
                if self.player.mouse_direction == "down":
                    Attack(self, self.player.rect.x, self.player.rect.y + config.char_size[1], "wave")
                if self.player.mouse_direction == "left":
                    Attack(self, self.player.rect.x - config.char_size[0], self.player.rect.y, "wave")
                if self.player.mouse_direction == "right":
                    Attack(self, self.player.rect.x + config.char_size[0], self.player.rect.y, "wave")
               
        if self.level_up == True:
                self.game_timer.pause() 
                self.level_up_menu(self.itens)
                self.game_timer.resume()
        
        if self.player.health <= 0:
            self.draw()
            self.game_over()
            
        self.update()
        self.draw()

        self.clock.tick(60)  # Controle de FPS

    def load_map(self):

        #Coordenadas que devem aparecer no centro da tela
        target_x, target_y = 1250, 1589
    
        #Coordenadas do centro da tela
        screen_center_x, screen_center_y = 460, 454

        #Calcula o deslocamento necessário
        offset_x = target_x - screen_center_x
        offset_y = target_y - screen_center_y


    #Define as propriedades de cada camada do mapa
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * self.tmx_data.tilewidth - offset_x , y * self.tmx_data.tileheight - offset_y )
                    tile = Tile(pos, surf, [self.all_sprites])
                    
                    # Verifica se o Tile é colidível
                    if layer.name == "Colidivel":
                        self.collidable_sprites.add(tile)

        # Adiciona objetos específicos como colidíveis
        for obj in self.tmx_data.objects:
            pos = (obj.x - offset_x , obj.y - offset_y)
            
            if obj.type == 'Poligono':
                if obj.name == 'rect':
                    rect = pygame.Rect(obj.x, obj.y ,obj.width, obj.height)
                    pygame.draw.rect(self.screen, 'yellow', rect)

            if obj.type in ("Vegetacao", "Pedras", "Lapide", "Cerca", "Poligono", "Montanha"):
                if obj.image:
                    tile = Tile(pos, obj.image, [self.all_sprites, self.collidable_sprites])
                    tile.scale(obj.width, obj.height)
                    print(obj.id, tile.rect)
                    self.collidable_sprites.add(tile)  # Garante que esses objetos sejam colidíveis
                else:
                    print(f"Objeto {obj.name} ({obj.type}) em {pos} está sem imagem!")  # Debug

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
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, (self.screen.get_height() // 2) - (button_height // 2) - 30))  # Centraliza no topo da tela

        # Define a coordenada Y para todos os itens, mantendo-os na mesma linha
        y_pos = 250  # Ajuste para a posição Y desejada

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
                        self.level_up = False  # Retomar o jogo
                        if isinstance(itens[0], Item):
                            self.inventory.add_item(itens[0])
                        if isinstance(itens[0], Ability):
                            self.skills_hub.add_item(itens[0])
                    elif item2.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        self.level_up = False  # Retomar o jogo
                        if isinstance(itens[1], Item):
                            self.inventory.add_item(itens[1])
                        if isinstance(itens[1], Ability):
                            self.skills_hub.add_item(itens[1])
                    elif item3.is_pressed(event.pos, pygame.mouse.get_pressed()):
                        self.level_up = False  # Retomar o jogo
                        if isinstance(itens[2], Item):
                            self.inventory.add_item(itens[2])
                        if isinstance(itens[2], Ability):
                            self.skills_hub.add_item(itens[2])

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

