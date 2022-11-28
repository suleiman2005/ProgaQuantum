import pygame
import numpy as np
from math import *


class Tower1:
    """Класс первой башни (с дискретными снарядами)"""
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.dmg = 25
        # Урон пушки
        self.speed = 30
        # Скорострельность
        self.angle = 0
        # Угол поворота
        self.radius = 100
        # Дальнобойность
        self.level = 0
        # Уровень башни (максимум 3)
        self.price = 1000
        # Стоимость башни в у.е.
        self.upgrade_price = [250, 500, 2000]
        # Стоимость улучшения башни (меняется в процессе (локальной) прогрессии)
        self.image = np.array([])
        # Переменная, хранящая изображение башни
        self.attacked_enemy = None
        # Переменная, хранящая атакованного врага

    def shoot(self, enemies):
        """ Функция выстрела по врагу
        enemies - список активных врагов на карте"""
        if self.attacked_enemy:
            if ((self.attacked_enemy.x - self.x) ** 2 + (self.attacked_enemy.y - self.y) ** 2) > self.radius ** 2:
                self.attacked_enemy = None
                self.shoot(enemies)
            else:
                self.attacked_enemy.hit(self.dmg)
        else:
            min = self.radius
            for enemy in enemies:
                enemy_distance = np.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
                if enemy_distance <= min:
                    min = enemy_distance
                    self.attacked_enemy = enemy
            if self.attacked_enemy:
                self.shoot(enemies)
            else:
                pass

    def upgrade(self, money, text_font, text_colour):
        """Если уровень не максимальный и достаточно денег, улучшает башню
        money - Казна игрока
        text_font - шрифт оповещения
        text_colour - цвет оповещения"""
        if self.level >= 3:
            pass
        else:
            if money >= self.upgrade_price[self.level]:
                money -= self.upgrade_price[self.level]
                self.level += 1
                self.dmg += 10
                self.speed += 5
                self.radius += 20
                return money
            else:
                return text_font.render("Нужно больше золота...", True, text_colour)

    def draw(self):
        """Рисует башню (тут должна использоваться переменная self.image, но рисунков пока нет((((,
        поэтому рисует круг с дулом)"""
        if self.attacked_enemy:
            self.angle = atan2(self.attacked_enemy.y - self.y, self.attacked_enemy.x - self.x)
        else:
            self.angle = 0
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), 5)
        pygame.draw.line(self.screen, (0, 0, 0), self.x, self.y,
                         self.x + 10 * cos(self.angle), self.y + 10 * sin(self.angle))

    def sell(self, money, towers):
        money += self.price/2
        while self.level >= 1:
            money += self.upgrade_price[self.level - 1]/2
            self.level -= 1
        towers.remove(self)
        return money