import pygame as pg
import sys
from pytmx.util_pygame import load_pygame

pg.init()
screen = pg.display.set_mode((1280,720))
tmx_data = load_pygame('../tmx/Mapa_lp_tiro.tmx')
print(dir(tmx_data))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.QUIT()
            sys.exit()

            screen.fill('black')
            pg.display.update()
