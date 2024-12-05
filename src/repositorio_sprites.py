"""Módulo para armazenar e gerenciar sprites de personagens em um jogo."""

from sprites import *

class Sprites:
    """Classe que armazena os sprites do personagem principal em diferentes estados de animação."""
    def __init__(self):
        """Inicializa uma nova instância da classe `Sprites` e carrega os sprites."""
        # Armazena a localização dos sprites
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
                "walk": {
                    "enemy_skeleton_spritesheet_walk_down": Spritesheet("../assets/enemy_sprites/skeleton/Down/Png/SkeletonWithSwordDownWalk.png"),
                    "enemy_skeleton_spritesheet_walk_up": Spritesheet("../assets/enemy_sprites/skeleton/Up/Png/SkeletonWithSwordUpWalk.png"),
                    "enemy_skeleton_spritesheet_walk_left": Spritesheet("../assets/enemy_sprites/skeleton/Left/Png/SkeletonWithSwordLefttRun.png"),
                    "enemy_skeleton_spritesheet_walk_right": Spritesheet("../assets/enemy_sprites/skeleton/Right/Png/SkeletonWithSwordRightRun.png")
                    },
                "hurt": {
                    "enemy_skeleton_spritesheet_hurt_down": Spritesheet("../assets/enemy_sprites/skeleton/Down/Png/SkeletonWithSwordDownHurt.png"),
                    "enemy_skeleton_spritesheet_hurt_up": Spritesheet("../assets/enemy_sprites/skeleton/Up/Png/SkeletonWithSwordUpHurt.png"),
                    "enemy_skeleton_spritesheet_hurt_left": Spritesheet("../assets/enemy_sprites/skeleton/Left/Png/SkeletonWithSwordLefttHurt.png"),
                    "enemy_skeleton_spritesheet_hurt_right": Spritesheet("../assets/enemy_sprites/skeleton/Right/Png/SkeletonWithSwordRightHurt.png")
                    }
                
                },

            "skeleton_hunter": {
                "enemy_skeleton_hunter_spritesheet": Spritesheet("../assets/enemy_sprites/skeleton_hunter/Down/SkeletonWithBowDownWalk.png"),
                "walk": {
                    "enemy_skeleton_hunter_spritesheet_walk_down": Spritesheet("../assets/enemy_sprites/skeleton_hunter/Down/SkeletonWithBowDownWalk.png"),
                    "enemy_skeleton_hunter_spritesheet_walk_up":   Spritesheet("../assets/enemy_sprites/skeleton_hunter/Up/SkeletonWithBowUpWalk.png"),
                    "enemy_skeleton_hunter_spritesheet_walk_left": Spritesheet("../assets/enemy_sprites/skeleton_hunter/Left/SkeletonWithBowLeftWalk.png"),
                    "enemy_skeleton_hunter_spritesheet_walk_right":Spritesheet("../assets/enemy_sprites/skeleton_hunter/Right/SkeletonWithBowRightWalk.png")
                    },
                "hurt": {
                    "enemy_skeleton_hunter_spritesheet_hurt_down": Spritesheet("../assets/enemy_sprites/skeleton_hunter/Down/SkeletonWithBowDownHurt.png"),
                    "enemy_skeleton_hunter_spritesheet_hurt_up":   Spritesheet("../assets/enemy_sprites/skeleton_hunter/Up/SkeletonWithBowUpHurt.png"),
                    "enemy_skeleton_hunter_spritesheet_hurt_left": Spritesheet("../assets/enemy_sprites/skeleton_hunter/Left/SkeletonWithBowLefttHurt.png"),
                    "enemy_skeleton_hunter_spritesheet_hurt_right":Spritesheet("../assets/enemy_sprites/skeleton_hunter/Right/SkeletonWithBowRightHurt.png")
                    }
                },

            "cultist": {

                "enemy_cultist_spritesheet": Spritesheet("../assets/enemy_sprites/cultist/Down/CultistDownWalk.png"),
                "walk": {
                    "enemy_cultist_spritesheet_walk_down": Spritesheet("../assets/enemy_sprites/cultist/Down/CultistDownWalk.png"),
                    "enemy_cultist_spritesheet_walk_up":   Spritesheet("../assets/enemy_sprites/cultist/Up/CultistUpWalk.png"),
                    "enemy_cultist_spritesheet_walk_left": Spritesheet("../assets/enemy_sprites/cultist/Left/CultistLeftWalk.png"),
                    "enemy_cultist_spritesheet_walk_right":Spritesheet("../assets/enemy_sprites/cultist/Right/CultistRightWalk.png")
                    },
                "hurt": {
                    "enemy_cultist_spritesheet_hurt_down": Spritesheet("../assets/enemy_sprites/cultist/Down/CultistDownHurt.png"),
                    "enemy_cultist_spritesheet_hurt_up":   Spritesheet("../assets/enemy_sprites/cultist/Up/CultistUpHurt.png"),
                    "enemy_cultist_spritesheet_hurt_left": Spritesheet("../assets/enemy_sprites/cultist/Left/CultistLeftHurt.png"),
                    "enemy_cultist_spritesheet_hurt_right":Spritesheet("../assets/enemy_sprites/cultist/Right/CultistRightHurt.png")
                    }
                },

            
            "goblin": {

                "enemy_goblin_spritesheet": Spritesheet("../assets/enemy_sprites/goblin/Down/GoblinDownWalk.png"),
                "walk": {
                    "enemy_goblin_spritesheet_walk_down": Spritesheet("../assets/enemy_sprites/goblin/Down/GoblinDownWalk.png"),
                    "enemy_goblin_spritesheet_walk_up":   Spritesheet("../assets/enemy_sprites/goblin/Up/GoblinUpWalk.png"),
                    "enemy_goblin_spritesheet_walk_left": Spritesheet("../assets/enemy_sprites/goblin/Left/GoblinLeftWalk.png"),
                    "enemy_goblin_spritesheet_walk_right":Spritesheet("../assets/enemy_sprites/goblin/Right/GoblinRightWalk.png")
                    },
                "hurt": {
                    "enemy_goblin_spritesheet_hurt_down": Spritesheet("../assets/enemy_sprites/goblin/Down/GoblinDownHurt.png"),
                    "enemy_goblin_spritesheet_hurt_up":   Spritesheet("../assets/enemy_sprites/goblin/Up/GoblinUpHurt.png"),
                    "enemy_goblin_spritesheet_hurt_left": Spritesheet("../assets/enemy_sprites/goblin/Left/GoblinLeftHurt.png"),
                    "enemy_goblin_spritesheet_hurt_right":Spritesheet("../assets/enemy_sprites/goblin/Right/GoblinRightHurt.png")
                    }
                },


            "skeleton_boss": {
                "enemy_skeleton_boss_spritesheet": Spritesheet("../assets/enemy_sprites/skeleton_boss/Down/Png/AncientSkeletonDownWalk.png"),
                "walk": {
                    "enemy_skeleton_boss_spritesheet_walk_down": Spritesheet("../assets/enemy_sprites/skeleton_boss/Down/Png/AncientSkeletonDownWalk.png"),
                    "enemy_skeleton_boss_spritesheet_walk_up": Spritesheet("../assets/enemy_sprites/skeleton_boss/Up/Png/AncientSkeletonUpWalk.png"),
                    "enemy_skeleton_boss_spritesheet_walk_left": Spritesheet("../assets/enemy_sprites/skeleton_boss/Left/Png/AncientSkeletonLeftWalk.png"),
                    "enemy_skeleton_boss_spritesheet_walk_right": Spritesheet("../assets/enemy_sprites/skeleton_boss/Right/Png/AncientSkeletonRightWalk.png")
                    },
                "hurt": {
                    "enemy_skeleton_boss_spritesheet_hurt_down": Spritesheet("../assets/enemy_sprites/skeleton_boss/Down/Png/AncientSkeletonDownHurt.png"),
                    "enemy_skeleton_boss_spritesheet_hurt_up": Spritesheet("../assets/enemy_sprites/skeleton_boss/Up/Png/AncientSkeletonUpHurt.png"),
                    "enemy_skeleton_boss_spritesheet_hurt_left": Spritesheet("../assets/enemy_sprites/skeleton_boss/Left/Png/AncientSkeletonLeftHurt.png"),
                    "enemy_skeleton_boss_spritesheet_hurt_right": Spritesheet("../assets/enemy_sprites/skeleton_boss/Right/Png/AncientSkeletonRightHurt.png")
                    }
                },
            "envoy_of_the_divine_beast": {
                "boss_envoy_of_the_divine_beast_spritesheet": Spritesheet("../assets/enemy_sprites/envoy_of_the_divine_beast/envoy_of_the_divine_beast.png")
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
                },
            "demon_sword": {
                "attack_spritesheet_demon_sword": Spritesheet("../assets/itens_sprites/DemonSword/DemonSword.png"),
                "icon": "../assets/itens_sprites/DemonSword/DemonSwordIcon.png"
                },
            "shotgun": {
                "attack_spritesheet_shotgun": Spritesheet("../assets\itens_sprites\ShotGun\shotgun.png"),
                "icon": "../assets\itens_sprites\ShotGun\shotgun_icon.png"
                }
            }
        
        self.enemy_attack_sprites = {
            "knife": {
                "attack_spritesheet_knife": Spritesheet("../assets/enemy_sprites/attack_sprites/knife.png")
                },
            "arrows": {
                "attack_spritesheet_arrows": Spritesheet("../assets/enemy_sprites/attack_sprites/Arrows_pack.png")
                },
            "axe": {
                "attack_spritesheet_axe_1": Spritesheet("../assets/enemy_sprites/attack_sprites/axe/Axe_1.png"),
                "attack_spritesheet_axe_2": Spritesheet("../assets/enemy_sprites/attack_sprites/axe/Axe_2.png"),
                "attack_spritesheet_axe_3": Spritesheet("../assets/enemy_sprites/attack_sprites/axe/Axe_3.png"),
                "attack_spritesheet_axe_4": Spritesheet("../assets/enemy_sprites/attack_sprites/axe/Axe_4.png")
                },
            "fire_ball": {
                "attack_spritesheet_fire_ball_1": Spritesheet("../assets/enemy_sprites/attack_sprites/fire_ball/fire_ball_1.png"),
                "attack_spritesheet_fire_ball_2": Spritesheet("../assets/enemy_sprites/attack_sprites/fire_ball/fire_ball_2.png"),
                "attack_spritesheet_fire_ball_3": Spritesheet("../assets/enemy_sprites/attack_sprites/fire_ball/fire_ball_3.png"),
                "attack_spritesheet_fire_ball_4": Spritesheet("../assets/enemy_sprites/attack_sprites/fire_ball/fire_ball_4.png"),
                "attack_spritesheet_fire_ball_5": Spritesheet("../assets/enemy_sprites/attack_sprites/fire_ball/fire_ball_5.png"),
                },
            "sword": {
                "attack_spritesheet_sword": Spritesheet("../assets/enemy_sprites/attack_sprites/sword.png")
                },
            "sword_slash": {
                "attack_spritesheet_sword_slash": Spritesheet("../assets/enemy_sprites/attack_sprites/sword_slash.png")
                },
            "acid": {
                "attack_spritesheet_acid": Spritesheet("../assets/enemy_sprites/attack_sprites/acid.png")
                }
            }
        
        self.abilities_sprites = {
            "nice_boots": "../assets/itens_sprites/Abilities/nice_boots.png",
            "divine_blessing": "../assets/itens_sprites/Abilities/divine_blessing.png",
            "saint_cross": "../assets/itens_sprites/Abilities/saint_cross.png",
            "rage_of_the_gods": "../assets/itens_sprites/Abilities/rage_of_the_gods.png",
            "indestructible_shield": "../assets/itens_sprites/Abilities/indestructible_shield.png",
            "Artemis_aim": "../assets/itens_sprites/Abilities/Artemis_aim.png",
            "Apollo_maestry": "../assets/itens_sprites/Abilities/Apollo_maestry.png" 
            }
        
        self.consumible_sprites = {
            "Baconseed": "../assets/drop_itens_sprites/Pigtree.png",
            "Baconfruit": "../assets/drop_itens_sprites/Bacon.jpg",
            "Starpotion": "../assets/drop_itens_sprites/starpotion.png",
            "Hugepotion": "../assets/drop_itens_sprites/hugepotion.png"
            }
        
        # Armazena as posições dos sprites nas imagens para criar a animação
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
            
            "death_animations": {
                "death_down_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(12, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(60, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(108, 7, 23, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(156, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_down"].get_sprite(204, 7, 22, 32)],
                
                "death_up_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(13, 7, 22, 33),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(61, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(109, 7, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(158, 8, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_up"].get_sprite(206, 8, 22, 32)],
                
                "death_right_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(12, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(61, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(109, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(157, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_right"].get_sprite(205, 9, 22, 32)],
                
                "death_left_animations": [self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(15, 9, 22, 33),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(63, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(111, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(159, 9, 22, 32),
                                         self.warrior_sprites["death"]["warrior_spritesheet_death_left"].get_sprite(207, 9, 22, 32)]
                }
            }
        
        
        self.enemy_animations = {
            "skeleton" : {
                "walk_animations": {
                    "walk_down_animations" : [ self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(  8, 12, 25, 29),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_down"].get_sprite( 55, 11, 25, 29),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(104, 10, 25, 29),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(152, 11, 25, 29),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(198, 11, 25, 29),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_down"].get_sprite(246, 11, 25, 29)],
                    
                    "walk_up_animations" : [ self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_up"].get_sprite( 15, 11, 25, 30),
                                             self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_up"].get_sprite( 63, 11, 24, 30),
                                             self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(111, 10, 23, 30),
                                             self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(159, 11, 25, 30),
                                             self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(208, 11, 24, 30),
                                             self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_up"].get_sprite(256, 11, 24, 30)],
                    
                    "walk_right_animations" : [ self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_right"].get_sprite( 15, 11, 22, 31),
                                                self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_right"].get_sprite( 62, 11, 22, 31),
                                                self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(109, 10, 22, 31),
                                                self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(159, 11, 22, 31),
                                                self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(207, 11, 22, 31),
                                                self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_right"].get_sprite(256, 10, 22, 31)],
                    
                    "walk_left_animations" : [ self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(  8, 11, 29, 30),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_left"].get_sprite( 54, 11, 29, 30),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(102, 10, 29, 30),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(152, 11, 29, 30),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(202, 11, 29, 30),
                                               self.enemy_sprites["skeleton"]["walk"]["enemy_skeleton_spritesheet_walk_left"].get_sprite(250, 10, 29, 30)]
                    },
                "hurt_animations":{
                    "hurt_down_animations" : [ self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_down"].get_sprite(  8, 12, 25, 29),
                                               self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_down"].get_sprite( 56, 10, 25, 29),
                                               self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_down"].get_sprite(103, 9, 25, 29),
                                               self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_down"].get_sprite(151, 8, 25, 29)],
                    
                    "hurt_up_animations" : [ self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_up"].get_sprite( 16, 12, 25, 30),
                                             self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_up"].get_sprite( 63, 10, 24, 30),
                                             self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_up"].get_sprite(112, 9, 23, 30),
                                             self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_up"].get_sprite(159, 8, 25, 30)],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_right"].get_sprite( 16, 12, 22, 31),
                                                self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_right"].get_sprite( 63, 10, 22, 31),
                                                self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_right"].get_sprite(112, 9, 22, 31),
                                                self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_right"].get_sprite(159, 8, 22, 31)],
                    
                    "hurt_left_animations" : [ self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_left"].get_sprite(  9, 12, 29, 30),
                                               self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_left"].get_sprite( 56, 10, 29, 30),
                                               self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_left"].get_sprite(105, 9, 29, 30),
                                               self.enemy_sprites["skeleton"]["hurt"]["enemy_skeleton_spritesheet_hurt_left"].get_sprite(152, 8, 29, 30)]
                    }
                
            },

            "skeleton_hunter" : {
                "walk_animations": {
                    "walk_down_animations" : [  self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_down"].get_sprite( 15, 11, 17, 30),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_down"].get_sprite( 64, 11, 16, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_down"].get_sprite(112, 10, 16, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_down"].get_sprite(159, 11, 17, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_down"].get_sprite(206, 11, 17, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_down"].get_sprite(254, 10, 17, 29)],
                    
                    "walk_up_animations" : [    self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_up"].get_sprite( 16, 11, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_up"].get_sprite( 64, 11, 17, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_up"].get_sprite(112, 10, 17, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_up"].get_sprite(160, 11, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_up"].get_sprite(209, 11, 17, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_up"].get_sprite(257, 10, 17, 29)],
                    
                    "walk_right_animations" : [ self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_right"].get_sprite( 15, 11, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_right"].get_sprite( 61, 11, 22, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_right"].get_sprite(108, 10, 23, 27),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_right"].get_sprite(159, 11, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_right"].get_sprite(209, 11, 15, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_right"].get_sprite(257, 10, 15, 27)],
                    
                    "walk_left_animations" : [  self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_left"].get_sprite( 13, 11, 20, 30),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_left"].get_sprite( 61, 11, 21, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_left"].get_sprite(109, 10, 22, 27),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_left"].get_sprite(157, 10, 20, 30),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_left"].get_sprite(206, 11, 18, 29),
                                                self.enemy_sprites["skeleton_hunter"]["walk"]["enemy_skeleton_hunter_spritesheet_walk_left"].get_sprite(256, 10, 16, 27)]
                    },

                "hurt_animations":{
                    "hurt_down_animations" : [  self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_down"].get_sprite( 15, 11, 17, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_down"].get_sprite( 63,  9, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_down"].get_sprite(111,  8, 17, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_down"].get_sprite(159,  7, 18, 30)],
                    
                    "hurt_up_animations" : [    self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_up"].get_sprite( 16, 11, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_up"].get_sprite( 63,  9, 20, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_up"].get_sprite(112,  8, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_up"].get_sprite(159,  7, 20, 30)],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_right"].get_sprite( 15, 11, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_right"].get_sprite( 61,  9, 21, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_right"].get_sprite(111,  8, 18, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_right"].get_sprite(157,  7, 21, 30)],
                    
                    "hurt_left_animations" : [  self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_left"].get_sprite( 13, 11, 20, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_left"].get_sprite( 60,  9, 22, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_left"].get_sprite(109,  8, 20, 30),
                                                self.enemy_sprites["skeleton_hunter"]["hurt"]["enemy_skeleton_hunter_spritesheet_hurt_left"].get_sprite(156,  7, 22, 30)]
                    }
                
            },

            "cultist" : {
                "walk_animations": {
                    "walk_down_animations" : [  self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite( 17, 10, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite( 65, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite(113, 11, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite(161, 11, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite(209, 10, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite(257, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite(305, 11, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_down"].get_sprite(353, 11, 14, 28)
                                                
                                                ],
                    
                    "walk_up_animations" : [    self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite( 17, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite( 65, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite(113, 11, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite(161, 11, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite(209, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite(257, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite(305, 11, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_up"].get_sprite(353, 11, 14, 28)
                                                ],
                    
                    "walk_right_animations" : [ self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite( 18,  9, 12, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite( 65,  9, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite(113, 10, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite(161, 10, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite(210,  9, 12, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite(258,  9, 12, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite(306, 10, 12, 27),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_right"].get_sprite(354, 10, 12, 27)
                                                ],
                    
                    "walk_left_animations" : [  self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite( 18,  9, 12, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite( 65,  9, 14, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite(113, 10, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite(161, 10, 14, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite(210,  9, 12, 29),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite(258,  9, 12, 28),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite(306, 10, 12, 27),
                                                self.enemy_sprites["cultist"]["walk"]["enemy_cultist_spritesheet_walk_left"].get_sprite(354, 10, 12, 27)
                                                
                                                ]
                    },

                "hurt_animations":{
                    "hurt_down_animations" : [  self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_down"].get_sprite( 17, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_down"].get_sprite( 64,  9, 16, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_down"].get_sprite(112,  8, 16, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_down"].get_sprite(160, 10, 16, 29)],
                    
                    "hurt_up_animations" : [    self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_up"].get_sprite( 17, 10, 14, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_up"].get_sprite( 65,  9, 14, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_up"].get_sprite(113,  8, 14, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_up"].get_sprite(161,  7, 14, 29)],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_right"].get_sprite( 18,  9, 12, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_right"].get_sprite( 65,  8, 14, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_right"].get_sprite(114,  7, 12, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_right"].get_sprite(161,  6, 14, 29)],
                    
                    "hurt_left_animations" : [  self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_left"].get_sprite( 18,  9, 12, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_left"].get_sprite( 65,  8, 14, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_left"].get_sprite(114,  7, 12, 29),
                                                self.enemy_sprites["cultist"]["hurt"]["enemy_cultist_spritesheet_hurt_left"].get_sprite(161,  6, 14, 29)]
                    }
                
            },

            "goblin" : {
                "walk_animations": {
                    "walk_down_animations" : [  self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite( 56, 12, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(105, 12, 31, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(151, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(199, 12, 33, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(248, 12, 31, 28)
                                                ],
                    
                    "walk_up_animations" : [    self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite( 56, 12, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(105, 12, 31, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(151, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(199, 12, 33, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(248, 12, 31, 28)
                                                ],
                    
                    "walk_right_animations" : [ self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite( 15, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite( 64, 12, 24, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(110, 12, 24, 27),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(159, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(205, 12, 31, 29),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(253, 12, 31, 29)
                                                ],
                    
                    "walk_left_animations" : [  self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(  6, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite( 56, 12, 24, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(106, 12, 24, 27),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(150, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(196, 12, 31, 29),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(244, 12, 31, 29)
                                                
                                                ]
                    },

                "hurt_animations":{
                    "hurt_down_animations" : [  self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite( 54, 12, 36, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite(103, 11, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite(150, 11, 36, 28)],
                    
                    "hurt_up_animations" : [    self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite( 54, 12, 36, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite(103, 11, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite(150, 11, 36, 28)],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite( 15, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite( 62, 12, 29, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite(111, 11, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite(158, 10, 29, 28)],
                    
                    "hurt_left_animations" : [  self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite(  6, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite( 53, 12, 29, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite(102, 11, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite(149, 10, 29, 28)]
                    }
                
            },

            "basic" : { # PARA TESTES   
                "walk_animations": {
                    "walk_down_animations" : [  self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite( 56, 12, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(105, 12, 31, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(151, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(199, 12, 33, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_down"].get_sprite(248, 12, 31, 28)
                                                ],
                    
                    "walk_up_animations" : [    self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite( 56, 12, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(105, 12, 31, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(151, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(199, 12, 33, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_up"].get_sprite(248, 12, 31, 28)
                                                ],
                    
                    "walk_right_animations" : [ self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite( 15, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite( 64, 12, 24, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(110, 12, 24, 27),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(159, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(205, 12, 31, 29),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_right"].get_sprite(253, 12, 31, 29)
                                                ],
                    
                    "walk_left_animations" : [  self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(  6, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite( 56, 12, 24, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(106, 12, 24, 27),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(150, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(196, 12, 31, 29),
                                                self.enemy_sprites["goblin"]["walk"]["enemy_goblin_spritesheet_walk_left"].get_sprite(244, 12, 31, 29)
                                                
                                                ]
                    },

                "hurt_animations":{
                    "hurt_down_animations" : [  self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite( 54, 12, 36, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite(103, 11, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_down"].get_sprite(150, 11, 36, 2)],
                    
                    "hurt_up_animations" : [    self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite(  7, 13, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite( 54, 12, 36, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite(103, 11, 34, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_up"].get_sprite(150, 11, 36, 28)],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite( 15, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite( 62, 12, 29, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite(111, 11, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_right"].get_sprite(158, 10, 29, 28)],
                    
                    "hurt_left_animations" : [  self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite(  6, 13, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite( 53, 12, 29, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite(102, 11, 27, 28),
                                                self.enemy_sprites["goblin"]["hurt"]["enemy_goblin_spritesheet_hurt_left"].get_sprite(149, 10, 29, 28)]
                    }
                
            },


            "skeleton_boss" : {
                "walk_animations": {
                    "walk_down_animations" : [ self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite(  20, 8, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite( 102, 9, 33, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite(183, 10, 34, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite(263, 11, 34, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite(340, 8, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite(419, 9, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite(498, 10, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_down"].get_sprite(578, 11, 35, 55, config.size["enemies"]["skeleton_boss"])],
                    
                    "walk_up_animations" : [ self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite( 25, 8, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite( 104, 9, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite(183, 10, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite(263, 11, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite(345, 8, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite(425, 9, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite(505, 10, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_up"].get_sprite(585, 11, 35, 55, config.size["enemies"]["skeleton_boss"])],
                    
                    "walk_right_animations" : [ self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite( 32, 16, 56, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite( 127, 17, 58, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite(222, 18, 61, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite(318, 19, 61, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite(416, 16, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite(513, 17, 57, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite(609, 18, 57, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_right"].get_sprite(705, 19, 57, 57, config.size["enemies"]["skeleton_boss"])],
                    
                    "walk_left_animations" : [ self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite(  9, 11, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite( 103, 17, 58, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite(197, 18, 61, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite(293, 19, 61, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite(393, 16, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite(486, 17, 57, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite(583, 18, 57, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["walk"]["enemy_skeleton_boss_spritesheet_walk_left"].get_sprite(679, 19, 57, 57, config.size["enemies"]["skeleton_boss"])]
                    },
                "hurt_animations":{
                    "hurt_down_animations" : [ self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_down"].get_sprite(  20, 8, 34, 55, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_down"].get_sprite( 105, 3, 32, 58, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_down"].get_sprite(185, 2, 32, 58, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_down"].get_sprite(265, 1, 32, 58, config.size["enemies"]["skeleton_boss"])],
                    
                    "hurt_up_animations" : [ self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_up"].get_sprite( 25, 8, 35, 55, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_up"].get_sprite( 103, 3, 32, 58, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_up"].get_sprite(183, 2, 32, 58, config.size["enemies"]["skeleton_boss"]),
                                             self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_up"].get_sprite(263, 1, 32, 58, config.size["enemies"]["skeleton_boss"])],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_right"].get_sprite( 24, 8, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_right"].get_sprite( 104, 7, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_right"].get_sprite(184, 6, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                                self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_right"].get_sprite(264, 5, 55, 57, config.size["enemies"]["skeleton_boss"])],
                    
                    "hurt_left_animations" : [ self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_left"].get_sprite(  1, 8, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_left"].get_sprite( 81, 7, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_left"].get_sprite(161, 6, 55, 57, config.size["enemies"]["skeleton_boss"]),
                                               self.enemy_sprites["skeleton_boss"]["hurt"]["enemy_skeleton_boss_spritesheet_hurt_left"].get_sprite(241, 5, 55, 57, config.size["enemies"]["skeleton_boss"])]
                    }
                
            },
            "envoy_of_the_divine_beast": {
                "walk_animations": {
                    "walk_down_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  19, 33, 51, 60, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 109, 36, 51, 57, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(199, 33, 51, 60, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  19, 33, 51, 60, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 109, 36, 51, 57, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(199, 33, 51, 60, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2)],
                    
                    "walk_up_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 20, 315, 51, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 113, 315, 45, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(203, 315, 45, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 20, 315, 51, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 113, 315, 45, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(203, 315, 45, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2)],
                    
                    "walk_right_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 3, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 93, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(183, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 3, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 93, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(183, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"])],
                    
                    "walk_left_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  3, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 93, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(183, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  3, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 93, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(183, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"])]
                    },
                "hurt_animations":{
                    "hurt_down_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  829, 33, 51, 60, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 919, 36, 51, 57, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(1009, 33, 51, 60, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2)],
                    
                    "hurt_up_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 830, 315, 51, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 923, 315, 45, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(1013, 315, 45, 69, config.size["enemies"]["envoy_of_the_divine_beast"] * 3/2)],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 813, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 903, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(993, 243, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"])],
                    
                    "hurt_left_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  813, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 903, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(993, 147, 84, 42, config.size["enemies"]["envoy_of_the_divine_beast"])]
                    }
                },
            "cockroach": {
                "walk_animations": {
                    "walk_down_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  289, 33, 51, 60, config.size["enemies"]["cockroach"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 379, 36, 51, 57, config.size["enemies"]["cockroach"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(469, 33, 51, 60, config.size["enemies"]["cockroach"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  289, 33, 51, 60, config.size["enemies"]["cockroach"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 379, 36, 51, 57, config.size["enemies"]["cockroach"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(469, 33, 51, 60, config.size["enemies"]["cockroach"] * 3/2)],
                    
                    "walk_up_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 290, 315, 51, 69, config.size["enemies"]["cockroach"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 383, 315, 45, 69, config.size["enemies"]["cockroach"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(473, 315, 45, 69, config.size["enemies"]["cockroach"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 290, 315, 51, 69, config.size["enemies"]["cockroach"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 383, 315, 45, 69, config.size["enemies"]["cockroach"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(473, 315, 45, 69, config.size["enemies"]["cockroach"] * 3/2)],
                    
                    "walk_right_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 273, 243, 84, 42, config.size["enemies"]["cockroach"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 363, 243, 84, 42, config.size["enemies"]["cockroach"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(453, 243, 84, 42, config.size["enemies"]["cockroach"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 273, 243, 84, 42, config.size["enemies"]["cockroach"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 363, 243, 84, 42, config.size["enemies"]["cockroach"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(453, 243, 84, 42, config.size["enemies"]["cockroach"])],
                    
                    "walk_left_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  273, 147, 84, 42, config.size["enemies"]["cockroach"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 363, 147, 84, 42, config.size["enemies"]["cockroach"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(453, 147, 84, 42, config.size["enemies"]["cockroach"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  273, 147, 84, 42, config.size["enemies"]["cockroach"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 363, 147, 84, 42, config.size["enemies"]["cockroach"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(453, 147, 84, 42, config.size["enemies"]["cockroach"])]
                    },
                "hurt_animations":{
                    "hurt_down_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  829, 33, 51, 60, config.size["enemies"]["cockroach"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 919, 36, 51, 57, config.size["enemies"]["cockroach"] * 3/2),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(1009, 33, 51, 60, config.size["enemies"]["cockroach"] * 3/2)],
                    
                    "hurt_up_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 830, 315, 51, 69, config.size["enemies"]["cockroach"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 923, 315, 45, 69, config.size["enemies"]["cockroach"] * 3/2),
                                             self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(1013, 315, 45, 69, config.size["enemies"]["cockroach"] * 3/2)],
                    
                    "hurt_right_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 813, 243, 84, 42, config.size["enemies"]["cockroach"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 903, 243, 84, 42, config.size["enemies"]["cockroach"]),
                                                self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(993, 243, 84, 42, config.size["enemies"]["cockroach"])],
                    
                    "hurt_left_animations" : [ self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(  813, 147, 84, 42, config.size["enemies"]["cockroach"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite( 903, 147, 84, 42, config.size["enemies"]["cockroach"]),
                                               self.enemy_sprites["envoy_of_the_divine_beast"]["boss_envoy_of_the_divine_beast_spritesheet"].get_sprite(993, 147, 84, 42, config.size["enemies"]["cockroach"])]
                    }
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
                },
            "demon_sword": {
                "demon_sword_animations": [self.attack_sprites["demon_sword"]["attack_spritesheet_demon_sword"].get_sprite(204, 419, 44, 69),
                                           self.attack_sprites["demon_sword"]["attack_spritesheet_demon_sword"].get_sprite(33, 403, 92, 86),
                                           self.attack_sprites["demon_sword"]["attack_spritesheet_demon_sword"].get_sprite(137, 273, 118, 85),
                                           self.attack_sprites["demon_sword"]["attack_spritesheet_demon_sword"].get_sprite(7, 267, 119, 71),
                                           self.attack_sprites["demon_sword"]["attack_spritesheet_demon_sword"].get_sprite(135, 138, 111, 67),
                                           self.attack_sprites["demon_sword"]["attack_spritesheet_demon_sword"].get_sprite(7, 141, 86, 64),
                                           self.attack_sprites["demon_sword"]["attack_spritesheet_demon_sword"].get_sprite(134, 16, 54, 60),]
                },
            "shotgun": {
                "shotgun_animations": [self.attack_sprites["shotgun"]["attack_spritesheet_shotgun"].get_sprite(119, 543, 123, 120),
                                        self.attack_sprites["shotgun"]["attack_spritesheet_shotgun"].get_sprite(110, 378, 142, 148),
                                        self.attack_sprites["shotgun"]["attack_spritesheet_shotgun"].get_sprite(78, 208, 206, 144),
                                        self.attack_sprites["shotgun"]["attack_spritesheet_shotgun"].get_sprite(65, 24, 231, 169),]
                }
            }
        
        self.enemy_attack_animations = {
            "knife": {
                "attack_animations": [self.enemy_attack_sprites["knife"]["attack_spritesheet_knife"].get_sprite(  154, 54, 92, 265, config.size["enemies"]["knife"]),
                                      self.enemy_attack_sprites["knife"]["attack_spritesheet_knife"].get_sprite(  154, 54, 92, 265, config.size["enemies"]["knife"]),
                                      self.enemy_attack_sprites["knife"]["attack_spritesheet_knife"].get_sprite(  154, 54, 92, 265, config.size["enemies"]["knife"]),
                                      self.enemy_attack_sprites["knife"]["attack_spritesheet_knife"].get_sprite(  154, 54, 92, 265, config.size["enemies"]["knife"]),
                                      self.enemy_attack_sprites["knife"]["attack_spritesheet_knife"].get_sprite(  154, 54, 92, 265, config.size["enemies"]["knife"]),
                                      self.enemy_attack_sprites["knife"]["attack_spritesheet_knife"].get_sprite(  154, 54, 92, 265, config.size["enemies"]["knife"])
                                      ]
                },
            "arrow": {
                "attack_animations": [self.enemy_attack_sprites["arrows"]["attack_spritesheet_arrows"].get_sprite(  415, 288, 162, 544, config.size["enemies"]["arrow"]),
                                      self.enemy_attack_sprites["arrows"]["attack_spritesheet_arrows"].get_sprite(  415, 288, 162, 544, config.size["enemies"]["arrow"]),
                                      self.enemy_attack_sprites["arrows"]["attack_spritesheet_arrows"].get_sprite(  415, 288, 162, 544, config.size["enemies"]["arrow"]),
                                      self.enemy_attack_sprites["arrows"]["attack_spritesheet_arrows"].get_sprite(  415, 288, 162, 544, config.size["enemies"]["arrow"]),
                                      self.enemy_attack_sprites["arrows"]["attack_spritesheet_arrows"].get_sprite(  415, 288, 162, 544, config.size["enemies"]["arrow"]),
                                      self.enemy_attack_sprites["arrows"]["attack_spritesheet_arrows"].get_sprite(  415, 288, 162, 544, config.size["enemies"]["arrow"])
                                      ]
                },
            "axe": {
                "attack_animations": [self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_1"].get_sprite(  1, 2, 14, 28, config.size["enemies"]["axe"]),
                                      self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_2"].get_sprite(  2, 1, 28, 14, config.size["enemies"]["axe"]/2),
                                      self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_3"].get_sprite(  1, 2, 14, 28, config.size["enemies"]["axe"]),
                                      self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_4"].get_sprite(  2, 1, 28, 14, config.size["enemies"]["axe"]/2),
                                      self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_1"].get_sprite(  1, 2, 14, 28, config.size["enemies"]["axe"]),
                                      self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_2"].get_sprite(  2, 1, 28, 14, config.size["enemies"]["axe"]/2),
                                      self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_3"].get_sprite(  1, 2, 14, 28, config.size["enemies"]["axe"]),
                                      self.enemy_attack_sprites["axe"]["attack_spritesheet_axe_4"].get_sprite(  2, 1, 28, 14, config.size["enemies"]["axe"]/2),
                                      ]
                },
            "fire_ball": {
                "attack_animations": [self.enemy_attack_sprites["fire_ball"]["attack_spritesheet_fire_ball_1"].get_sprite(  6, 11, 17, 32, config.size["enemies"]["fire_ball"]),
                                      self.enemy_attack_sprites["fire_ball"]["attack_spritesheet_fire_ball_2"].get_sprite(  6, 11, 17, 31, config.size["enemies"]["fire_ball"]),
                                      self.enemy_attack_sprites["fire_ball"]["attack_spritesheet_fire_ball_3"].get_sprite(  6, 11, 17, 35, config.size["enemies"]["fire_ball"]),
                                      self.enemy_attack_sprites["fire_ball"]["attack_spritesheet_fire_ball_4"].get_sprite(  6, 11, 17, 33, config.size["enemies"]["fire_ball"]),
                                      self.enemy_attack_sprites["fire_ball"]["attack_spritesheet_fire_ball_5"].get_sprite(  6, 11, 17, 29, config.size["enemies"]["fire_ball"])
                                      ]
                },
            "sword": {
                "attack_animations": [self.enemy_attack_sprites["sword"]["attack_spritesheet_sword"].get_sprite(  52, 0, 25, 43, config.size["enemies"]["sword"]),
                                      self.enemy_attack_sprites["sword"]["attack_spritesheet_sword"].get_sprite(  52, 0, 25, 43, config.size["enemies"]["sword"]),
                                      self.enemy_attack_sprites["sword"]["attack_spritesheet_sword"].get_sprite(  52, 0, 25, 43, config.size["enemies"]["sword"]),
                                      self.enemy_attack_sprites["sword"]["attack_spritesheet_sword"].get_sprite(  52, 0, 25, 43, config.size["enemies"]["sword"]),
                                      self.enemy_attack_sprites["sword"]["attack_spritesheet_sword"].get_sprite(  52, 0, 25, 43, config.size["enemies"]["sword"]),
                                      self.enemy_attack_sprites["sword"]["attack_spritesheet_sword"].get_sprite(  52, 0, 25, 43, config.size["enemies"]["sword"])
                                      ]
                },
            "sword_slash": {
                "attack_animations": [self.enemy_attack_sprites["sword_slash"]["attack_spritesheet_sword_slash"].get_sprite(  0, 25, 64, 16, config.size["enemies"]["sword_slash"]),
                                      self.enemy_attack_sprites["sword_slash"]["attack_spritesheet_sword_slash"].get_sprite(  66, 12, 60, 9, config.size["enemies"]["sword_slash"]),
                                      self.enemy_attack_sprites["sword_slash"]["attack_spritesheet_sword_slash"].get_sprite(  139, 0, 42, 4, config.size["enemies"]["sword_slash"])
                                      ]
                },
            "acid": {
                "attack_animations": [self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  11, 1, 11, 55, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  45, 1, 9, 55, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  78, 19, 7, 37, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  107, 12, 11, 44, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  139, 8, 14, 48, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  171, 7, 14, 49, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  204, 6, 8, 50, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  233, 6, 11, 50, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  263, 2, 11, 54, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  294, 1, 13, 55, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  327, 1, 14, 55, config.size["enemies"]["acid"]),
                                      self.enemy_attack_sprites["acid"]["attack_spritesheet_acid"].get_sprite(  361, 1, 13, 55, config.size["enemies"]["acid"]),
                                      ]
                }
            }