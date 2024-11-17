from sprites import *

class Sprites:
    def __init__(self):
        self.warrior_sprites = {
            "walk":{
                "main_character_spritesheet": Spritesheet("../assets/warrior_sprites/Down/Png/WarriorDownWalk.png"),
                "main_character_spritesheet_walk_down": Spritesheet("../assets/warrior_sprites/Down/Png/WarriorDownWalk.png"),
                "main_character_spritesheet_walk_up": Spritesheet("../assets/warrior_sprites/Up/Png/WarriorUpWalk.png"),
                "main_character_spritesheet_walk_left": Spritesheet("../assets/warrior_sprites/Left/Png/WarriorLeftWalk.png"),
                "main_character_spritesheet_walk_right": Spritesheet("../assets/warrior_sprites/Right/Png/WarriorRightWalk.png")
                },
            "hurt":{
                "warrior_spritesheet_hurt_down": Spritesheet("../assets/warrior_sprites/Down/Png/WarriorDownHurt.png"),
                "warrior_spritesheet_hurt_up": Spritesheet("../assets/warrior_sprites/Up/Png/WarriorUpHurt.png"),
                "warrior_spritesheet_hurt_right": Spritesheet("../assets/warrior_sprites/Right/Png/WarriorRightHurt.png"),
                "warrior_spritesheet_hurt_left": Spritesheet("../assets/warrior_sprites/Left/Png/WarriorLeftHurt.png")
                },
            "death":{
                "warrior_spritesheet_death_down": Spritesheet("../assets/warrior_sprites/Down/Png/WarriorDownDeath.png"),
                "warrior_spritesheet_death_up": Spritesheet("../assets/warrior_sprites/Up/Png/WarriorUpDeath.png"),
                "warrior_spritesheet_death_right": Spritesheet("../assets/warrior_sprites/Right/Png/WarriorRightDeath.png"),
                "warrior_spritesheet_death_left": Spritesheet("../assets/warrior_sprites/Left/Png/WarriorLeftDeath.png")
                }
            }
        
        self.enemy_sprites = {
            "skeleton": {
                "enemy_skeleton_spritesheet": Spritesheet("../assets/enemy_sprites/skeleton/Down/Png/SkeletonWithSwordDownWalk.png"),
                "enemy_skeleton_spritesheet_walk_down": Spritesheet("../assets/enemy_sprites/skeleton/Down/Png/SkeletonWithSwordDownWalk.png"),
                "enemy_skeleton_spritesheet_walk_up": Spritesheet("../assets/enemy_sprites/skeleton/Up/Png/SkeletonWithSwordUpWalk.png"),
                "enemy_skeleton_spritesheet_walk_left": Spritesheet("../assets/enemy_sprites/skeleton/Left/Png/SkeletonWithSwordLefttRun.png"),
                "enemy_skeleton_spritesheet_walk_right": Spritesheet("../assets/enemy_sprites/skeleton/Right/Png/SkeletonWithSwordRightRun.png")
                }
            }
        
        self.attack_sprites = {
            "wave": {
                "attack_spritesheet_wave_down": Spritesheet("../assets/itens_sprites/Wave/Small/Down/WaveSmallDown.png"),
                "attack_spritesheet_wave_up": Spritesheet("../assets/itens_sprites/Wave/Small/Up/WaveSmallUp.png"),
                "attack_spritesheet_wave_right": Spritesheet("../assets/itens_sprites/Wave/Small/Right/WaveSmallRight.png"),
                "attack_spritesheet_wave_left": Spritesheet("../assets/itens_sprites/Wave/Small/Left/WaveSmallLeft.png")
                },
            "energy_ball": {
                "attack_spritesheet_energy_ball": Spritesheet("../assets/itens_sprites/EnergyBall/EnergyBall.png"),
                "icon": "../assets/itens_sprites/EnergyBall/orb.png"
                }
            }
        
        self.warrior_animations = {
            "walk_animations": {
                "walk_down_animations": [self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(12, 7, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(61, 7, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(109, 6, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(157, 6, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(204, 7, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(251, 7, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(299, 6, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_down"].get_sprite(347, 6, 22, 32)],
        
                "walk_up_animations": [self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(13, 7, 22, 32),
                                       self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(60, 7, 22, 32),
                                       self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(108, 6, 22, 32),
                                       self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(156, 6, 22, 32),
                                       self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(205, 7, 22, 32),
                                       self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(255, 7, 22, 32),
                                       self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(303, 6, 22, 32),
                                       self.warrior_sprites["walk"]["main_character_spritesheet_walk_up"].get_sprite(351, 6, 22, 32)],
        
                "walk_right_animations": [self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(12, 9, 22, 32),
                                          self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(60, 9, 22, 32),
                                          self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(109, 9, 22, 32),
                                          self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(157, 9, 22, 32),
                                          self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(204, 9, 22, 32),
                                          self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(251, 9, 22, 32),
                                          self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(299, 9, 22, 32),
                                          self.warrior_sprites["walk"]["main_character_spritesheet_walk_right"].get_sprite(347, 9, 22, 32)],
        
                "walk_left_animations": [self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(15, 9, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(64, 9, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(113, 9, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(161, 9, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(207, 9, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(254, 9, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(302, 9, 22, 32),
                                         self.warrior_sprites["walk"]["main_character_spritesheet_walk_left"].get_sprite(350, 9, 22, 32)]
                },
                
            "hurt_animations": {
                "hurt_down_animations": [self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_down"].get_sprite(12, 7, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_down"].get_sprite(60, 4, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_down"].get_sprite(108, 3, 23, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_down"].get_sprite(156, 3, 22, 32)],
                
                "hurt_up_animations": [self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_up"].get_sprite(13, 7, 22, 33),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_up"].get_sprite(61, 5, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_up"].get_sprite(109, 4, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_up"].get_sprite(157, 4, 22, 32)],
                
                "hurt_right_animations": [self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_right"].get_sprite(11, 9, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_right"].get_sprite(59, 8, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_right"].get_sprite(107, 7, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_right"].get_sprite(155, 7, 22, 32)],
                
                "hurt_left_animations": [self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_left"].get_sprite(14, 10, 22, 33),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_left"].get_sprite(62, 8, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_left"].get_sprite(110, 7, 22, 32),
                                         self.warrior_sprites["hurt"]["warrior_spritesheet_hurt_left"].get_sprite(158, 7, 22, 32)]
                
                },
            
            # PRECISA VERIFICAR NO PAINT
            "death_animations": {
                "death_down_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(12, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(60, 4, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(108, 3, 23, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(156, 3, 22, 32)],
                
                "death_up_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(13, 7, 22, 33),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(61, 5, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(109, 4, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(157, 4, 22, 32)],
                
                "death_right_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(11, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(59, 8, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(107, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(155, 7, 22, 32)],
                
                "death_left_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(14, 10, 22, 33),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(62, 8, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(110, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(158, 7, 22, 32)]
                }
            }
        
        
        self.enemy_animations = {
            "skeleton" : {
                "walk_down_animations" : [ self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(  8, 12, 25, 29),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_down"].get_sprite( 55, 11, 25, 29),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(104, 10, 25, 29),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(152, 11, 25, 29),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(198, 11, 25, 29),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(246, 11, 25, 29)],
                
                "walk_up_animations" : [ self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_up"].get_sprite( 15, 11, 25, 30),
                                         self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_up"].get_sprite( 63, 11, 24, 30),
                                         self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(111, 10, 23, 30),
                                         self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(159, 11, 25, 30),
                                         self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(208, 11, 24, 30),
                                         self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(256, 11, 24, 30)],
                
                "walk_right_animations" : [ self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_right"].get_sprite( 15, 11, 22, 31),
                                            self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_right"].get_sprite( 62, 11, 22, 31),
                                            self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(109, 10, 22, 31),
                                            self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(159, 11, 22, 31),
                                            self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(207, 11, 22, 31),
                                            self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(256, 10, 22, 31)],
                
                "walk_left_animations" : [ self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(  8, 11, 29, 30),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_left"].get_sprite( 54, 11, 29, 30),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(102, 10, 29, 30),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(152, 11, 29, 30),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(202, 11, 29, 30),
                                           self.enemy_sprites["skeleton"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(250, 10, 29, 30)]
                
            }
        }
        
        self.attack_animations = {
            "wave": {
                "wave_animations": [self.attack_sprites["wave"]["attack_spritesheet_wave_up"].get_sprite(0, 0, 32, 32),
                                        self.attack_sprites["wave"]["attack_spritesheet_wave_up"].get_sprite(32, 0, 32, 32),
                                        self.attack_sprites["wave"]["attack_spritesheet_wave_up"].get_sprite(64, 0, 32, 32)]
                },
            "energy_ball": {
                "energy_ball_animations": [self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 1054, 36, 86),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 920, 36, 94),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 802, 36, 86),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 666, 36, 94),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 544, 36, 86),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 416, 36, 86),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 288, 36, 86),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 162, 36, 86),
                                           self.attack_sprites["energy_ball"]["attack_spritesheet_energy_ball"].get_sprite(44, 34, 36, 86),
                    ]
                }
            }