import pygame
from game import *

g = Game()
g.intro_screen()
while g.running:
    g.run()
    if g.restart:
        g = Game()
        pygame.time.delay(150)
        g.intro_screen()

pygame.quit()
sys.exit()