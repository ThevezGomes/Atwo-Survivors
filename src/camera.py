import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)  # Define o tamanho da câmera
        self.width = width
        self.height = height

    def apply(self, entity):
        # Move o sprite baseado na posição da câmera
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Centraliza a câmera no jogador
        self.camera.center = target.rect.center

        # Limita os limites da câmera para não ultrapassar o mapa
        self.camera.clamp_ip(pygame.Rect(0, 0, self.width, self.height))


