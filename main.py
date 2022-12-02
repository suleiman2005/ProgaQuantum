import pygame

from Textures import *
from Buttons import *
from Classes import *
import random as rnd


def erase_useless_buttons(buttons):
    """функция стирающая ненужные в некоторый момент кнопки"""
    for button in buttons:
        if button.type == "upgrade_button":
            buttons.remove(button)


FPS = 60
WIDTH = 1200
HEIGHT = 800

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
    for a in range(15):
        for b in range(30):
            if abv[a][b] == 1:
                i = grass_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(grass_surf, i)
            elif abv[a][b] == 0:
                i = road_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(road_surf, i)



    clock.tick(FPS)
    screen.blit(text_font.render("Money " + str(int(money)), True, (0, 0, 0)), (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_pressed(event):
                    if button.type == "quit_button":
                        finished = True
            if event.button == 1:
                if event.pos[1] < 600:
                    x_square_light = event.pos[0] // SIDE
                    y_square_light = event.pos[1] // SIDE
                    if is_free_for_tower[y_square_light][x_square_light] == 0:
                        text = "You can't build tower there"
                        erase_useless_buttons(buttons)
                    elif is_free_for_tower[y_square_light][x_square_light] == 1:
                        text = "You can build tower there"
                        erase_useless_buttons(buttons)
                    else:
                        text = "There is tower LVL " + \
                               str(towers[is_free_for_tower[y_square_light][x_square_light] - 2].level)
                        buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                else:
                    for button in buttons:
                        if button.is_pressed(event):
                            if button.type == "upgrade_button":
                                twr = towers[is_free_for_tower[y_square_light][x_square_light] - 2]
                                if money >= twr.upgrade_price[twr.level] and twr.level < 3:
                                    money -= twr.upgrade_price[twr.level]
                                    twr.upgrade()
                                    towers[is_free_for_tower[y_square_light][x_square_light] - 2] = twr
                                    text = "There is tower LVL " + \
                                           str(towers[is_free_for_tower[y_square_light][x_square_light] - 2].level)
                                else:
                                    text = "Need more money..."
            if event.button == 3:
                x_square_light = event.pos[0] // SIDE
                y_square_light = event.pos[1] // SIDE
                if money < 100:
                    text = "Not enough money"
                elif is_free_for_tower[y_square_light][x_square_light] != 1:
                    text = "You can't build tower there"
                else:
                    text = "There is tower LVL " + str(0)
                    buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                    tower = Tower1(screen, event.pos[0], event.pos[1])
                    if tower.x != None and money >= 100:
                        towers.append(tower)
                        money -= 100
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
        if event.type == pygame.QUIT:
            finished = True
    if x_square_light != -1:
        pygame.draw.polygon(screen, GREEN, ((x_square_light*SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE + SIDE),
                                            (x_square_light*SIDE, y_square_light*SIDE + SIDE)), 1)
    if rnd.randint(1, 30) == 1:
        enemy = Enemy1(screen, 0, 300)
        enemies.append(enemy)
    for enemy in enemies:
        if enemy.x < 1025:
            enemy.move()
        if time//6 == time/6:
            enemy.draw()
        else:
            enemy.draw1()
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


