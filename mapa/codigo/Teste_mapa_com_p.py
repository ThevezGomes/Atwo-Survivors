import pygame as pg
import sys
from pytmx.util_pygame import load_pygame
import os

""" MAPA """ 
class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, collidable_sprites):
        super().__init__(groups)
        self.image = pg.Surface((32, 32))  
        self.image.fill("blue")  
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.collidable_sprites = collidable_sprites

    def update(self):
        # Captura posição atual para detectar colisão
        original_position = self.rect.topleft

        # Movimenta o player
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed

        # Checa colisão e retorna à posição original se colidir
        if pg.sprite.spritecollide(self, self.collidable_sprites, False):
            self.rect.topleft = original_position

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(screen.get_width() / 2)
        y = -target.rect.centery + int(screen.get_height() / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - screen.get_width()), x)
        y = max(-(self.height - screen.get_height()), y)

        self.camera = pg.Rect(x, y, self.width, self.height)

""" MAPA """
#Tela que vai aparecer
pg.init()
screen = pg.display.set_mode((480, 480))
pg.display.set_caption("Thevez S2")

tmx_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tmx', 'File.tmx')
try:
    tmx_data = load_pygame(tmx_path)
except Exception as e:
    print(f"Erro ao carregar o mapa: {e}")
    pg.quit()
    sys.exit()

sprite_group = pg.sprite.Group()
""" MAPA """
#Colisão
collidable_group = pg.sprite.Group()  # Grupo para objetos com colisão

player = Player(pos=(100, 100), groups=sprite_group, collidable_sprites=collidable_group)
camera = Camera(tmx_data.width * 32, tmx_data.height * 32)

""" MAPA """
# Criação dos tiles do mapa
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * 32, y * 32)
            Tile(pos=pos, surf=surf, groups=sprite_group)

# Criação dos objetos com colisão
for obj in tmx_data.objects:
    pos = (obj.x, obj.y)
    if obj.type in ("Vegetacao", "Pedra", "Lapide"):
        Tile(pos=pos, surf=obj.image, groups=(sprite_group, collidable_group))

clock = pg.time.Clock()

# Loop principal
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Atualiza o jogador e a câmera
    sprite_group.update()
    camera.update(player)

    # Desenha o mapa, objetos e o player
    screen.fill('black')
    for sprite in sprite_group:
        if sprite != player:  
            screen.blit(sprite.image, camera.apply(sprite))
    screen.blit(player.image, camera.apply(player))
    pg.display.flip()
    clock.tick(60)  # Limita a 60 FPS
