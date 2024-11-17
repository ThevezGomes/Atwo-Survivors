# Variavel que armazena o tamanho de certos objetos
tilesize = 1

# Variavel que define as camadas dos objetos
layers = {"player_layer": 3,
          "enemy_layer": 2,
          "block_layer": 1}

max_health = {"player": 1000,
              "enemies": {
                  "skeleton": 1000
                  }
              }

damage = {
    "enemies": {
        "skeleton": 10
        },
    "itens": {
        "wave": 10}
    }

# Variavel que define a velocidade do jogador
player_speed = 7

# Variavel que define a velocidade base dos inimigos
enemy_speed = {
    "skeleton" : 4
}

# Campo de visão do inimigo
enemy_fov = 400

# Cor vermelha em rgb
red = (255, 0 , 0)

# Largura do personagem principal
width = 77

# Tamanho do personagem principal
char_size = (width, (width*32)/22)

# Tmanho base para os personagens
size = 77