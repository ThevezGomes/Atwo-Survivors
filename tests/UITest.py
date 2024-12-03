import pygame
import unittest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from ui import *  # Certifique-se de que o caminho está correto para a classe Button
from props import *

# Função para simular a entrada do mouse
def create_mouse_click_mock(pressed_buttons):
    def mocked_get_pressed():
        tmp = [0] * 3  # Suporte para 3 botões de mouse
        for key in pressed_buttons:
            tmp[key] = 1
        return tmp
    return mocked_get_pressed

# Função para simular a posição do mouse
def create_mouse_pos_mock(mouse_pos):
    def mocked_get_pos():
        return mouse_pos
    return mocked_get_pos

# Testes da classe Button
class TestButton(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.button = Button(100, 100, 200, 50, (255, 255, 255), "Test", 24)

    def test_button_draw(self):
        # Verifica se o botão é desenhado corretamente na tela
        self.button.draw(self.screen)
        # Adicione verificações se necessário, como a verificação da superfície renderizada

    def test_button_hover(self):
        # Simula o mouse sobre o botão e verifica se a imagem muda (hover)
        mock_function = create_mouse_pos_mock((150, 125))  # Posição do mouse sobre o botão
        pygame.mouse.get_pos = mock_function
        self.button.update((150, 125))
        # Verifique se a imagem do botão foi alterada para o estado de hover

        mock_function = create_mouse_pos_mock((300, 300))  # Posição do mouse fora do botão
        pygame.mouse.get_pos = mock_function
        self.button.update((300, 300))
        # Verifique se a imagem do botão voltou para o estado normal

    def test_button_click(self):
        # Simula um clique no botão e verifica se ele é pressionado corretamente
        mock_function = create_mouse_click_mock([0])  # Botão esquerdo do mouse pressionado
        pygame.mouse.get_pressed = mock_function
        mock_function_pos = create_mouse_pos_mock((150, 125))  # Posição do mouse sobre o botão
        pygame.mouse.get_pos = mock_function_pos

        # Verifica se o botão foi pressionado
        self.assertTrue(self.button.is_pressed((150, 125), pygame.mouse.get_pressed()))

        # Simula um clique fora do botão
        mock_function_pos = create_mouse_pos_mock((300, 300))  # Posição do mouse fora do botão
        pygame.mouse.get_pos = mock_function_pos
        self.assertFalse(self.button.is_pressed((300, 300), pygame.mouse.get_pressed()))


class TestHub(unittest.TestCase):
    def test_hub_initialization(self):
        hub = Hub(100, 200, 45, 5, "inventory")
        self.assertEqual(hub.x, 100)
        self.assertEqual(hub.y, 200)
        self.assertEqual(hub.max_slots, 5)
        self.assertEqual(hub.type_hub, "inventory")
        
    def test_add_item(self):
        hub = Hub(100, 200, 45, 5, "inventory")
        item = Item("energy_ball","Bola de energia", "Destroi tudo no caminho.", max_level=5)
        hub.add_item(item)
        self.assertIn(item, hub.items[0])

class TestSkillsHub(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((800, 600))

    def test_skills_hub_initialization(self):
        skills_hub = Skills_hub(100, 200, 45, 5)
        self.assertEqual(skills_hub.type_hub, "skills_hub")
        self.assertEqual(skills_hub.x, 100)
        self.assertEqual(skills_hub.y, 200)
        self.assertEqual(skills_hub.max_slots, 5)
        
    def test_add_skill(self):
        skills_hub = Skills_hub(100, 200, 45, 5)
        skill = Ability("nice_boots", "Botas Legais", "Aumenta a velocidade", "speed", max_level=5)
        skills_hub.add_item(skill)
        self.assertIn(skill, skills_hub.items[0])

    def tearDown(self):
        pygame.quit()



class TestInventory(unittest.TestCase):
    def test_inventory_initialization(self):
        inventory = Inventory(100, 200, 45, 5)
        self.assertEqual(len(inventory.items), 0)

    def test_add_remove_item(self):
        inventory = Inventory(100, 200, 45, 5)
        item = Item("energy_ball","Bola de energia", "Destroi tudo no caminho.", max_level=5)
        inventory.add_item(item)
        self.assertIn(item, inventory.items[0])

    def test_inventory_capacity(self):
        inventory = Inventory(100, 200, 45, 5)
        item = Item("energy_ball","Bola de energia", "Destroi tudo no caminho.", max_level=5)
        for i in range(5):
            inventory.add_item(Item("energy_ball", f"Bola de energia{i}", "Destroi tudo no caminho.", max_level=5))
        self.assertEqual(len(inventory.items), 5)

        result = inventory.add_item(item)
        self.assertFalse(result)
        self.assertEqual(len(inventory.items), 5)

    def test_inventory_selection_key_press(self):
        inventory = Inventory(100, 200, 45, 5)
        for i in range(5):
            inventory.add_item(Item("energy_ball", f"Bola de energia{i}", "Destroi tudo no caminho.", max_level=5))
        # Testa a seleção de item usando teclas numéricas (1 a 5)
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_1)
        inventory.selection_event(event)
        self.assertEqual(inventory.selected_item_index, 0)  # Deve selecionar o primeiro item

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_3)
        inventory.selection_event(event)
        self.assertEqual(inventory.selected_item_index, 2)  # Deve selecionar o terceiro item

    def test_inventory_selection_mouse_scroll(self):
        inventory = Inventory(100, 200, 45, 5)
        for i in range(5):
            inventory.add_item(Item("energy_ball", f"Bola de energia{i}", "Destroi tudo no caminho.", max_level=5))
        # Testa a seleção de item usando a rolagem do mouse
        inventory.selected_item_index = 0  # Define um índice inicial para a seleção

        event = pygame.event.Event(pygame.MOUSEWHEEL, y=1)  # Rolagem para baixo (avançar para o próximo item)
        inventory.selection_event(event)
        self.assertEqual(inventory.selected_item_index, 1)  # Seleciona o próximo item

        event = pygame.event.Event(pygame.MOUSEWHEEL, y=-1)  # Rolagem para cima (voltar para o item anterior)
        inventory.selection_event(event)
        self.assertEqual(inventory.selected_item_index, 0)  # Seleciona o item anterior

        # Simula rolagem além do final do inventário para garantir que a seleção cicla corretamente
        for _ in range(10):  # Move para frente além do limite
            event = pygame.event.Event(pygame.MOUSEWHEEL, y=1)
            inventory.selection_event(event)
        self.assertEqual(inventory.selected_item_index, 0)  # O índice deve ser o primeiro item (0)

        event = pygame.event.Event(pygame.MOUSEWHEEL, y=-1)  # Volta um item
        inventory.selection_event(event)
        self.assertEqual(inventory.selected_item_index, 4)  # Seleciona o item anterior

class TestBar(unittest.TestCase):
    def setUp(self):
        # Inicializa o Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def test_health_bar_drawing(self):
        # Testa se a barra de saúde é desenhada corretamente
        health_bar = HealthBar(100, (255, 0, 0), (0, 0, 0), (0, 255, 0), 200, 20, 50, 50, "../assets/img/WarriorIcon.png")
        health_bar.draw(self.screen)
        self.assertEqual(health_bar.max, 100)
        self.assertEqual(health_bar.amount, 100)
        self.assertEqual(health_bar.border_color, (255, 0, 0))
        self.assertEqual(health_bar.background_color, (0, 0, 0))
        self.assertEqual(health_bar.color, (0, 255, 0))
        self.assertEqual(health_bar.width, 20.0)
        self.assertEqual(health_bar.height, 20)
        self.assertEqual(health_bar.x, 230.0)
        self.assertEqual(health_bar.y, 50)

    def test_experience_bar_drawing(self):
        # Testa se a barra de experiência é desenhada corretamente
        exp_bar = ExperienceBar((255, 0, 0), (0, 0, 0), (0, 255, 0), 300, 20, 100, 100, 1, 50)
        exp_bar.draw(self.screen)
        # Verifica se a função de desenho foi chamada

    def test_boss_bar_drawing(self):
        # Testa se a barra de vida do chefe é desenhada corretamente
        boss_bar = BossBar(200, (255, 0, 0), (0, 0, 0), (0, 255, 0), 300, 20, 100, 100, "Boss Name")
        boss_bar.draw(self.screen)
        # Verifica se a função de desenho foi chamada

    def tearDown(self):
        pygame.quit()

class TestTimeGame(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste."""
        pygame.init()
        self.screen = pygame.Surface((800, 600))  # Superfície para renderizar a tela
        self.timer = TimeGame(400, 300)

    def test_timer_initialization(self):
        """Testa a inicialização do temporizador."""
        self.assertEqual(self.timer.x, 400)
        self.assertEqual(self.timer.y, 300)
        self.assertFalse(self.timer.time_paused)
        self.assertEqual(self.timer.elapsed_time, 0)
        self.assertEqual(self.timer.total_elapsed, 0)

    @patch('pygame.time.get_ticks', return_value=1000)
    def test_timer_start(self, mock_get_ticks):
        """Testa a função de iniciar o temporizador."""
        self.timer.start()
        self.assertEqual(self.timer.start_time, 1000)
        self.assertEqual(self.timer.elapsed_time, 0)
        self.assertFalse(self.timer.time_paused)

    @patch('pygame.time.get_ticks', return_value=5000)
    def test_timer_pause(self, mock_get_ticks):
        """Testa a função de pausar o temporizador."""
        self.timer.start()
        self.timer.pause()
        self.assertTrue(self.timer.time_paused)
        self.assertEqual(self.timer.elapsed_time, 0)

    @patch('pygame.time.get_ticks', return_value=10000)
    def test_timer_resume(self, mock_get_ticks):
        """Testa a função de retomar o temporizador."""
        self.timer.start()
        self.timer.pause()
        self.timer.resume()
        self.assertFalse(self.timer.time_paused)
        self.assertEqual(self.timer.start_time, 10000)

@patch('pygame.time.get_ticks', side_effect=[2000, 5000, 8000])
def test_timer_update_event_triggered(self, mock_get_ticks):
    """Testa a atualização e disparo de eventos do temporizador."""
    self.timer.start()
    # Adiciona um evento que será disparado após 3 segundos
    event_func = MagicMock()
    self.timer.add_event(3, event_func)

    # Atualiza o temporizador para 2 segundos, evento não deve disparar
    self.timer.update()
    self.assertEqual(len(self.timer.events), 1)  # O evento ainda deve estar presente

    # Atualiza o temporizador para 5 segundos, evento deve disparar
    self.timer.update()
    self.assertEqual(len(self.timer.events), 0)  # O evento deve ter sido removido e disparado
    event_func.assert_called_once()  # Verifica se o evento foi chamado

class TestSelectionItem(unittest.TestCase):
    def setUp(self):
        # Inicializa o Pygame e cria uma superfície de teste
        pygame.init()
        self.screen = pygame.Surface((800, 600))
        
        # Mock do item com propriedades básicas
        self.item_mock = MagicMock()
        self.item_mock.name = "Item Teste"
        self.item_mock.description = "Descrição do item"
        self.item_mock.sprite = '../assets\img\Warrior.png'  # Caminho para o ícone (mockado)

        # Cria o objeto SelectionItem
        self.selection_item = SelectionItem(100, 100, 200, 100, (255, 255, 255), self.item_mock, 20)

    def test_initialization(self):
        """Teste de inicialização do SelectionItem"""
        self.assertEqual(self.selection_item.item.name, "Item Teste")
        self.assertEqual(self.selection_item.item.description, "Descrição do item")
        self.assertEqual(self.selection_item.fg, (255, 255, 255))
        self.assertIsInstance(self.selection_item.rect, pygame.Rect)

    @patch('pygame.image.load')
    @patch('pygame.font.Font')
    def test_draw(self, mock_font, mock_image_load):
        """Teste de renderização do SelectionItem"""
        # Mock da fonte e da imagem
        mock_font.return_value.render = MagicMock(return_value=pygame.Surface((100, 20)))
        mock_image_load.return_value = pygame.Surface((200, 100))

        # Chama o método draw e verifica se a superfície é desenhada
        self.selection_item.draw(self.screen)

    def test_is_pressed(self):
        """Teste de clique no botão"""
        pressed = (1, 0, 0)  # Simula o clique do botão esquerdo do mouse
        self.assertTrue(self.selection_item.is_pressed((150, 150), pressed))  # Dentro do botão
        self.assertFalse(self.selection_item.is_pressed((50, 50), pressed))   # Fora do botão

    def tearDown(self):
        # Finaliza o Pygame após os testes
        pygame.quit()

if __name__ == "__main__":
    unittest.main()

