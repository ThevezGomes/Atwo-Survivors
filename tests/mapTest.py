import pygame
import unittest
from unittest.mock import patch, Mock
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from map import Tile  


class TestTile(unittest.TestCase):
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        pg.init()
        self.surface = pg.Surface((32, 32))  # Criando uma superfície para testes
        self.groups = []
        self.tile = Tile((0, 0), self.surface, self.groups)

    def tearDown(self):
        """
        Finalização após os testes.
        """
        pg.quit()

    def test_initialization(self):
        """
        Testa se a inicialização do Tile é feita corretamente.
        """
        self.assertEqual(self.tile.rect.topleft, (0, 0))
        self.assertEqual(self.tile.image, self.surface)
        self.assertIn(self.tile, self.groups)

    def test_scale(self):
        """
        Testa se a escala do tile é aplicada corretamente.
        """
        self.tile.scale(64, 64)
        self.assertEqual(self.tile.image.get_size(), (64, 64))
        self.assertEqual(self.tile.rect.size, (64, 64))

if __name__ == '__main__':
    unittest.main()
