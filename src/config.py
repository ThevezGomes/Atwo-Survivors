# Variavel que armazena o tamanho de certos objetos
tilesize = 1

# Variavel que define as camadas dos objetos
layers = {"player_layer": 3,
          "enemy_layer": 2,
          "block_layer": 1}

max_health = {"player": 1000,
              "enemies": {
                  "skeleton": 1000,
                  "skeleton_boss": 10000,
                  "skeleton_hunter": 1000,
                  "cultist": 2000,
                  "goblin": 1500,
                  }
              }

damage = {
    "enemies": {
        "skeleton": 10,
        "skeleton_boss": 30,
        "skeleton_hunter": 10,
        "cultist": 15,
        "goblin": 20,
        },
    "enemies_attack": {
        "knife": 20
        },
    "itens": {
        "wave": {
            1: 10
            },
        "energy_ball": {
            1: 30,
            2: 50,
            3: 100,
            4: 150,
            5: 200
            },
        "demon_sword": {
            1: 30,
            2: 50,
            3: 100,
            4: 150,
            5: 200
            },
        "shot_gun": {
            1: 50,
            2: 75,
            3: 100,
            4: 200,
            5: 250
            }
        }
    }

buff = {
        "nice_boots": {
            1: 0.1 ,
            2: 0.2 ,
            3: 0.25 ,
            4: 0.3 ,
            5: 0.4 },
        "divine_blessing": {
            1: 0.1 ,
            2: 0.2 ,
            3: 0.3 ,
            4: 0.4 ,
            5: 0.5 },
        "saint_cross": {
            1: 0.1 ,
            2: 0.2 ,
            3: 0.3 ,
            4: 0.4,
            5: 0.5},
        "rage_of_the_gods": {
            1: 0.1,
            2: 0.2,
            3: 0.3,
            4: 0.4,
            5: 0.5},
        "indestructible_shield": {
            1: 0.1,
            2: 0.2,
            3: 0.3,
            4: 0.4,
            5: 0.5},
        "Artemis_aim": {
            1: 0.1,
            2: 0.2,
            3: 0.3,
            4: 0.4,
            5: 0.5},
        "Apollo_maestry": {
            1: 0.1,
            2: 0.2,
            3: 0.3,
            4: 0.4,
            5: 0.5}
        
        }

# Variavel que define a velocidade do jogador
player_speed = 9

itens_speed = {
    "wave": 1,
    "energy_ball": 10,
    "demon_sword": 1,
    "shot_gun": 5
    }

item_animation_speed = {
    "wave": 0.1,
    "energy_ball": 0.1,
    "demon_sword": 0.5,
    "shot_gun": 0.6
    }

itens_delay = {
    "wave": 550,
    "energy_ball": 550,
    "demon_sword": 550,
    "shot_gun": 750
    }

# Variavel que define a velocidade base dos inimigos
enemy_speed = {
    "skeleton" : 3,
    "skeleton_boss": 5,
    "skeleton_hunter": 2,
    "cultist": 2,
    "goblin": 4,
}

enemy_xp = {
    "skeleton": 150,
    "skeleton_boss": 1000,
    "skeleton_hunter": 200,
    "cultist": 250,
    "goblin": 250,
    }

# Campo de visão do inimigo
enemy_fov = {
    "skeleton" : 800,
    "skeleton_boss": 800,
    "skeleton_hunter" : 1000,
    "cultist": 900,
    "goblin": 400
}

enemies_attack_list = {
    "skeleton": [],
    "skeleton_boss": [],
    "skeleton_hunter": ["knife"],
    "cultist": [], # uma possível potion?
    "goblin": [], # uma possível arma de machado?
    }

enemy_attack_speed = {
    "knife": 10,
    "potion" : 10,
    "axe" : 10
    }

enemy_attack_animation_speed = {
    "knife": 0.1,
    "potion": 0.1,
    "axe" : 0.1
    }

enemy_attack_delay = {
    "skeleton": 5000,
    "skeleton_boss": 550,
    "skeleton_hunter": 15000,
    "cultist": 5000,
    "goblin": 5000,
    }

# Cor vermelha em rgb
red = (255, 0 , 0)

# Largura do personagem principal
width = 60

# Tamanho do personagem principal
char_size = (width, (width*32)/22)

# Tmanho base para os personagens
size = {"player": 60,
        "enemies": {
            "skeleton": 60,
            "skeleton_boss": 100,
            "skeleton_hunter": 60,
            "cultist": 60,
            "goblin": 70,
            "knife": 30
            }
        }

damage_delay = 400

spawn_delay = 400
despawn_delay = 1000

enemies_attack_limit = 3