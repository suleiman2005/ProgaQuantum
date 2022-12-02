import pygame
import numpy as np

BLACK = (0, 0, 0)


def erase_useless_buttons(buttons):
    """функция стирающая ненужные в некоторый момент кнопки"""
    for button in buttons:
        if button.type == "upgrade_button":
            buttons.remove(button)


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
        """ Ричует кнопку """
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
        self.screen.blit(self.text_font.render('Quit (esc)', True, (0, 0, 0)),
                         (self.x + self.width/5, self.y + self.height/10))


class UpgradeButton(Button):
    """Класс кнопки апгрейда"""
    def __init__(self, screen, x, y, text_font, width=250, height=50, colour=(255, 0, 0)):
        super().__init__(screen, x, y, text_font, width, height, colour)
        self.type = "upgrade_button"

    def draw(self):
        self.screen.blit(self.text_font.render("Upgrade tower", True, BLACK),
                         (self.x, self.y + self.height/10))



