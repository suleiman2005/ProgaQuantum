import pygame

from Textures import *
from Buttons import *
from Classes import *
import random as rnd


FPS = 60


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
text_font = pygame.font.Font(None, 24)
play_menu_text_surface = pygame.font.SysFont('Comic Sans MS', 30, True)
text = ""
play_menu_surface = pygame.image.load('img/игровое меню.png').convert()
play_menu_surface.set_colorkey((255, 255, 255))
play_menu_surface = pygame.transform.scale(play_menu_surface, (play_menu_surface.get_width() // 1.45, play_menu_surface.get_height() // 1.135))
play_menu_rect = play_menu_surface.get_rect(center=(WIDTH // 2, 700))
clock = pygame.time.Clock()
finished = False
fortress = Fortress(screen)
buttons = [QuitButton(screen, 1100, 0, text_font)]
money = 100
time = 0
Delta_t = 1
x_square_light = -1
y_square_light = -1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


while not finished:
    screen.fill(WHITE)
    textures()



    clock.tick(FPS)
    screen.blit(text_font.render("Money " + str(int(money)), True, (0, 0, 0)), (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            erase_useless_buttons(buttons)
            for button in buttons:
                if button.is_pressed(event):
                    if button.type == "quit_button":
                        finished = True
            if event.button == 1:
                erase_useless_buttons(buttons)
                if event.pos[1] < 600:
                    x_square_light = event.pos[0] // SIDE
                    y_square_light = event.pos[1] // SIDE
                    if is_free_for_tower[y_square_light][x_square_light] == 0:
                        text = "You can't build tower there"
                    elif is_free_for_tower[y_square_light][x_square_light] == 1:
                        text = "You can build tower there"
                    else:
                        text = "There is tower LVL " + \
                               str(towers[is_free_for_tower[y_square_light][x_square_light] - 2].level)
                        buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                        buttons.append(SellButton(screen, 860, 650, play_menu_text_surface))
                else:
                    buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                    buttons.append(SellButton(screen, 860, 650, play_menu_text_surface))
                    for button in buttons:
                        if button.is_pressed(event):
                            twr = towers[is_free_for_tower[y_square_light][x_square_light] - 2]
                            if button.type == "upgrade_button":
                                if twr.level >= 3:
                                    text = "Maximum level"
                                elif money >= twr.upgrade_price[twr.level - 1]:
                                    money -= twr.upgrade_price[twr.level - 1]
                                    twr.upgrade()
                                    text = "There is tower LVL " + str(twr.level)
                                elif money < twr.upgrade_price[twr.level - 1]:
                                    text = "Need more money"
                            if button.type == "sell_button":
                                money += twr.price / 2
                                while twr.level > 1:
                                    money += twr.upgrade_price[twr.level - 1] / 2
                                    twr.level -= 1
                                twr.sell(towers)
            if event.button == 3:
                x_square_light = event.pos[0] // SIDE
                y_square_light = event.pos[1] // SIDE
                if money < 100:
                    text = "Not enough money"
                elif is_free_for_tower[y_square_light][x_square_light] != 1:
                    text = "You can't build tower there"
                else:
                    text = "There is tower LVL " + str(1)
                    tower = Tower1(screen, event.pos[0], event.pos[1])
                    if tower.x != None and money >= 100:
                        towers.append(tower)
                        buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                        buttons.append(SellButton(screen, 860, 650, play_menu_text_surface))
                        money -= 100
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
        elif event.type == pygame.QUIT:
            finished = True
    if x_square_light != -1:
        pygame.draw.polygon(screen, GREEN, ((x_square_light*SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE + SIDE),
                                            (x_square_light*SIDE, y_square_light*SIDE + SIDE)), 1)
    if rnd.randint(1, 30) == 1:
        enemy = Enemy1(screen, 0, 300, time)
        enemies.append(enemy)
    for enemy in enemies:
        if enemy.x < 1025:
            enemy.move()
            enemy.draw(time)
    for tower in towers:
        tower.draw()
        if time % tower.speed == 0:
            money = tower.shoot(enemies, money)
    fortress.hit(enemies)
    if not fortress.alive_or_not():
        finished = True

    time += Delta_t
    screen.blit(play_menu_surface, play_menu_rect)
    screen.blit(play_menu_text_surface.render(text, True, BLACK), (100, 675))
    for button in buttons:
        button.draw()
    fortress.draw()
    pygame.display.update()

pygame.quit()


