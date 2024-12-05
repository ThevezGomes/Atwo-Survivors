# Jogo da A2: Atwo Survivors

## Visão Geral do Projeto
Neste trabalho foi elaborado um jogo de aventura, ação e RPG, utilizando a linguagem Python e a biblioteca Pygame. Nomeado "Atwo Survivors", foi inspirado no conceito de Vampire Survivors, a partir do qual recebeu suas modificações na mecânica de jogo e funcionalidades. 

## Controles do jogo
Utilize as teclas `A`, `W`, `S` e `D` para locomover o personagem na tela, ou os direcionais.
Utilize o botão esquerdo do mouse para realizar ataques, ajustando a posição do mouse na direção do ataque.
O scroll do mouse ou as teclas numéricas superiores podem ser utilizadas para alternar entre itens do inventário.
A tecla `ESC` pausa o jogo.


## Estrutura do Projeto

### 1. **Diretório Raiz**
- **`.gitignore`**: Especifica arquivos e diretórios a serem ignorados pelo Git.
- **`README.md`**: Este documento, que fornece uma visão geral do projeto.
- **`requirements.txt`**: Contém as dependências do Python necessárias para rodar o projeto.

### 2. **`assets/`**
Contém todos os recursos visuais e de áudio usados no jogo.
- **`drop_itens_sprites/`**: Imagens de sprites para vários itens do jogo (ex.: poções, árvores, etc.).
- **`enemy_sprites/`**: Folhas de sprites para vários inimigos, incluindo animações de diferentes movimentos e ataques.
- **`fonts/`**: Arquivos de fonte usados para renderização de texto no jogo.
- **`img/`**: Recursos gerais de IU, como botões, planos de fundo e ícones.
- **`itens_sprites/`**: Imagens de sprites de itens, incluindo habilidades, armas e outros objetos.
- **`sounds/`**: Arquivos de áudio para sons do jogo, incluindo música de fundo e efeitos sonoros.
- **`Tiled/`**: Recursos relacionados ao editor de mapas Tiled, incluindo conjuntos de tiles, camadas de mapa e objetos.
- **`warrior_sprites/`**: Folhas de sprites para o personagem principal (guerreiro), com animações para diferentes direções (cima, baixo, esquerda, direita).

### 3. **`docs/`**
Contém documentação e anotações relacionadas ao projeto.

- **`relatorio/`**: Pasta contendo relatório.
  - **`Rel_A2_LP_2024.pdf`**: Relatório detalhado sobre a etapa A2 do projeto de 2024.
  - **`main.tex`**: Arquivo fonte em LaTeX para a criação do relatório principal.

### 4. **`src/`**
O código fonte principal do jogo.

- **`main.py`**: Inicia o loop principal do jogo.
- **`config.py`**: Configurações do jogo (ex.: parâmetros do jogo).
- **`drop_item.py`**: Lógica relacionada à drop de itens.
- **`enemies.py`**: Definições e propriedades das classes de inimigos.
- **`enemy_ai.py`**: Inteligência artificial dos inimigos.
- **`game.py`**: Lógica principal do jogo e inicialização.
- **`items_abilities.py`**: Gerenciamento de itens e habilidades do jogo.
- **`main_character.py`**: Código para o personagem do jogador (ex.: movimento, interações).
- **`map.py`**: Gerenciamento de mapas e tiles.
- **`props.py`**: Manipulação de objetos interativos no ambiente do jogo.
- **`repositorio_sons.py`**: Gerenciamento de recursos de áudio e reprodução de sons.
- **`repositorio_sprites.py`**: Carregamento e gerenciamento de recursos de sprite.
- **`sprites.py`**: Manipulação e renderização de sprites.
- **`ui.py`**: Componentes da interface do usuário e renderização.

### 5. **`tests/`**
Contém scripts de teste para garantir a funcionalidade do código.
- **`gameTest.py`**: Testes unitários para a lógica principal do jogo.
- **`main_chrTest.py`**: Testes para as funcionalidades do personagem do jogador.
- **`mapTest.py`**: Testes relacionados aos elementos e escalas do mapa
- **`UITest.py`**: Testes relacionados aos elementos da interface do usuário.
- **`enemiesTest.py`**: Testes relacionados aos inimigos do jogo.
- **`enemy_aiTeste.py`**: Testes relacionados à inteligência artifical de movimentação dos inimigos.


## Instruções de Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/HenryGasparelo/A2-LP-2024.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd A2-LP-2024
   ```
3. Instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o jogo:
   ```bash
   python src/main.py
   ```

## Captura de Tela
<div style="text-align: center;">
  <img src="assets\img\tela-jogo.jpeg" alt="Captura de Tela do jogo" width="900"/>
</div> 
