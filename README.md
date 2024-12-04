# Jogo da A2

## Visão Geral do Projeto
Este projeto de jogo é uma estrutura abrangente para o desenvolvimento de um jogo 2D. Inclui recursos, base de código e materiais organizados para facilitar o desenvolvimento, testes e expansão do jogo.

## Estrutura do Projeto

### 1. **Diretório Raiz**
- **`.gitignore`**: Especifica arquivos e diretórios a serem ignorados pelo Git.
- **`README.md`**: Este documento, que fornece uma visão geral do projeto.
- **`requirements.txt`**: Contém as dependências do Python necessárias para rodar o projeto.

### 2. **`assets/`**
Contém todos os recursos visuais e de áudio usados no jogo.
- **`drop_itens_sprites/`**: Imagens de sprites para vários itens colecionáveis do jogo (ex.: poções, árvores, etc.).
- **`enemy_sprites/`**: Folhas de sprites para vários inimigos, incluindo animações de diferentes movimentos e ataques.
- **`fonts/`**: Arquivos de fonte usados para renderização de texto no jogo.
- **`img/`**: Recursos gerais de IU, como botões, planos de fundo e ícones.
- **`itens_sprites/`**: Imagens de sprites de itens, incluindo habilidades, armas e outros objetos.
- **`sounds/`**: Arquivos de áudio para sons do jogo, incluindo música de fundo e efeitos sonoros.
- **`Tiled/`**: Recursos relacionados ao editor de mapas Tiled, incluindo conjuntos de tiles, camadas de mapa e objetos.
- **`warrior_sprites/`**: Folhas de sprites para o personagem principal (guerreiro), com animações para diferentes direções (cima, baixo, esquerda, direita).

### 3. **`docs/`**
Contém documentação e anotações relacionadas ao projeto.
- **`none.txt`**: Espaço reservado ou arquivo vazio para fins de documentação.

### 4. **`src/`**
O código fonte principal do jogo.
- **`config.py`**: Configurações do jogo (ex.: tamanho da janela, parâmetros do jogo).
- **`drop_item.py`**: Código relacionado à lógica de queda de itens.
- **`enemies.py`**: Definições e propriedades das classes de inimigos.
- **`enemy_ai.py`**: Lógica para a inteligência artificial dos inimigos.
- **`game.py`**: Lógica principal do jogo e código de inicialização.
- **`items_abilities.py`**: Lógica para gerenciamento de itens e habilidades do jogo.
- **`main.py`**: Ponto de entrada do jogo, iniciando o loop principal.
- **`main_character.py`**: Código para o personagem do jogador (ex.: movimento, interações).
- **`map.py`**: Lógica para gerenciamento de mapas e tiles.
- **`props.py`**: Código para lidar com objetos interativos no ambiente do jogo.
- **`repositorio_sons.py`**: Módulo para gerenciamento de recursos de áudio e reprodução de sons.
- **`repositorio_sprites.py`**: Módulo para carregar e gerenciar recursos de sprite.
- **`sprites.py`**: Lógica geral de manipulação e renderização de sprites.
- **`ui.py`**: Componentes da interface do usuário e sua renderização.

### 5. **`tests/`**
Contém scripts de teste para garantir a funcionalidade do código.
- **`gameTest.py`**: Testes unitários para a lógica principal do jogo.
- **`test_player.py`**: Testes para as funcionalidades do personagem do jogador.
- **`UITest.py`**: Testes relacionados aos elementos da interface do usuário.

## Instruções de Instalação
Para instalar as dependências do projeto, utilize o seguinte comando:
```bash
pip install pygame
```

## Instruções de Uso
1. Clone o repositório:
   ```bash
   git clone https://github.com/HenryGasparelo/A2-LP-2024.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd A2-LP-2024
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o jogo:
   ```bash
   python src/main.py
   ```

## Captura de Tela
*Insira aqui uma captura de tela do jogo.*
