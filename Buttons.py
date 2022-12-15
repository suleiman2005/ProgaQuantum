from Classes import *
from Textures import *
import Common_list


def erase_useless_buttons(text_font):
    """функция стирающая ненужные в некоторый момент кнопки"""
    Common_list.buttons = [QuitButton(screen, 1100, 0, text_font)]


class Button:
    """ Общий класс кнопки (родитель всех кнопок) """
    def __init__(self, screen, x, y, text_font, width=100, height=50, colour=(255, 0, 0)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        # Ширина кнопки
        self.height = height
        # Высота кнопки
        self.colour = colour
        # Цвет кнопки
        self.text_font = text_font
        # Шрифт текста на кнопке (в идиале бы иконки...)
        self.image = np.array([])
        # Иконка(в идеале)

    def draw(self):
        """ Рисует кнопку """
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))

    def is_pressed(self, event):
        """ Распознаёт, было ли сделано нажатие по кнопке """
        if self.x <= event.pos[0] <= self.x + self.width and self.y <= event.pos[1] <= self.y + self.height:
            return True
        else:
            return False


class QuitButton(Button):
    """ Класс кнопки выхода """
    def __init__(self, screen, x, y, text_font, width=100, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.type = "quit_button"

    def draw(self):
        super().draw()
        self.screen.blit(self.text_font.render('Quit', True, (0, 0, 0)),
                         (self.x + self.width/5, self.y + self.height/10))


class UpgradeButton(Button):
    """Класс кнопки апгрейда"""
    def __init__(self, screen, x, y, text_font, width=270, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.type = "upgrade_button"

    def draw(self):
        self.screen.blit(self.text_font.render("Upgrade tower (z)", True, BLACK), (self.x, self.y + self.height/10))

    def upgrade_initiation(self, twr, money):
        """функция, запускпющая процесс улучшения"""
        if twr.level >= 3:
            text = "Maximum level"
        elif money >= twr.upgrade_price[twr.level - 1]:
            money -= twr.upgrade_price[twr.level - 1]
            twr.upgrade()
            text = "There is tower LVL " + str(twr.level)
        elif money < twr.upgrade_price[twr.level - 1]:
            text = "Need more money"
        return money, text


class SellButton(Button):
    def __init__(self, screen, x, y, text_font, width=200, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.type = "sell_button"

    def draw(self):
        self.screen.blit(self.text_font.render("Sell tower (x)", True, BLACK), (self.x, self.y + self.height/10))


class BuildButton(Button):
    def __init__(self, screen, x, y, text_font, width=220, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.type = "build_button"

    def draw(self):
        self.screen.blit(self.text_font.render("Build tower (z)", True, BLACK), (self.x, self.y + self.height / 10))

    def build_initiation(self, money, screen, x_square_light, y_square_light, button, play_menu_text_surface, stage, active_tower):
        """функция, запускающая процесс постройки"""
        if money < 100:
            text = "Not enough money"
        else:
            Common_list.abv[stage-1][y_square_light][x_square_light] = 1
            text = "There is tower LVL " + str(1)
            active_tower = Tower1(screen, stage, x_square_light, y_square_light)
            Common_list.towers.append(active_tower)
            money -= 100
        return money, text, active_tower


class StartButton(Button):
    def __init__(self, screen, x, y, text_font, width=200, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.type = "start_button"

    def draw(self, COLOUR):
        self.screen.blit(self.text_font.render("Start Game", True, COLOUR), (self.x, self.y))


class ExitButton(Button):
    def __init__(self, screen, x, y, text_font, width=200, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width=200, height=50, colour=(255, 0, 0))
        self.type = "exit_button"

    def draw(self, COLOUR):
        self.screen.blit(self.text_font.render("Exit", True, COLOUR), (self.x, self.y))


class SelectButton1(Button):
    def __init__(self, screen, x, y, text_font, width=200, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.name = "level 1"
        self.type = "level1_button"

    def draw(self, COLOUR):
        self.screen.blit(self.text_font.render(self.name, True, COLOUR), (self.x, self.y))


class SelectButton2(SelectButton1):
    def __init__(self, screen, x, y, text_font, width=200, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.name = "level 2"
        self.type = "level2_button"


class SelectButton3(SelectButton1):
    def __init__(self, screen, x, y, text_font, width=200, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.name = "level 3"
        self.type = "level3_button"


class ExitToMainMenuButton(StartButton):
    def draw(self, COLOUR):
        self.screen.blit(self.text_font.render("Exit to main menu", True, COLOUR), (self.x, self.y))



