"""Configurações do jogo"""

# Variavel que armazena o tamanho de certos objetos
tilesize = 1

# Variavel que define as camadas dos objetos
layers = {"player_layer": 3,
          "enemy_layer": 2,
          "block_layer": 1}

# Define a vida maxima das entidades
max_health = {"player": 1000,
              "enemies": {
                  "skeleton": 1000,
                  "skeleton_boss": 10000,
                  "skeleton_hunter": 1000,
                  "cultist": 2500,
                  "goblin": 3000,
                  "envoy_of_the_divine_beast": 10000,
                  "cockroach": 500
                  }
              }

# Define o dano dos objetos
damage = {
    "enemies": {
        "skeleton": 10,
        "skeleton_boss": 30,
        "skeleton_hunter": 10,
        "cultist": 15,
        "goblin": 20,
        "envoy_of_the_divine_beast": 30,
        "cockroach": 10
        },
    "enemies_attack": {
        "knife": 20,
        "arrow": 20,
        "axe": 40,
        "fire_ball": 30,
        "sword": 50,
        "sword_slash": 30,
        "acid": 30
        },
    "itens": {
        "wave": {
            1: 30
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
        "shotgun": {
            1: 50,
            2: 75,
            3: 100,
            4: 200,
            5: 250
            }
        }
    }

# Define os buffs das habilidades por nível
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

# Define o alcance dos itens
itens_speed = {
    "wave": 1,
    "energy_ball": 10,
    "demon_sword": 1,
    "shotgun": 5
    }

# Define a velocidade de animação dos itens
item_animation_speed = {
    "wave": 0.1,
    "energy_ball": 0.1,
    "demon_sword": 0.5,
    "shotgun": 0.6
    }

# Define os delays dos itens
itens_delay = {
    "wave": 550,
    "energy_ball": 550,
    "demon_sword": 550,
    "shotgun": 750
    }

# Variavel que armazena todos os inimigos
enemy_list = [["skeleton",
              "skeleton_hunter"],
              ["cultist",
              "goblin"
              ]]

boss_list = ["skeleton_boss",
             "envoy_of_the_divine_beast"]

boss_name = {
    "skeleton_boss": "Guerreiro morto sem nome",
    "envoy_of_the_divine_beast": "Enviada da Besta Divina"
    }

# Define a velocidade dos inimigos
enemy_speed = {
    "skeleton" : 3,
    "skeleton_boss": 5,
    "skeleton_hunter": 2,
    "cultist": 2,
    "goblin": 4,
    "envoy_of_the_divine_beast": 5,
    "cockroach": 6
}

enemy_animation_speed = {
    "skeleton" : 0.2,
    "skeleton_boss": 0.2,
    "skeleton_hunter": 0.2,
    "cultist": 0.2,
    "goblin": 0.2,
    "envoy_of_the_divine_beast": 0.2,
    "cockroach": 0.2
    }

enemy_damage_animation_speed = {
    "skeleton" : 50,
    "skeleton_boss": 50,
    "skeleton_hunter": 50,
    "cultist": 50,
    "goblin": 50,
    "envoy_of_the_divine_beast": 50,
    "cockroach": 50
    }

# Variavel que define o xp dos inimigos
enemy_xp = {
    "skeleton": 100,
    "skeleton_boss": 1000,
    "skeleton_hunter": 150,
    "cultist": 250,
    "goblin": 300,
    "envoy_of_the_divine_beast": 1000,
    "cockroach": 50
    }


# Distancia minima dos inimigos para perseguir o jogador
enemy_range = {
    "skeleton" : 40,
    "skeleton_boss": 40,
    "cultist": 40,
    "goblin": 40,
    "skeleton_hunter" : 200,
    "envoy_of_the_divine_beast": 40,
    "cockroach": 40
    }

enemy_range_attack = {
    "skeleton" : 200,
    "skeleton_boss": 200,
    "cultist": 40,
    "goblin": 200,
    "skeleton_hunter" : 40,
    "envoy_of_the_divine_beast": 200,
    "cockroach": 40
    }

# Lista de ataques inimigos para cada inimigo
enemies_attack_list = {
    "skeleton": [],
    "skeleton_boss": ["sword", "knife", "sword_slash"],
    "skeleton_hunter": ["arrow"],
    "cultist": ["fire_ball"], # uma possível potion?
    "goblin": ["axe"], # uma possível arma de machado?
    "envoy_of_the_divine_beast": ["acid", "spawn_minions"],
    "cockroach": []
    }

enemies_attack_kind = {
    "knife": "far",
    "arrow": "far",
    "axe": "far",
    "fire_ball": "far",
    "sword": "far",
    "sword_slash": "near",
    "acid": "far",
    "spawn_minions": "spawn"
    }

# Alcance dos ataques inimigos
enemy_attack_speed = {
    "knife": 10,
    "arrow": 10,
    "axe": 10,
    "fire_ball": 10,
    "sword": 10,
    "sword_slash": 3,
    "acid": 10
    }

# Velocidade de animação dos ataques inimigos
enemy_attack_animation_speed = {
    "knife": 0.1,
    "arrow": 0.1,
    "fire_ball": 0.1,
    "axe" : 0.2,
    "sword": 0.1,
    "sword_slash": 0.1,
    "acid": 0.2
    }

# Delay dos ataques inimigos
enemy_attack_delay = {
    "skeleton": 5000,
    "skeleton_boss": 2000,
    "skeleton_hunter": 15000,
    "cultist": 5000,
    "goblin": 5000,
    "envoy_of_the_divine_beast": 2000,
    "cockroach": 5000
    }

minions_list = {
    "envoy_of_the_divine_beast": ["cockroach"]
    }

music_theme = {
    "skeleton_boss": "../assets/sounds/skeleton_boss_theme.mp3",
    "envoy_of_the_divine_beast": "../assets/sounds/main_theme.mp3"
    }

# Cor vermelha em rgb
red = (255, 0 , 0)

# Largura do personagem principal
width = 60

# Tamanho do personagem principal
char_size = (width, (width*32)/22)

# Tamanho do personagem principal
char_size_colision = (200, 200)

# Tmanho base para os personagens
size = {"player": 60,
        "enemies": {
            "skeleton": 60,
            "skeleton_boss": 100,
            "skeleton_hunter": 60,
            "cultist": 60,
            "goblin": 70,
            "knife": 40,
            "arrow": 40,
            "axe": 60,
            "fire_ball": 50,
            "sword": 100,
            "sword_slash": 20,
            "acid": 120,
            "envoy_of_the_divine_beast": 100,
            "cockroach": 40
            }
        }

# Delay de dano
damage_delay = 400

# Delay de spawn de despawn de inimigos
spawn_delay = 400
despawn_delay = 1000

# Limite de inimigos por ataque
enemies_attack_limit = 3