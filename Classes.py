import pygame
import numpy as np
from math import *
from Textures import *

SIDE = 40

is_free_for_tower = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                     ],
                     [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                     ],
                     [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                      [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                      [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                      [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                      [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                     ]
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
        if is_free_for_tower[stage-1][self.y_square][self.x_square] != 1:
            self.x = None
            self.y = None
        else:
            is_free_for_tower[stage-1][self.y_square][self.x_square] = 2 + len(towers)
        self.screen = screen
        self.dmg = 50
        # Урон пушки
        self.speed = 30
        # Скорострельность
        self.angle = 0
        # Угол поворота
        self.radius = 200
        # Дальнобойность
        self.level = 0
        # Уровень башни (максимум 3)
        self.price = 1000
        # Стоимость башни в у.е.
        self.upgrade_price = [20, 500, 2000]
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
        """Если уровень не максимальный и достаточно денег, улучшает башню
        money - Казна игрока
        text_font - шрифт оповещения
        text_colour - цвет оповещения"""
            #if money >= self.upgrade_price[self.level]:
                #money -= self.upgrade_price[self.level]
        self.level += 1
        self.dmg += 10
        self.speed += 10
        self.radius += 20
            #else:
               # return text_font.render("Нужно больше золота...", True, text_colour)

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
        while self.level >= 1:
            money += self.upgrade_price[self.level - 1]/2
            self.level -= 1
        towers.remove(self)
        is_free_for_tower[stage-1][self.y_square][self.x_square] = 1
        return money


class Enemy1:
    """Класс, описывающий превый тип врага"""
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 1
        # Скорость юнита
        self.axis = 'x'
        #Ось движения юнита
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
        if self.axis == 'x' and abv[stage-1][self.y // SIDE][(self.x+np.sign(self.speed)*(SIDE//2+1)) // SIDE] != 0:
            self.axis = 'y'
            self.x = (self.x//SIDE) * SIDE + SIDE // 2
            if abv[stage-1][(self.y+np.sign(self.speed)*(SIDE//2+1)) // SIDE][self.x // SIDE] != 0:
                self.speed = -self.speed
        elif self.axis == 'y' and (abv[stage-1][(self.y+np.sign(self.speed)*(SIDE//2+1)) // SIDE][self.x // SIDE] != 0 or abs(self.y - 300) <= abs(self.speed) / 2):
            self.axis = 'x'
            self.y = (self.y//SIDE) * SIDE + SIDE // 2
            if abv[stage-1][self.y // SIDE][(self.x+np.sign(self.speed)*(SIDE//2+1)) // SIDE] != 0:
                self.speed = -self.speed
        if self.axis == 'x':
            self.x += self.speed
        else:
            self.y += self.speed
        if self.y == 300 and self.x >= 840:
            self.x = 840

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
        super().__init__(screen, 860, 300)
        self.hp = 10000
        self.is_alive = True
        self.radius = 20
        # Временная (!!!!!)

    def hit(self, enemies):
        """Функция, отвечающая за повреждения главного здания"""
        for enemy in enemies:
            enemy_distance = np.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
            if enemy_distance == 20:
                enemy.attack(self)
                if self.hp <= 0:
                    self.is_alive = False

    def alive_or_not(self):
        """Функция, отвечающая на вопрос: "проиграл ли игрок?" """
        return self.is_alive

    def draw(self):
        super().draw()
