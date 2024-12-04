import unittest
from unittest.mock import MagicMock, patch
import pygame
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from enemies import * 


class TestEnemy(unittest.TestCase):

    def setUp(self):
        # Mock do jogo e suas dependências
        self.mock_game = MagicMock()
        self.mock_game.all_sprites = MagicMock()
        self.mock_game.enemies = MagicMock()
        self.mock_game.collidable_sprites = MagicMock()
        self.mock_game.sprites = MagicMock()
        self.mock_game.player = MagicMock()
        self.mock_game.difficulty_ratio = 1.0
        
        # Mock do config
        patcher_config = patch('enemies.config', autospec=True)
        self.mock_config = patcher_config.start()
        self.addCleanup(patcher_config.stop)
        
        self.mock_config.tilesize = 32
        self.mock_config.enemy_fov = {"basic": 100}
        self.mock_config.enemy_speed = {"basic": 2}
        self.mock_config.max_health = {"enemies": {"basic": 10}}
        self.mock_config.enemies_attack_list = {"basic": ["attack1"]}
        self.mock_config.enemy_attack_delay = {"basic": 1000}
        self.mock_config.layers = {"enemy_layer": 1}
        # Mock para simular um Surface do Pygame
        mock_surface = MagicMock()
        mock_surface.get_rect.return_value = MagicMock()  # Simula o retorno de get_rect
        
        # Mock das animações
        
        self.mock_game.sprites.enemy_animations = {
                "basic": {
                    "walk_animations": {
                        "down": [mock_surface],
                        "up": [mock_surface],
                        "right": [mock_surface],
                        "left": [mock_surface],
                    },
                    "hurt_animations": {
                        "up": [mock_surface],
                        "down": [mock_surface],
                        "left": [mock_surface],
                        "right": [mock_surface]
                    }
                }
            }
        
        # Inicializar um inimigo
        self.enemy = Enemy(self.mock_game, "basic", 0, 0)

    def test_enemy_initialization(self):
        """Testa se o inimigo inicializa corretamente."""
        self.assertEqual(self.enemy.kind, "basic")
        self.assertEqual(self.enemy.health, 10)
        self.assertEqual(self.enemy.speed, 2)


    def test_enemy_attack(self):
        """Testa se o inimigo pode atacar."""
        self.enemy.attacking = False
        with patch('enemies.EnemyAttack') as MockAttack:
            self.enemy.atacar(self.mock_game)
            MockAttack.assert_called_once()
            self.assertTrue(self.enemy.attacking)

    def test_enemy_health_check(self):
        """Testa se o inimigo é removido ao perder toda a vida."""
        self.enemy.health = 0
        self.enemy.check_health()
        self.assertTrue(self.enemy not in self.mock_game.enemies_list)
        self.assertTrue(self.enemy not in self.mock_game.all_sprites)


    def test_boss_health_check(self):
        """Testa o comportamento de um Boss ao morrer."""
        boss = Boss(self.mock_game, "basic", 0, 0, "BossName", last_boss=True)
        boss.health = 0
        with patch.object(self.mock_game, "game_over") as mock_game_over:
            boss.check_health()
            mock_game_over.assert_called_once_with("Parabéns, você venceu!")


if __name__ == "__main__":
    unittest.main()