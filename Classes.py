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

start_positions = [[180, 420, 620], [140, 460, 1060], [220, 380, 0]]
enemies = []
towers = []
bullets = []

class Bullet:
    def __init__(self, x, y, vx, vy, dmg):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.dmg = dmg
        self.live = 1
	
    def draw_and_move(self):
        draw_bullet(self.x, self.y)
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            bullets.remove(self)
        
    def hit_enemies(self, money):
        for enemy in enemies:
            if (enemy.x-self.x)**2 + (enemy.y-self.y)**2 <= enemy.radius**2:
                money = enemy.hit(self.dmg, money)
                bullets.remove(self)
                break
        return money
                
	

class Tower1:
    """Класс первой башни (с дискретными снарядами)"""
    def __init__(self, screen, stage, x_square, y_square):
        global is_free_for_tower
        self.x_square = x_square
        self.y_square = y_square
        self.x = self.x_square * SIDE + SIDE // 2
        self.y = self.y_square * SIDE + SIDE // 2
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

    def shoot(self, enemies):
        """ Функция выстрела по врагу
        enemies - список активных врагов на карте"""
        if self.attacked_enemy:
            if ((self.attacked_enemy.x - self.x) ** 2 + (self.attacked_enemy.y - self.y) ** 2) > self.radius ** 2 \
                    or self.attacked_enemy.hp <= 0:
                self.attacked_enemy = None
                self.shoot(enemies)
            else:
                self.angle = atan2(self.attacked_enemy.y - self.y, self.attacked_enemy.x - self.x)
                vx = BULLET_SPEED * cos(self.angle)
                vy = BULLET_SPEED * sin(self.angle)
                if self.attacked_enemy.axis == 'x':
                    vx += self.attacked_enemy.speed
                else:
                    vy += self.attacked_enemy.speed
                bullet = Bullet(self.x, self.y, vx, vy, self.dmg)
                bullets.append(bullet)
        else:
            min_distance = self.radius
            for enemy in enemies:
                enemy_distance = np.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
                if enemy_distance <= min_distance:
                    min_distance = enemy_distance
                    self.attacked_enemy = enemy
            if self.attacked_enemy:
                self.shoot(enemies)


    def upgrade(self):
        """Если уровень не максимальный и достаточно денег, улучшает башню"""
        self.level += 1
        self.dmg += 10
        self.speed += 10
        self.radius += 20

    def draw(self):
        """Рисует башню (тут должна использоваться переменная self.image, но рисунков пока нет((((,
        поэтому рисует круг с дулом)"""
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y),
                         (self.x + 20 * cos(self.angle), self.y + 20 * sin(self.angle)), 2)
        draw_tower(self.x, self.y, self.level)

    def sell(self, stage, towers):
        """Функция продажи башни"""
        for tower_index in range(len(towers)):
            if tower_index > is_free_for_tower[stage-1][self.y_square][self.x_square] - 2:
                is_free_for_tower[stage-1][towers[tower_index].y_square][towers[tower_index].x_square] -= 1
        is_free_for_tower[stage-1][self.y_square][self.x_square] = 1
        towers.remove(self)


class Enemy1:
    """Класс, описывающий превый тип врага"""
    def __init__(self, screen, x, y, time_creation):
        self.time_creation = time_creation
        self.screen = screen
        self.x = x
        self.y = y
        self.type = 1
        self.tik = 4
        self.speed = 2
        # Скорость юнита
        self.axis = 'x'
        #Ось движения юнита
        self.dmg = 10
        # Урон юнита по главной постройке
        self.hp = 200
        # Здоровье юнита
        self.reward = 30
        # Вознаграждение за убийство юнита
        self.image = np.array([])
        # Изображение юнита
        self.radius = 10
        # Временная (!!!!!) переменная, отвечающая за размер врага


    def hit(self, tower_damage, money):
        """Функция, отвечающая за боль и страдания юнита"""
        self.hp -= tower_damage
        if self.hp <= 0:
            money += self.reward
            enemies.remove(self)
        return money

    def move(self, stage):
        """Функция, двигающаяя юнита"""
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

    def draw(self, time):
        draw_enemy(self, time)


class Enemy2(Enemy1):
    """Класс, описывающий 2 тип врага"""
    def __init__(self, screen, x, y, time_creation):
        super().__init__(screen, x, y, time_creation)
        self.hp = 2800
        self.reward = 50

    def draw(self, time):
        draw_enemy1(self, time)

class Fortress:
    """Класс описывающий главное здание"""
    def __init__(self, screen):
        self.screen = screen
        self.x = 860
        self.y = 300
        self.hp = 10000
        self.is_alive = True

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
        draw_fort(self)
