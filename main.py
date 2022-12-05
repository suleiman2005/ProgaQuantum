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
money = 200
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
                    if is_free_for_tower[stage-1][y_square_light][x_square_light] == 0:
                        text = "You can't build tower there"
                    elif is_free_for_tower[stage-1][y_square_light][x_square_light] == 1:
                        text = "You can build tower there"
                        buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))
                    else:
                        text = "There is tower LVL " + \
                               str(towers[is_free_for_tower[stage-1][y_square_light][x_square_light] - 2].level)
                        buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                        buttons.append(SellButton(screen, 900, 650, play_menu_text_surface))
                else:
                    if is_free_for_tower[stage-1][y_square_light][x_square_light] == 1:
                        buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))
                    elif is_free_for_tower[stage-1][y_square_light][x_square_light] > 1:
                        buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                        buttons.append(SellButton(screen, 900, 650, play_menu_text_surface))
                    for button in buttons:
                        if button.is_pressed(event):
                            if button.type == "upgrade_button":
                                twr = towers[is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                                money, text = button.upgrade_initiation(twr, money)
                            if button.type == "sell_button":
                                twr = towers[is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                                money += twr.price / 2
                                while twr.level > 1:
                                    money += twr.upgrade_price[twr.level - 1] / 2
                                    twr.level -= 1
                                twr.sell(towers)
                                text = "You can build tower there"
                                erase_useless_buttons(buttons)
                                buttons.remove(button)
                                buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))
                            if button.type == "build_button":
                                money, text = button.build_initiation(money, towers, screen, x_square_light,
                                                                      y_square_light, buttons, button,
                                                                      play_menu_text_surface)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
            elif event.key == pygame.K_z:
                for button in buttons:
                    if button.type == "upgrade_button":
                        if is_free_for_tower[stage-1][y_square_light][x_square_light] > 1:
                            twr = towers[is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                            money, text = button.upgrade_initiation(twr, money)
                    if button.type == "build_button":
                        money, text = button.build_initiation(money, towers, screen, x_square_light, y_square_light, buttons,
                                                        button, play_menu_text_surface)
            elif event.key == pygame.K_x:
                for button in buttons:
                    if button.type == "sell_button":
                        twr = towers[is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                        money += twr.price / 2
                        while twr.level > 1:
                            money += twr.upgrade_price[twr.level - 1] / 2
                            twr.level -= 1
                        twr.sell(towers)
                        text = "You can build tower there"
                        erase_useless_buttons(buttons)
                        buttons.remove(button)
                        buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))

        elif event.type == pygame.QUIT:
            finished = True

    if x_square_light != -1:
        pygame.draw.polygon(screen, GREEN, ((x_square_light*SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE + SIDE),
                                            (x_square_light*SIDE, y_square_light*SIDE + SIDE)), 1)
    random_number = rnd.randint(1, 100)
    if random_number == 1:
        enemy = Enemy1(screen, 0, 220, time)
        enemies.append(enemy)
    elif random_number == 100:
        enemy = Enemy1(screen, 0, 380, time)
        enemies.append(enemy)
    for enemy in enemies:
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


