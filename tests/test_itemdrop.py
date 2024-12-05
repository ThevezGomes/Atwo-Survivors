import pygame
import unittest
from unittest.mock import patch, Mock
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from drop_item import ItemDrop
from main_character import *  


class TestItemDrop(unittest.TestCase):
    def setUp(self):
        pygame.init()  # Inicializa o pygame para evitar erros de inicialização

    def tearDown(self):
        pygame.quit()  # Encerra o pygame após os testes

    def test_initialization(self):
        """Testa a inicialização do ItemDrop."""
        item = ItemDrop(100, 200, 'Baconseed')

        self.assertEqual(item.item_type, 'Baconseed')
        self.assertEqual(item.rect.center, (100, 200))
        self.assertEqual(item.lifetime, 15000)
        self.assertIsNotNone(item.image)  # Garante que a imagem foi carregada

    @patch("pygame.time.get_ticks", return_value=5000)
    def test_update_transparency(self, mock_ticks):
        """Testa a mudança de transparência no tempo final."""
        item = ItemDrop(100, 200, 'Baconseed')
        item.spawn_time = 3000  # Simula um tempo de criação

        # Simula o update nos últimos 2 segundos
        item.update()
        self.assertEqual(item.image.get_alpha(), 255)  # Sem redução de transparência

        # Tempo dentro dos últimos 2 segundos
        mock_ticks.return_value = 14800
        item.update()
        self.assertLess(item.image.get_alpha(), 255)  # Transparência reduzida

        # Tempo expirado
        mock_ticks.return_value = 16000
        with patch.object(item, "kill") as mock_kill:
            item.update()
            mock_kill.assert_called_once()  # Verifica se o método kill() foi chamado

    def test_apply_effect(self):
        """Testa os efeitos dos itens no jogador."""
        # Mock do jogador
        player = Mock()
        player.health = 50
        player.max_health = 100
        player.xp = 100

        # Testa Baconseed (cura 50% da vida máxima)
        item = ItemDrop(100, 200, 'Baconseed')
        item.apply_effect(player)
        self.assertEqual(player.health, 100)  # Vida não pode ultrapassar o máximo

        # Testa Baconfruit (cura 100% da vida máxima)
        player.health = 50
        item = ItemDrop(100, 200, 'Baconfruit')
        item.apply_effect(player)
        self.assertEqual(player.health, 100)

        # Testa Starpotion (aumenta 40% do XP atual)
        player.xp = 100
        item = ItemDrop(100, 200, 'Starpotion')
        item.apply_effect(player)
        self.assertEqual(player.xp, 140)

        # Testa Hugepotion (aumenta 60% do XP atual)
        player.xp = 100
        item = ItemDrop(100, 200, 'Hugepotion')
        item.apply_effect(player)
        self.assertEqual(player.xp, 160)


if __name__ == "__main__":
    unittest.main()
