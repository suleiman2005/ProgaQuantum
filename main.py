from Classes import *
import random as rnd

FPS = 60
WIDTH = 1500
HEIGHT = 750

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
text_font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()
finished = False
enemies = []
towers = []
fortress = Fortress(screen)
money = 100
time = 0
Delta_t = 1

while not finished:
    screen.fill((255, 255, 255))
    clock.tick(FPS)
    fortress.draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and money >= 100:
                tower = Tower1(screen, event.pos[0], event.pos[1])
                if tower.x != None:
                    towers.append(tower)
                    money -= 100
        if event.type == pygame.QUIT:
            finished = True
    if rnd.randint(1, 30) == 1:
        enemy = Enemy1(screen, 0, 375)
        enemies.append(enemy)
    for enemy in enemies:
        if enemy.x < 1300:
            enemy.move()
        enemy.draw()
    for tower in towers:
        tower.draw()
        if time % tower.speed == 0:
            money = tower.shoot(enemies, money)
    fortress.hit(enemies)
    if not fortress.alive_or_not():
        finished = True

    time += Delta_t
    pygame.display.update()

pygame.quit()


