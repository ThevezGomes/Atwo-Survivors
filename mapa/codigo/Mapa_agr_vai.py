import pygame as pg
import sys
from pytmx.util_pygame import load_pygame
import os

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Mapa Tiled com Pygame")

# Constrói o caminho para voltar uma pasta, entrar na pasta 'tmx' e abrir o arquivo .tmx
tmx_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tmx', 'Mapalp.tmx')

# Carrega os dados do mapa
try:
    tmx_data = load_pygame(tmx_path)
except Exception as e:
    print(f"Erro ao carregar o mapa: {e}")
    pg.quit()
    sys.exit()

sprite_group = pg.sprite.Group()

# Para mostrar os tilesets de chão
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * 32, y * 32)
            Tile(pos=pos, surf=surf, groups=sprite_group)

# Para objetos como Vegetação e Pedras
for obj in tmx_data.objects:
    pos = (obj.x, obj.y)
    if obj.type in ("Vegetacao", "Pedras"):
        Tile(pos=pos, surf=obj.image, groups=sprite_group)

clock = pg.time.Clock()

# Loop principal
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)
    pg.display.flip()
    clock.tick(60)  # Limita a 60 FPS

            