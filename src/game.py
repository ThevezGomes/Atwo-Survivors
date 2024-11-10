import pygame
from ui import *
from main_character import *
from sprites import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        
        self.main_character_spritesheet = Spritesheet("../assets/warrior_sprites/Down/Png/WarriorDownWalk.png")
        
        self.main_character_spritesheet_walk_down = Spritesheet("../assets/warrior_sprites/Down/Png/WarriorDownWalk.png")
        self.main_character_spritesheet_walk_up = Spritesheet("../assets/warrior_sprites/Up/Png/WarriorUpWalk.png")
        self.main_character_spritesheet_walk_left = Spritesheet("../assets/warrior_sprites/Left/Png/WarriorLeftWalk.png")
        self.main_character_spritesheet_walk_right = Spritesheet("../assets/warrior_sprites/Right/Png/WarriorRightWalk.png")

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
        self.inventory.add_item("Espada", "../assets\img\sword1.png")
        self.inventory.add_item("Espada", "../assets\img\sword1.png")
        self.inventory.add_item("Poção", "../assets/img/staff36.png")

        #Criação do hub de habilidades (posição, tamanho do slot e número de slots)
        self.skills_hub = Skills_hub(x=10, y=10, slot_size=40, max_slots=5)
        self.skills_hub.add_item("Resistencia", "../assets\img\Sorceress Green Skill 07.png")
        self.skills_hub.add_item("Resistencia", "../assets\img\Sorceress Green Skill 07.png")
        self.skills_hub.add_item("Cura", "../assets\img\Sorceress Icon 10.png")

        # Barra de vida
        self.health_bar = HealthBar(max=100, border_color =(40, 34, 31), background_color=(255, 255, 255, 50), color=(0, 255, 0), width=200, height=25, x=self.screen.get_width() - 210, y=self.screen.get_height() - 35)
        self.health_bar.amount -= 25  # Exemplo de perda de vida

        # Barra de experiência
        self.experience_bar = ExperienceBar(max=100, border_color =(40, 34, 31),  background_color=(255, 255, 255, 50), color=(0, 255, 0), width=200, height=25, x=self.screen.get_width() /2 , y=45, level= 3)
        self.experience_bar.amount += 60

        #Timer do jogo
        self.game_timer = TimeGame(x=self.screen.get_width() /2, y=5)
        #self.game_timer.add_event(5, self.spawn_boss)

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        
        self.player = Player(self, (self.screen.get_width() - config.size[0]) // 2, (self.screen.get_height() - config.size[1]) // 2) 

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
        self.all_sprites.update()

    def run(self):
        while self.running:
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
                
            self.update()
            self.draw()
            self.clock.tick(60)  # Controle de FPS

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

    def blur(self, surface):
        # Aplica  um efeito de blur na tela
        blur_overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        blur_overlay.fill((0, 0, 0, 180))  # Opacidade a 180
        surface.blit(blur_overlay, (0, 0))

    def pause_menu(self):
        # Congela o jogo e exibe o menu de pausa
        paused_surface = self.screen.copy()  # Captura o estado atual do jogo
        self.blur(paused_surface)
        
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
        
        resume_button = Button(menu_rect.centerx - button_width // 2, menu_rect.top + 150, button_width, button_height, pygame.Color('white'), 'Retomar', 24)
        exit_button = Button(menu_rect.centerx - button_width // 2, resume_button.rect.bottom + button_spacing, button_width, button_height, pygame.Color('white'), 'Sair', 24)
        
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
            exit_button.update(pygame.mouse.get_pos())
            resume_button.draw(self.screen)
            exit_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
           