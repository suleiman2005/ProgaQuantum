from math import *
from Textures import *
import Common_list

SIDE = 40
start_positions = [[0, 599, 620], [140, 460, 1199], [220, 380, 0]]

def generate_road():
    Common_list.is_free_for_tower = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
            Common_list.bullets.remove(self)
        
    def hit_enemies(self, money):
        for enemy in Common_list.enemies:
            if (enemy.x-self.x)**2 + (enemy.y-self.y)**2 <= enemy.radius**2:
                money = enemy.hit(self.dmg, money)
                Common_list.bullets.remove(self)
                break
        return money
                
	

class Tower1:
    """Класс первой башни (с дискретными снарядами)"""
    def __init__(self, screen, stage, x_square, y_square):
        self.type = 1
        self.x_square = x_square
        self.y_square = y_square
        self.x = self.x_square * SIDE + SIDE // 2
        self.y = self.y_square * SIDE + SIDE // 2
        Common_list.is_free_for_tower[stage-1][self.y_square][self.x_square] = 2 + len(Common_list.towers)
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
        self.t = self.speed

    def shoot(self):
        """ Функция выстрела по врагу
        enemies - список активных врагов на карте"""
        if self.attacked_enemy:
            if ((self.attacked_enemy.x - self.x) ** 2 + (self.attacked_enemy.y - self.y) ** 2) > self.radius ** 2 \
                    or self.attacked_enemy.hp <= 0:
                self.attacked_enemy = None
                self.shoot()
            else:
                self.angle = atan2(self.attacked_enemy.y - self.y, self.attacked_enemy.x - self.x)
                vx = BULLET_SPEED * cos(self.angle)
                vy = BULLET_SPEED * sin(self.angle)
                if self.attacked_enemy.axis == 'x':
                    vx += self.attacked_enemy.speed
                else:
                    vy += self.attacked_enemy.speed
                bullet = Bullet(self.x, self.y, vx, vy, self.dmg)
                Common_list.bullets.append(bullet)
        else:
            min_distance = self.radius
            for enemy in Common_list.enemies:
                enemy_distance = np.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
                if enemy_distance <= min_distance:
                    min_distance = enemy_distance
                    self.attacked_enemy = enemy
            if self.attacked_enemy:
                self.shoot()

    def upgrade(self):
        """Если уровень не максимальный и достаточно денег, улучшает башню"""
        self.level += 1
        self.dmg += 10
        self.speed -= 10
        self.t = self.speed
        self.radius += 20

    def draw(self):
        """Рисует башню (тут должна использоваться переменная self.image, но рисунков пока нет((((,
        поэтому рисует круг с дулом)"""
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y),
                         (self.x + 20 * cos(self.angle), self.y + 20 * sin(self.angle)), 2)
        draw_tower(self.x, self.y, self.level)

    def sell(self, stage):
        """Функция продажи башни"""
        for tower_index in range(len(Common_list.towers)):
            if tower_index > Common_list.is_free_for_tower[stage-1][self.y_square][self.x_square] - 2:
                Common_list.is_free_for_tower[stage-1][Common_list.towers[tower_index].y_square][Common_list.towers[tower_index].x_square] -= 1
        Common_list.is_free_for_tower[stage-1][self.y_square][self.x_square] = 1
        Common_list.towers.remove(self)

class Tower2:
    """Класс второй башни (с лазерами)"""
    def __init__(self, screen, stage, x_square, y_square):
        self.type = 2
        self.x_square = x_square
        self.y_square = y_square
        self.x = self.x_square * SIDE + SIDE // 2
        self.y = self.y_square * SIDE + SIDE // 2
        Common_list.is_free_for_tower[stage-1][self.y_square][self.x_square] = 2 + len(Common_list.towers)
        self.screen = screen
        self.dmg = 1
        # Урон пушки
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

    def shoot(self, money):
        """ Функция выстрела по врагу
        enemies - список активных врагов на карте"""
        if self.attacked_enemy:
            if ((self.attacked_enemy.x - self.x) ** 2 + (self.attacked_enemy.y - self.y) ** 2) > self.radius ** 2 \
                    or self.attacked_enemy.hp <= 0:
                self.attacked_enemy = None
                money = self.shoot(money)
            else:
                self.angle = atan2(self.attacked_enemy.y - self.y, self.attacked_enemy.x - self.x)
                money = self.attacked_enemy.hit(self.dmg, money)
        else:
            min_distance = self.radius
            for enemy in Common_list.enemies:
                enemy_distance = np.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
                if enemy_distance <= min_distance:
                    min_distance = enemy_distance
                    self.attacked_enemy = enemy
            if self.attacked_enemy:
                money = self.shoot(money)
        return money

    def upgrade(self):
        """Если уровень не максимальный и достаточно денег, улучшает башню"""
        self.level += 1
        self.dmg += 10
        self.speed -= 10
        self.t = self.speed
        self.radius += 20

    def draw(self):
        """Рисует башню (тут должна использоваться переменная self.image, но рисунков пока нет((((,
        поэтому рисует круг с дулом)"""
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y),
                         (self.x + 20 * cos(self.angle), self.y + 20 * sin(self.angle)), 2)
        draw_tower(self.x, self.y, self.level)

    def sell(self, stage):
        """Функция продажи башни"""
        for tower_index in range(len(Common_list.towers)):
            if tower_index > Common_list.is_free_for_tower[stage-1][self.y_square][self.x_square] - 2:
                Common_list.is_free_for_tower[stage-1][Common_list.towers[tower_index].y_square][Common_list.towers[tower_index].x_square] -= 1
        Common_list.is_free_for_tower[stage-1][self.y_square][self.x_square] = 1
        Common_list.towers.remove(self)

class Enemy1:
    """Класс, описывающий превый тип врага"""
    def __init__(self, screen, x, y, time_creation):
        self.time_creation = time_creation
        self.screen = screen
        self.x = x
        self.y = y
        self.type = 1
        self.tik = 4
        self.speed = 1
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
            Common_list.enemies.remove(self)
        return money

    def move(self, stage):
        """Функция, двигающаяя юнита"""
        if self.axis == 'x' and not (0 <= (self.x+np.sign(self.speed)*(SIDE//2+1)) // SIDE <= 29):
            self.speed = -self.speed
        elif self.axis == 'x' and Common_list.abv[stage-1][self.y // SIDE][(self.x+np.sign(self.speed)*(SIDE//2+1)) // SIDE] != 0:
            self.axis = 'y'
            self.x = (self.x//SIDE) * SIDE + SIDE // 2 
            if not (0 <= (self.y+np.sign(self.speed)*(SIDE//2+1)) // SIDE <= 14) or Common_list.abv[stage-1][(self.y+np.sign(self.speed)*(SIDE//2+1)) // SIDE][self.x // SIDE] != 0:
                self.speed = -self.speed
        elif self.axis == 'y' and not (0 <= (self.y+np.sign(self.speed)*(SIDE//2+1)) // SIDE <= 14):
            self.speed = -self.speed
        elif self.axis == 'y' and (Common_list.abv[stage-1][(self.y+np.sign(self.speed)*(SIDE//2+1)) // SIDE][self.x // SIDE] != 0 or abs(self.y - 300) <= abs(self.speed) / 2):
            self.axis = 'x'
            self.y = (self.y//SIDE) * SIDE + SIDE // 2
            if not (0 <= (self.x+np.sign(self.speed)*(SIDE//2+1)) // SIDE <= 29) or Common_list.abv[stage-1][self.y // SIDE][(self.x+np.sign(self.speed)*(SIDE//2+1)) // SIDE] != 0:
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
        self.hp = 50
        self.reward = 50
        self.tik = 2
        self.speed = 4

    def draw(self, time):
        draw_enemy1(self, time)

class Enemy4(Enemy1):
    """Класс, описывающий 2 тип врага"""
    def __init__(self, screen, x, y, time_creation):
        super().__init__(screen, x, y, time_creation)
        self.hp = 200
        self.reward = 50
        self.tik = 4
        self.speed = 1

    def draw(self, time):
        draw_enemy4(self, time)

class Fortress:
    """Класс описывающий главное здание"""
    def __init__(self, screen):
        self.screen = screen
        self.x = 860
        self.y = 300
        self.hp = 10000
        self.is_alive = True

    def hit(self):
        """Функция, отвечающая за повреждения главного здания"""
        for enemy in Common_list.enemies:
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
        
class MainBack:
    def __init__(self):
        self.angle = 0
        self.main_back_surface = pygame.transform.scale(main_back_surface, (main_back_surface.get_width() // 0.5,\
                                                     main_back_surface.get_height() // 0.5))

    def draw(self):
        screen.fill(WHITE)
        screen.blit(self.main_back_surface, (-250 + 200*cos(self.angle), -150 + 100*sin(self.angle)))
        self.angle += 0.007 + 0.002 * cos(self.angle/pi)
