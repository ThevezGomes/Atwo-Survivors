import pygame
from sprites import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_title = pygame.font.Font('assets/fonts/PixelifySans-Regular.ttf', 54)
        self.font_text = pygame.font.Font('assets/fonts/PixelifySans-Regular.ttf', 32)

        #Imagens da tela inicial
        self.intro_background = pygame.image.load('assets/img/Loginscreen.png').convert()
        target_height = self.screen.get_height()
        scaled_width = int(self.intro_background.get_width() * (target_height / self.intro_background.get_height()))
        self.intro_background = pygame.transform.scale(self.intro_background, (scaled_width, target_height))
        self.character = pygame.image.load('assets/img/Warrior.png').convert_alpha()

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
        
g = Game()
g.intro_screen()
pygame.quit()
sys.exit()
