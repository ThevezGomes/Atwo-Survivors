import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Ajusta a posição da entidade com base no deslocamento da câmera
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Calcula o deslocamento da câmera para centralizar no alvo
        x = -target.rect.centerx + pygame.display.get_surface().get_width() // 2
        y = -target.rect.centery + pygame.display.get_surface().get_height() // 2

        # Restringe a câmera aos limites do mapa
        x = max(-(self.width - pygame.display.get_surface().get_width()), min(0, x))
        y = max(-(self.height - pygame.display.get_surface().get_height()), min(0, y))

        self.camera = pygame.Rect(x, y, self.width, self.height)

