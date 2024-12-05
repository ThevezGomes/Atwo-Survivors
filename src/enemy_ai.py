""""Métodos de IA que serão utilizados pelos inimigos"""
from game import *
from main_character import Player
import config
import math

class Enemy_AI:

    """
    Gerencia a inteligência artificial básica dos inimigos.

    Essa classe implementa métodos para detectar o jogador, calcular distâncias,
    gerenciar perseguições e direcionar os inimigos.

    Atributos:
        enemy (Enemy): Referência ao inimigo associado a esta IA.
        game (Game): Referência ao objeto principal do jogo.
        player (Player): Referência ao jogador controlado pelo usuário.
        seach_distance (int): Distância máxima que o inimigo pode enxergar.
        facing (str): Direção atual em que o inimigo está olhando ("up", "down", "left", "right").
        track_player (bool): Indica se o inimigo está rastreando o jogador.
        time_untracked (int): Tempo (em milissegundos) desde que o inimigo parou de rastrear o jogador.
    """

    def __init__(self, enemy):

        """
        Inicializa a IA do inimigo.

        Parâmetros:
            enemy (Enemy): Instância do inimigo para o qual a IA será aplicada.
        """

        # Define propriedades da IA dos inimigos
        self.enemy = enemy
        self.game = enemy.game
        self.player = self.game.player
        self.seach_distance = enemy.fov
        self.facing = "down"
        self.track_player = False
        self.time_untracked = 0

    def enemy_pursue(self):

        """
        Calcula os movimentos para que o inimigo persiga o jogador.

        Identifica a direção do jogador, ajusta a velocidade do inimigo e atualiza
        a orientação do sprite (facing).

        Retorna:
            tuple: Deslocamentos nos eixos X e Y para o próximo movimento.
        """

        target = self.target_detector()
        if not isinstance(target, Player):
            return 0, 0
        vector_module = self.distance_vector(target)

        if vector_module > 1 :
            constant = self.enemy.speed / vector_module
        else: constant = 0

        delta_x, delta_y = self.get_deltas(target)

        x_change = constant * delta_x
        y_change = constant * delta_y

        if abs(x_change)> abs(y_change):
            if x_change > 0: self.facing = "right"
            else: self.facing = "left"
        else:
            if y_change > 0: self.facing = "down"
            else: self.facing = "up"

        return x_change, y_change
    

    def target_detector(self): 

        """
        Detecta se o jogador está dentro do campo de visão do inimigo.

        Monitora a distância entre o inimigo e o jogador, liberando a perseguição
        quando o jogador está próximo e interrompendo quando está muito distante.

        Retorna:
            Player: Referência ao jogador caso esteja dentro do campo de visão.
            None: Caso contrário.
        """

        if self.distance_vector(self.player) <= self.seach_distance and self.distance_vector(self.player) > config.enemy_range[self.enemy.kind]:
                self.track_player = True
                return self.player
        elif self.distance_vector(self.player) > self.seach_distance:
            # Verifica se o inimigo está longe, se estiver, coleta o tempo para despawnar inimigos parados e distantes
            if self.track_player:
                self.time_untracked = pygame.time.get_ticks()
                self.track_player = False
            return None

    def get_deltas(self, player): # Calcula a distância entre o inimigo e uma entidade
        """
        Calcula a diferença de posição entre o inimigo e o jogador.

        Parâmetros:
            player (Player): Referência ao jogador.

        Retorna:
            tuple: Diferença em X (delta_x) e em Y (delta_y) entre o inimigo e o jogador.
        """
        delta_x = player.rect.x - self.enemy.rect.x
        delta_y = player.rect.y - self.enemy.rect.y

        return delta_x, delta_y


    def distance_vector(self, target):
        """
        Calcula a distância euclidiana entre o inimigo e um alvo.

        Parâmetros:
            target (Player): Entidade alvo para o cálculo da distância.

        Retorna:
            float: Distância euclidiana entre o inimigo e o alvo. Retorna 0 se o alvo não for válido.
        """
        if not isinstance(target, Player):
            return 0
        
        delta_x, delta_y = self.get_deltas(target)
        vector_norm = math.sqrt(delta_x ** 2 + delta_y **2)

        return vector_norm 

class Boss_IA(Enemy_AI):
    """
    Gerencia a inteligência artificial de chefes (Boss).

    Esta classe herda de `Enemy_AI` e modifica o comportamento de detecção de alvos
    para permitir que o Boss continue rastreando o jogador mesmo a grandes distâncias.
    """

    def __init__(self, enemy):

        """
        Inicializa a IA de um Boss.

        Herda os atributos e métodos de `Enemy_AI`.

        Parâmetros:
            enemy (Enemy): Instância do Boss para o qual a IA será aplicada.
        """

        # Define as mesmas propriedades da IA de um inimigo
        super().__init__(enemy)
        
    def target_detector(self):
        
        """
        Detecta se o jogador está longe o suficiente para iniciar ou continuar a perseguição.

        Sobrescreve o método `target_detector` da classe base para ajustar o comportamento do Boss.

        Retorna:
            Player: Referência ao jogador caso esteja a uma distância maior que o limite configurado.
        """

        # Verifica se o player está longe o bastante para liberar a perseguição, sem parar o boss caso esteja distante
        if self.distance_vector(self.player) > 40:
            self.track_player = True
            return self.player






