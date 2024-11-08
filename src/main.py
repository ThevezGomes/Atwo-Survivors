import pygame
from game import *
from sprites import *

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.run()
    
pygame.quit()
sys.exit()