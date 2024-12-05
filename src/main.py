"""Módulo principal do jogo, que inicializa e executa a aplicação do jogo."""

import pygame
from game import *

# Inicializa uma nova instância do jogo
g = Game()
g.intro_screen()  # Exibe a tela de introdução do jogo

# Executa o loop principal do jogo até que a variável `running` seja False
while g.running:
    g.run()  # Executa o loop principal do jogo
    if g.restart:  # Verifica se o jogo deve ser reiniciado
        pygame.mixer.stop()  # Para a música e efeitos de áudio
        g = Game()  # Cria uma nova instância do jogo
        pygame.time.delay(150)  # Aguarda um curto intervalo para reiniciar
        g.intro_screen()  # Exibe a tela de introdução novamente

# Finaliza o Pygame e sai do programa
pygame.quit()
sys.exit()  