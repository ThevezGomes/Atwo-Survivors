import unittest
from unittest.mock import Mock, MagicMock
import sys
import os
import math

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from enemy_ai import Enemy_AI, Boss_IA
from main_character import Player

class TestEnemyAI(unittest.TestCase):
    def setUp(self):
        self.game_mock = Mock()
        self.player_mock = MagicMock(spec=Player)
        self.player_mock.rect = Mock(x=50, y=50)
        self.game_mock.player = self.player_mock

        self.enemy_mock = Mock()
        self.enemy_mock.game = self.game_mock
        self.enemy_mock.rect = Mock(x=10, y=10)
        self.enemy_mock.fov = 100
        self.enemy_mock.kind = "test_kind"
        self.enemy_mock.speed = 5

        global config
        config = Mock()
        config.enemy_range = {"test_kind": 20, "boss": 40}

        self.ai = Enemy_AI(self.enemy_mock)

    def test_distance_vector(self):
        self.player_mock.rect.x = 40
        self.player_mock.rect.y = 30

        expected_distance = math.sqrt((40 - 10) ** 2 + (30 - 10) ** 2)
        self.assertAlmostEqual(self.ai.distance_vector(self.player_mock), expected_distance)

    def test_get_deltas(self):
        self.player_mock.rect.x = 40
        self.player_mock.rect.y = 30

        delta_x, delta_y = self.ai.get_deltas(self.player_mock)
        self.assertEqual(delta_x, 30)  # 40 - 10
        self.assertEqual(delta_y, 20)  # 30 - 10

    def test_enemy_pursue(self):
        self.player_mock.rect.x = 30
        self.player_mock.rect.y = 30
        self.ai.seach_distance = 100

        x_change, y_change = self.ai.enemy_pursue()
        self.assertNotEqual((x_change, y_change), (0, 0))

    def test_target_detector_in_range(self):
        self.player_mock.rect.x = 30
        self.player_mock.rect.y = 30
        self.ai.seach_distance = 100

        target = self.ai.target_detector()
        self.assertEqual(target, self.player_mock)

    def test_target_detector_out_of_range(self):
        self.player_mock.rect.x = 200
        self.player_mock.rect.y = 200
        self.ai.seach_distance = 100

        target = self.ai.target_detector()
        self.assertIsNone(target)


class TestBossIA(unittest.TestCase):
    def setUp(self):
        self.game_mock = Mock()
        self.player_mock = MagicMock(spec=Player)
        self.player_mock.rect = Mock(x=50, y=50)
        self.game_mock.player = self.player_mock

        self.enemy_mock = Mock()
        self.enemy_mock.game = self.game_mock
        self.enemy_mock.rect = Mock(x=10, y=10)
        self.enemy_mock.fov = 100
        self.enemy_mock.kind = "boss"
        self.enemy_mock.speed = 5

        global config
        config = Mock()
        config.enemy_range = {"test_kind": 20, "boss": 40}

        self.boss_ai = Boss_IA(self.enemy_mock)

    def test_target_detector(self):
        self.player_mock.rect.x = 100
        self.player_mock.rect.y = 100

        target = self.boss_ai.target_detector()
        self.assertEqual(target, self.player_mock)


if __name__ == '__main__':
    unittest.main()