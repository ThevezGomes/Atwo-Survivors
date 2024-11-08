import pygame
from game import *

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.run()
    
pygame.quit()
sys.exit()