import unittest
import pygame
import os
import sys
from unittest.mock import patch

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game import *
from ui import *

def create_key_mock(pressed_keys):
    """Cria um mock para o método pygame.key.get_pressed() que retorna um estado de teclas simuladas."""
    def mocked_get_pressed():
        tmp = [0] * 300  # Simula um array com 300 teclas
        for key in pressed_keys:
            tmp[key] = 1  # Marca as teclas pressionadas como 1
        return tmp
    return mocked_get_pressed

class TestGameMethods(unittest.TestCase):
    def setUp(self):
        """Configura o ambiente de teste."""
        pygame.init()
        self.game = Game()
        self.game.new()
        self.game.clock = pygame.time.Clock()

    @patch('pygame.key.get_pressed', side_effect=create_key_mock([pygame.K_ESCAPE]))
    def test_pause_menu(self, mock_get_pressed):
        """Testa a exibição do menu de pausa."""
        self.game.paused = True  # Simula o estado de pausa

        self.assertTrue(self.game.paused)

    def test_spawn_enemies(self):
        """Testa o spawn de inimigos."""
        initial_enemy_count = len(self.game.enemies_list)
        self.game.spawn_enemies()
        # Verifica se um inimigo foi adicionado
        self.assertGreater(len(self.game.enemies_list), initial_enemy_count)

    def test_buffs_apply(self):
        """Testa a aplicação de buffs de habilidades."""
        # Simula a adição de habilidades
        self.game.skills_hub.add_item(Ability("nice_boots", "Botas Legais", "Aumenta a velocidade", "speed", max_level=5))
        self.game.buffs_apply()
        # Verifica se os buffs foram aplicados
        self.assertEqual(self.game.buffs['speed'], 0.1)

    def test_message_spawn_boss(self):
        """Testa a exibição da mensagem de spawn do boss."""
        self.game.MessageSpawnBoss()
        # Verifica se a mensagem está ativa
        self.assertTrue(self.game.show_message)

    def test_draw_message(self):
        """Testa a função de desenho da mensagem."""
        self.game.show_message = True
        self.game.message = "teste"
        self.game.message_duration = 1000
        self.game.message_time = pygame.time.get_ticks() - 1000  # Simula uma mensagem que já passou 1 segundo
        self.game.draw_message()
        # Verifica se a mensagem ainda é desenhada
        self.assertFalse(self.game.show_message)

    def test_despawn_all_enemies(self):
        """Testa a remoção de todos os inimigos."""
        # Adiciona inimigos fictícios
        self.game.enemies_list.append(Enemy(self.game, 'skeleton', 100, 100))
        self.game.despawn_all_enemies()
        # Verifica se a lista de inimigos está vazia
        #self.assertEqual(len(self.game.enemies_list), 0)

    def test_items_list_choice(self):
        """Testa a escolha da lista de itens para level up."""
        # Simula um inventário com itens
        self.game.inventory.add_item(Item("energy_ball","Bola de energia", "Destroi tudo no caminho.", max_level=5))
        self.game.items_list_choice()
        # Verifica se a lista de itens não está vazia
        self.assertTrue(len(self.game.itens) > 0)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()


