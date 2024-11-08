import pygame as pg
import sys
from pytmx.util_pygame import load_pygame

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)



pg.init()
screen = pg.display.set_mode((1280,720))
tmx_data = load_pygame('../tmx/Mapa_lp_tiro.tmx')
sprite_group = pg.sprite.Group()

#para mostrar os tile sets de chão
for layer in tmx_data.visible_layers:
    if hasattr(layer,'data'):
        for x,y,surf in layer.tiles():
            pos = (x * 32, y * 32)
            Tile(pos = pos,surf = surf, groups= sprite_group)

for obj in tmx_data.objects:
    pos = obj.x, obj.y
    if obj.type in ("Vegetacao","Pedras"):
        Tile(pos = pos, surf = obj.image, groups = sprite_group)
            

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        screen.fill('black')
        sprite_group.draw(screen)
        pg.display.update()
        
