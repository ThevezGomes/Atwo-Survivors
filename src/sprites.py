import pygame

class Button:
    def __init__(self, x, y, width, height, fg, content, fontsize, image_path='assets\img\GenericButton.png', image_path_hover='assets\img\GenericButtonActive.png'):
        # Define a fonte e outras variáveis
        self.font = pygame.font.Font('assets/fonts/PixelifySans-Regular.ttf', fontsize)  # Fonte do texto
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