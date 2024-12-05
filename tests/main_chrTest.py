import unittest
import pygame
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import main_character
import config

class MockGame:
    """
    A mock game class to simulate the game environment for testing.
    """
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.collidable_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_attacks = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()
        self.player = None
        
        # Mock sprites repository
        class MockSprites:
            def __init__(self):
                self.warrior_animations = {
                    "walk_animations": {
                        "walk_down_animations": [pygame.Surface((32, 32))],
                        "walk_up_animations": [pygame.Surface((32, 32))],
                        "walk_right_animations": [pygame.Surface((32, 32))],
                        "walk_left_animations": [pygame.Surface((32, 32))]
                    },
                    "hurt_animations": {
                        "hurt_down_animations": [pygame.Surface((32, 32))],
                        "hurt_up_animations": [pygame.Surface((32, 32))],
                        "hurt_right_animations": [pygame.Surface((32, 32))],
                        "hurt_left_animations": [pygame.Surface((32, 32))]
                    },
                    "death_animations": {
                        "death_down_animations": [pygame.Surface((32, 32))],
                        "death_up_animations": [pygame.Surface((32, 32))],
                        "death_right_animations": [pygame.Surface((32, 32))],
                        "death_left_animations": [pygame.Surface((32, 32))]
                    }
                }
                
                self.attack_animations = {
                    "sword": {
                        "attack_sword_animations": [pygame.Surface((32, 32))]
                    }
                }
        
        self.sprites = MockSprites()
        
        # Mock buffs and difficulty
        self.buffs = {
            "speed": 0,
            "life": 0,
            "defense": 0,
            "firing_speed": 0
        }
        self.difficulty_ratio = 1
        
        # Mock methods
        def play_sound(sound, condition):
            pass
        
        def draw(self):
            pass
        
        def game_over(self):
            pass
        
        self.play_sound = play_sound
        self.draw = draw
        self.game_over = game_over

class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()

    def setUp(self):
        """Set up a fresh game environment for each test."""
        self.mock_game = MockGame()
        self.player = main_character.Player(self.mock_game, 0, 0)
        self.mock_game.player = self.player

    def test_player_initialization(self):
        """Test initial player attributes."""
        self.assertEqual(self.player.health, config.max_health["player"])
        self.assertEqual(self.player.max_health, config.max_health["player"])
        self.assertEqual(self.player.level, 1)
        self.assertEqual(self.player.xp, 0)

    def test_player_movement(self):
        """Test player movement mechanics."""
        initial_x = self.player.rect.x
        initial_y = self.player.rect.y

        # Simulate key press for movement (mocking pygame key events)
        keys = pygame.key.get_pressed()
        keys[pygame.K_RIGHT] = True

        self.player.movement()
        
        # Check that the player has moved
        self.assertNotEqual(self.player.rect.x, initial_x)
        self.assertEqual(self.player.rect.y, initial_y)
        self.assertEqual(self.player.facing, "right")

    def test_player_level_calculation(self):
        """Test player level progression calculation."""
        # Test level progression
        level_1_xp = self.player.levels(1)
        level_2_xp = self.player.levels(2)
        
        self.assertTrue(level_2_xp > level_1_xp)
        
        # Simulate leveling up
        self.player.xp = level_1_xp + 1
        self.player.check_xp_level()
        
        self.assertEqual(self.player.level, 2)

    def test_player_low_life_detection(self):
        """Test low life detection mechanism."""
        # Reduce health to trigger low life
        self.player.health = self.player.max_health * 0.1
        self.player.check_low_life()
        
        self.assertTrue(self.player.low_life)

class TestAttack(unittest.TestCase):
    def setUp(self):
        """Set up game and player for attack tests."""
        self.mock_game = MockGame()
        self.player = main_character.Player(self.mock_game, 0, 0)
        self.mock_game.player = self.player

    def test_attack_initialization(self):
        """Test attack initialization and basic attributes."""
        attack = main_character.Attack(
            self.mock_game, 
            self.player.rect.centerx, 
            self.player.rect.centery, 
            "sword", 
            (100, 100), 
            1
        )
        
        self.assertIsNotNone(attack)
        self.assertEqual(attack.item, "sword")
        self.assertEqual(attack.level, 1)

    def test_attack_movement(self):
        """Test attack movement mechanics."""
        attack = main_character.Attack(
            self.mock_game, 
            self.player.rect.centerx, 
            self.player.rect.centery, 
            "sword", 
            (100, 100), 
            1
        )
        
        initial_x = attack.rect.x
        initial_y = attack.rect.y
        
        attack.movement()
        
        self.assertNotEqual(attack.rect.x, initial_x)
        self.assertNotEqual(attack.rect.y, initial_y)

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()