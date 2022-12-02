import pygame
import numpy as np
from math import *

SIDE = 40

is_free_for_tower = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    ]
enemies = []
towers = []

class Tower1:
    """Класс первой башни (с дискретными снарядами)"""
    def __init__(self, screen, x, y):
        global is_free_for_tower
        self.x = (x//SIDE) * SIDE + SIDE // 2
        self.y = (y//SIDE) * SIDE + SIDE // 2
        self.x_square = (self.x-SIDE//2) // SIDE
        self.y_square = (self.y-SIDE//2) // SIDE
        if is_free_for_tower[self.y_square][self.x_square] != 1:
            self.x = None
            self.y = None
        else:
            is_free_for_tower[self.y_square][self.x_square] = 2 + len(towers)
        self.screen = screen
        self.dmg = 50
        # Урон пушки
        self.speed = 30
        # Скорострельность
        self.angle = 0
        # Угол поворота
        self.radius = 200
        # Дальнобойность
        self.level = 1
        # Уровень башни (максимум 3)
        self.price = 100
        # Стоимость башни в у.е.
        self.upgrade_price = [20, 30, 40]
        # Стоимость улучшения башни (меняется в процессе (локальной) прогрессии)
        self.image = np.array([])
        # Переменная, хранящая изображение башни
        self.attacked_enemy = None
        # Переменная, хранящая атакованного врага

    def shoot(self, enemies, money):
        """ Функция выстрела по врагу
        enemies - список активных врагов на карте"""
        if self.attacked_enemy:
            if ((self.attacked_enemy.x - self.x) ** 2 + (self.attacked_enemy.y - self.y) ** 2) > self.radius ** 2 \
                    or self.attacked_enemy.hp <= 0:
                self.attacked_enemy = None
                money = self.shoot(enemies, money)
            else:
                money = self.attacked_enemy.hit(self.dmg, enemies, money)
        else:
            min_distance = self.radius
            for enemy in enemies:
                enemy_distance = np.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
                if enemy_distance <= min_distance:
                    min_distance = enemy_distance
                    self.attacked_enemy = enemy
            if self.attacked_enemy:
                money = self.shoot(enemies, money)
        return money

    def upgrade(self):
        """Если уровень не максимальный и достаточно денег, улучшает башню"""
        self.level += 1
        self.dmg += 10
        self.speed += 10
        self.radius += 20

    def draw(self):
        """Рисует башню (тут должна использоваться переменная self.image, но рисунков пока нет((((,
        поэтому рисует круг с дулом)"""
        if self.attacked_enemy:
            self.angle = atan2(self.attacked_enemy.y - self.y, self.attacked_enemy.x - self.x)
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), 15)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y),
                         (self.x + 20 * cos(self.angle), self.y + 20 * sin(self.angle)), 2)

    def sell(self, money, towers):
        money += self.price/2
        while self.level > 1:
            money += self.upgrade_price[self.level - 1]/2
            self.level -= 1
        towers.remove(self)
        is_free_for_tower[self.y_square][self.x_square] = 1
        return money, towers


class Enemy1:
    """Класс, описывающий превый тип врага"""
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 3
        # Скорость юнита
        self.dmg = 10
        # Урон юнита по главной постройке
        self.hp = 100
        # Здоровье юнита
        self.reward = 30
        # Вознаграждение за убийство юнита
        self.image = np.array([])
        # Изображение юнита
        self.radius = 10
        # Временная (!!!!!) переменная, отвечающая за размер врага

    def hit(self, tower_damage, enemies, money):
        """Функция, отвечающая за боль и страдания юнита"""
        self.hp -= tower_damage
        if self.hp <= 0:
            money += self.reward
            enemies.remove(self)
        
        return money

    def move(self):
        """Функция, двигающаяя юнита (пока что написана только для движения по прямой, т.к. пока неизвестны координаты точек изгиба дороги)"""
        self.x += self.speed

    def attack(self, fortress):
        fortress.hp -= self.dmg

    def draw(self):
        """Рисует врага (пока нет изображения - просто круг)"""
        pygame.draw.circle(self.screen, (0, 255, 0), (self.x, self.y), self.radius)
    def draw1(self):
        """Рисует врага (пока нет изображения - просто круг)"""
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.radius)


class Fortress(Enemy1):
    """Класс описывающий главное здание"""
    def __init__(self, screen):
        super().__init__(screen, 1075, 300)
        self.hp = 10000
        self.is_alive = True
        self.radius = 50
        # Временная (!!!!!)

    def hit(self, enemies):
        """Функция, отвечающая за повреждения главного здания"""
        for enemy in enemies:
            enemy_distance = np.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
            if enemy_distance <= 100:
                enemy.attack(self)
                if self.hp <= 0:
                    self.is_alive = False

    def alive_or_not(self):
        """Функция, отвечающая на вопрос: "проиграл ли игрок?" """
        return self.is_alive

    def draw(self):
        super().draw()
