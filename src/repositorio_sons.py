import pygame

class Sound:
    def __init__(self):
        self.all_sounds = {"warrior_hurt_sound": pygame.mixer.Sound("../assets/sounds/warrior_hurt_sound.wav"),
                           "game_over_sound": pygame.mixer.Sound("../assets/sounds/game_over_sound.wav"),
                           "victory_sound": pygame.mixer.Sound("../assets/sounds/victory_sound.wav"),
                           "pig_sound": pygame.mixer.Sound("../assets/sounds/pig_sound.wav"),
                           "eating_sound": pygame.mixer.Sound("../assets/sounds/eating_sound.wav"),
                           "xp_potion_sound": pygame.mixer.Sound("../assets/sounds/xp_potion_sound.wav"),
                           "button_sound": pygame.mixer.Sound("../assets/sounds/button_sound.mp3"),
                           "wave": pygame.mixer.Sound("../assets/sounds/wave_sound.wav"),
                           "demon_sword": pygame.mixer.Sound("../assets/sounds/demon_sword_sound.wav"),
                           "shotgun": pygame.mixer.Sound("../assets/sounds/shotgun_sound.wav"),
                           "energy_ball": pygame.mixer.Sound("../assets/sounds/energy_ball_sound.wav"),
                           "boss_coming": pygame.mixer.Sound("../assets/sounds/boss_coming_sound.wav"),
                           "low_life": pygame.mixer.Sound("../assets/sounds/low_life_sound.wav"),
                           "level_up": pygame.mixer.Sound("../assets/sounds/level_up_sound.wav")
                           }
        
        self.all_sounds["pig_sound"].set_volume(0.2)

