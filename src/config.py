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
                  "skeleton_hunter": 1000
                  }
              }

damage = {
    "enemies": {
        "skeleton": 10,
        "skeleton_boss": 30
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
    "skeleton_hunter": 2
}

enemy_xp = {
    "skeleton": 150,
    "skeleton_boss": 1000,
    "skeleton_hunter": 200
    }

# Campo de visão do inimigo
enemy_fov = 800

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
                  "skeleton_hunter": 60
                  }
              }

damage_delay = 400

spawn_delay = 400
despawn_delay = 1000

enemies_attack_limit = 3