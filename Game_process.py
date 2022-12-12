import random as rnd
from Textures import *
from Buttons import *
from Classes import *
from Main_menu import *
from Common_list import *

def game_process(text_font, stage, clock, FPS):
    finished = False
    loose = False
    fortress = Fortress(screen)
    Common_list.buttons = [QuitButton(screen, 1100, 0, text_font)]
    Common_list.enemies = []
    Common_list.towers = []
    Common_list.bullets = []
    money = 200
    time = 0
    Delta_t = 1
    x_square_light = -1
    y_square_light = -1
    active_tower = None
    flag_build = False
    flag_tower = False
    play_menu_text_surface = pygame.font.SysFont('Comic Sans MS', 30, True)
    text = ""
    generate_textures()
    generate_road()

    while not finished:
        screen.fill(WHITE)
        textures(stage)
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                erase_useless_buttons()
                for button in Common_list.buttons:
                    if button.is_pressed(event):
                        if button.type == "quit_button":
                            finished = True
                if event.button == 1 or event.button == 3:
                    erase_useless_buttons()
                    if event.pos[1] < 600:
                        active_tower = None
                        x_square_light = event.pos[0] // SIDE
                        y_square_light = event.pos[1] // SIDE
                        if Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] == 0 or Common_list.abv[stage-1][y_square_light][x_square_light] == 3 or\
                           {Common_list.abv[stage-1][y_square_light][x_square_light],\
                            Common_list.abv[stage-1][min(14, y_square_light+1)][x_square_light],\
                            Common_list.abv[stage-1][min(14, y_square_light+1)][min(29, x_square_light+1)],\
                            Common_list.abv[stage-1][y_square_light][min(29, x_square_light+1)]}.intersection({7,8}) != set():
                            flag_build = False
                            flag_tower = False
                            text = "You can't build tower there"
                        elif Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] == 1:
                            flag_build = True
                            flag_tower = False
                            text = "You can build tower there"
                            Common_list.buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))
                        else:
                            flag_build = False
                            flag_tower = True
                            active_tower = Common_list.towers[Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                            text = "There is tower LVL " + \
                                   str(active_tower.level)
                            Common_list.buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                            Common_list.buttons.append(SellButton(screen, 900, 650, play_menu_text_surface))
                    else:
                        if flag_build:
                            Common_list.buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))
                        elif flag_tower:
                            Common_list.buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                            Common_list.buttons.append(SellButton(screen, 900, 650, play_menu_text_surface))
                        for button in Common_list.buttons:
                            if button.is_pressed(event):
                                if button.type == "upgrade_button":
                                    twr = Common_list.towers[Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                                    money, text = button.upgrade_initiation(twr, money)
                                if button.type == "sell_button":
                                    twr = Common_list.towers[Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                                    money += twr.price / 2
                                    while twr.level > 1:
                                        money += twr.upgrade_price[twr.level - 1] / 2
                                        twr.level -= 1
                                    twr.sell(stage)
                                    text = "You can build tower there"
                                    erase_useless_buttons()
                                    Common_list.buttons.remove(button)
                                    Common_list.buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))
                                if button.type == "build_button":
                                    money, text, active_tower = button.build_initiation(money, screen, x_square_light,
                                                                          y_square_light, button,
                                                                          play_menu_text_surface, stage, active_tower)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finished = True
                elif event.key == pygame.K_z:
                    for button in Common_list.buttons:
                        if button.type == "upgrade_button":
                            if Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] > 1:
                                twr = Common_list.towers[Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                                money, text = button.upgrade_initiation(twr, money)
                        if button.type == "build_button":
                            money, text, active_tower = button.build_initiation(money, screen, x_square_light, y_square_light,
                                                            button, play_menu_text_surface, stage, active_tower)
                elif event.key == pygame.K_x:
                    for button in Common_list.buttons:
                        if button.type == "sell_button":
                            twr = Common_list.towers[Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                            money += twr.price / 2
                            while twr.level > 1:
                                money += twr.upgrade_price[twr.level - 1] / 2
                                twr.level -= 1
                            twr.sell(stage)
                            text = "You can build tower there"
                            erase_useless_buttons()
                            Common_list.buttons.remove(button)
                            Common_list.buttons.append(BuildButton(screen, 600, 650, play_menu_text_surface))

            elif event.type == pygame.QUIT:
                finished = True

        if x_square_light != -1:
            pygame.draw.polygon(screen, GREEN, ((x_square_light*SIDE, y_square_light*SIDE),
                                                (x_square_light*SIDE + SIDE, y_square_light*SIDE),
                                                (x_square_light*SIDE + SIDE, y_square_light*SIDE + SIDE),
                                                (x_square_light*SIDE, y_square_light*SIDE + SIDE)), 1)
        random_number = rnd.randint(1, 100)
        if random_number == 1:
            enemy = Enemy1(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time)
            Common_list.enemies.append(enemy)
        elif random_number == 100:
            enemy = Enemy1(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time)
            Common_list.enemies.append(enemy)

        random_number = rnd.randint(1, 1000)
        if random_number == 1:
            enemy = Enemy2(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time)
            Common_list.enemies.append(enemy)
        elif random_number == 100:
            enemy = Enemy2(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time)
            Common_list.enemies.append(enemy)
        for enemy in Common_list.enemies:
            enemy.move(stage)
            enemy.draw(time)

        for tower in Common_list.towers:
            tower.draw()
            if tower.t <= 0:
                tower.shoot()
                if tower.attacked_enemy:
                    tower.t = tower.speed
            tower.t -= 1
        if active_tower:
            pygame.draw.circle(screen, GREEN, (active_tower.x, active_tower.y), active_tower.radius, 3)
        for bullet in Common_list.bullets:
            bullet.draw_and_move()
            money = bullet.hit_enemies(money)
        fortress.hit()
        if not fortress.alive_or_not():
            finished = True
            loose = True
        time += Delta_t
        screen.blit(play_menu_surface, play_menu_rect)
        screen.blit(play_menu_text_surface.render(text, True, BLACK), (100, 675))
        draw_clouds(stage)
        for button in Common_list.buttons:
            button.draw()
        fortress.draw()
        screen.blit(text_font.render("Money " + str(int(money)), True, (0, 0, 0)), (10, 10))
        screen.blit(text_font.render("FPS: " + str(int(clock.get_fps())), True, (0, 0, 0)), (500, 10))
        pygame.display.update()
    return finished, loose
