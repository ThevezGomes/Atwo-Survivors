import pygame
import unittest
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from main_character import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Mock do objeto game com os atributos necessários
        self.mock_game = Mock()
        self.mock_game.all_sprites = pygame.sprite.Group()
        self.mock_game.collidable_sprites = pygame.sprite.Group()
        self.mock_game.enemies = pygame.sprite.Group()
        self.mock_game.buffs = {"speed": 0, "life": 0, "defense": 0, "firing_speed": 0}
        self.mock_game.sprites = {
            "warrior_animations": {
                "walk_animations": {
                    "walk_down_animations": [Mock(), Mock()],
                    "walk_up_animations": [Mock(), Mock()],
                    "walk_right_animations": [Mock(), Mock()],
                    "walk_left_animations": [Mock(), Mock()],
                },
            },
        }

        self.player = Player(self.mock_game, 5, 5)

    @patch("pygame.key.get_pressed")
    def test_movement(self, mock_get_pressed):
        # Configurar o retorno do mock
        mock_get_pressed.return_value = {
            pygame.K_w: True,
            pygame.K_s: False,
            pygame.K_a: False,
            pygame.K_d: False,
        }

        self.player.movement()

        # Verifica se o jogador se moveu para cima
        self.assertEqual(self.player.y_change, -self.player.speed)
        self.assertEqual(self.player.facing, "up")

    def test_collide_blocks_x(self):
        # Cria um sprite colidível
        block = Mock()
        block.rect = pygame.Rect(100, 100, 50, 50)
        self.mock_game.collidable_sprites.add(block)

        # Simula o movimento para a direita e colisão
        self.player.rect = pygame.Rect(95, 100, 50, 50)
        self.player.x_change = 10
        self.player.collide_blocks("x")

        # Verifica se o movimento foi corrigido
        self.assertEqual(self.player.rect.x, block.rect.left - self.player.rect.width)

    def test_check_xp_level(self):
        # Aumenta o XP do jogador para testar progressão de nível
        self.player.xp = 200  # Mais que o XP necessário para o próximo nível
        self.player.level = 1
        self.player.check_xp_level()

        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.player.xp, 50)  # Resto após subir de nível

    def test_animate(self):
        # Mock de condições de movimento
        self.player.facing = "down"
        self.player.y_change = 1
        self.player.animation_loop = 1
        self.player.animate()

        # Verifica se a animação mudou
        expected_image = self.mock_game.sprites["warrior_animations"]["walk_animations"]["walk_down_animations"][1]
        self.assertEqual(self.player.image, expected_image)

if __name__ == "__main__":
    unittest.main()


"""
def create_key_mock(pressed_keys): #outer

    def mocked_get_pressed(): #inner
        tmp = [0] * 300
        for key in pressed_keys:
            tmp[key] = 1
        return tmp

    return mocked_get_pressed #Essa função simulará a `get_pressed` apenas com
                              #as teclas da lista `pressed_keys`

#Classe com casos de teste
class TestPlayerMovements(unittest.TestCase):

    def test_player_arrows_press(self):
        #criei um objeto simulando um player. Veja a implementação deles para meu
        #jogo no arquivo src/player.py
        player = Player(("Sprites", "Player", "player.png"), (0,0), Inventory(), 10)

        self.assertEqual(player.rect.centerx, 0) #como não foi feito movimento,
        self.assertEqual(player.rect.centery, 0) #a posição deve bater com a
                                                 #passada na inicialização da classe
        player.update((0, 0)) #Essa função verifica as teclas pressionadas. como
                              #nenhuma foi pressionada, a posição não deve mudar
        self.assertEqual(player.rect.centerx, 0)
        self.assertEqual(player.rect.centery, 0)

        #Agora, vou substituir a função `get_pressed` pela artificial.
        mock_function = create_key_mock([pygame.K_w])
        pygame.key.get_pressed = mock_function

        #Essa chamada de update vai agir como se a tecla w estivesse apertada
        player.update((0, 0))
        self.assertEqual(player.rect.centerx, 0)
        self.assertEqual(player.rect.centery, -7) #O player "se moveu"
        player.update((0, 0))
        self.assertEqual(player.rect.centerx, 0)
        self.assertEqual(player.rect.centery, -14)

        #Posso fazer para outras teclas, é só sobrescrever de novo
        mock_function = create_key_mock([pygame.K_a])
        pygame.key.get_pressed = mock_function

        #Agora o player deverá se mover para a esquerda
        player.update((0, 0))
        self.assertEqual(player.rect.centerx, -7)
        self.assertEqual(player.rect.centery, -14) #O player "se moveu"

        player.update((0, 0))
        self.assertEqual(player.rect.centerx, -14)
        self.assertEqual(player.rect.centery, -14) #O player "se moveu"

        #Fazendo para várias teclas
        mock_function = create_key_mock([pygame.K_a, pygame.K_w])
        pygame.key.get_pressed = mock_function

        player.update((0, 0))
        self.assertEqual(player.rect.centerx, -19)
        self.assertEqual(player.rect.centery, -19) #O player "se moveu"

    def test_player_arrows_press_better(self):
        player = Player(("Sprites", "Player", "player.png"), (0,0), Inventory(), 10)
        #claro que você não precisa ficar copiando e colando, e pode fazer algo
        #automatizado.

        keys = ([],
                [pygame.K_w],
                [pygame.K_a],
                [pygame.K_s],
                [pygame.K_d],
                [pygame.K_w, pygame.K_s],
                [pygame.K_a, pygame.K_d],
                [pygame.K_w, pygame.K_a],
                [pygame.K_w, pygame.K_d],
                [pygame.K_s, pygame.K_a],
                [pygame.K_s, pygame.K_d],
        )
        expected_positions = ([0, 0], #As posições esperadas para essa sequência de teclas apertadas
                              [0, -7],
                              [-7, -7],
                              [-7, 0],
                              [0, 0],
                              [0, 0],
                              [0, 0],
                              [-5, -5],
                              [0, -10],
                              [-5, -5],
                              [0, 0]
        )
        for i in range(len(keys)):
            mock_function = create_key_mock(keys[i])
            pygame.key.get_pressed = mock_function
            player.update((0, 0))
            self.assertEqual(player.rect.centerx, expected_positions[i][0])
            self.assertEqual(player.rect.centery, expected_positions[i][1])

#Eu posso criar outros testes que usem os mocks, mas vai ficar muito específico
#para a minha implementação do jogo. Sabendo fazer a função retornar as teclas
#que você quer, você deverá ser capaz de dizer como seu código deveria reagir,
#e fazer o teste para ver se está reagindo de maneira correta.


#Outros mocks que vocês podem querer usar são:
def create_mouse_click_mock(pressed_buttons): #0 é o botão da esquerda, 1 o do meio e 2 o da direita

    def mocked_get_pressed(): #inner
        tmp = [0] * 3
        for key in pressed_buttons:
            tmp[key] = 1
        return tmp

    return mocked_get_pressed

pygame.mouse.get_pressed = create_mouse_click_mock([0])


def create_mouse_pos_mock(mouse_pos):

    def mocked_get_pressed(): #inner
        return mouse_pos

    return mocked_get_pressed

pygame.mouse.get_pos = create_mouse_pos_mock((1, 2))

if __name__ == "__main__":
    pygame.init() #Se não fizer o init o pygame chora
    pygame.display.set_mode((1000, 1000))
    unittest.main()
"""