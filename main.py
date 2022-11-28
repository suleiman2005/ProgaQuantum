from Classes import *
import random as rnd

FPS = 30
WIDTH = 1000
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
text_font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()
finished = False
enemies = []
tower = Tower1(screen, 500, 350)
towers = [tower]
fortress = Fortress(screen)
money = 0
time = 0
Delta_t = 1

while not finished:
    screen.fill((255, 255, 255))
    clock.tick(FPS)
    fortress.draw()
    if rnd.randint(1, 30) == 1:
        enemy = Enemy1(screen, 0, 300)
        enemies.append(enemy)
    for enemy in enemies:
        if enemy.x < 797:
            enemy.move()
        enemy.draw()
    for tower in towers:
        tower.draw()
        if time % tower.speed == 0:
            tower.shoot(enemies, money)
    fortress.hit(enemies)
    if not fortress.alive_or_not():
        finished = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    time += Delta_t
    pygame.display.update()

pygame.quit()


