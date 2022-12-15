import random as rnd
from Textures import *
from Buttons import *
from Classes import *
from Main_menu import *
import Common_list


def arrow_check(x_square_light, y_square_light, stage, active_tower):
    if Common_list.is_free_for_tower[stage - 1][y_square_light][x_square_light] == 0 or \
            Common_list.abv[stage - 1][y_square_light][x_square_light] == 3 or \
            {Common_list.abv[stage - 1][y_square_light][x_square_light], \
             Common_list.abv[stage - 1][min(14, y_square_light + 1)][x_square_light], \
             Common_list.abv[stage - 1][min(14, y_square_light + 1)][min(29, x_square_light + 1)], \
             Common_list.abv[stage - 1][y_square_light][min(29, x_square_light + 1)]}.intersection({7, 8}) != set():
        flag_build = False
        flag_tower = False
        active_tower = None
        text = "You can't build tower there"
    elif Common_list.is_free_for_tower[stage - 1][y_square_light][x_square_light] == 1:
        flag_build = True
        flag_tower = False
        active_tower = None
        text = "You can build tower there"
    else:
        flag_build = False
        flag_tower = True
        active_tower = Common_list.towers[
            Common_list.is_free_for_tower[stage - 1][y_square_light][x_square_light] - 2]
        text = "There is tower LVL " + str(active_tower.level)
    return flag_build, flag_tower, text, active_tower


def game_process(text_font, stage, clock, FPS):
    finished = False
    loose = False
    win = False
    fortress = Fortress(screen)
    Common_list.buttons = [QuitButton(screen, 1100, 0, text_font)]
    Common_list.enemies = []
    number_of_enemies = 0
    Common_list.towers = []
    Common_list.bullets = []
    money = 200
    time = 0
    Delta_t = 1
    x_square_light = 21
    y_square_light = 7
    active_tower = None
    flag_build = False
    flag_tower = False
    play_menu_text_surface = pygame.font.SysFont('Comic Sans MS', 30, True)
    text = "You can't build tower there"
    time_move = 0
    type_move = ""
    flag_move = False
    generate_textures()
    generate_road()

    while not finished:
        screen.fill(WHITE)
        textures(stage)
        clock.tick(FPS)
        flag_move = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in Common_list.buttons:
                    if button.is_pressed(event):
                        if button.type == "quit_button":
                            finished = True
                if event.button == 1 or event.button == 3:
                    if event.pos[1] < 600:
                        active_tower = None
                        if (Common_list.boards[stage-1][0][0] <= event.pos[0] // SIDE <= Common_list.boards[stage-1][0][1]) and\
                           (Common_list.boards[stage-1][1][0] <= event.pos[1] // SIDE <= Common_list.boards[stage-1][1][1]):
                            x_square_light = event.pos[0] // SIDE
                            y_square_light = event.pos[1] // SIDE
                        flag_build, flag_tower, text, active_tower = arrow_check(x_square_light, y_square_light, stage, active_tower)
                    else:
                        erase_useless_buttons(text_font)
                        if flag_build:
                            Common_list.buttons.append(BuildButton1(screen, 600, 650, play_menu_text_surface))
                            Common_list.buttons.append(BuildButton2(screen, 890, 650, play_menu_text_surface))
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
                                    flag_build = True
                                    flag_tower = False
                                    active_tower = None
                                if button.type == "build_button_1":
                                    flag_build = False
                                    flag_tower = True
                                    money, text, active_tower = button.build_initiation(money, screen, x_square_light,
                                                                          y_square_light, button,
                                                                          play_menu_text_surface, stage, active_tower)
                                if button.type == "build_button_2":
                                    flag_build = False
                                    flag_tower = True
                                    money, text, active_tower = button.build_initiation(money, screen, x_square_light,
                                                                                        y_square_light, button,
                                                                                        play_menu_text_surface, stage,
                                                                                        active_tower)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finished = True
                elif event.key == pygame.K_UP:
                    flag_move = True
                    y_square_light = max(y_square_light-1, Common_list.boards[stage-1][1][0])
                elif event.key == pygame.K_DOWN:
                    flag_move = True
                    y_square_light = min(y_square_light+1, Common_list.boards[stage-1][1][1])
                elif event.key == pygame.K_LEFT:
                    flag_move = True
                    x_square_light = max(x_square_light-1, Common_list.boards[stage-1][0][0])
                elif event.key == pygame.K_RIGHT:
                    flag_move = True
                    x_square_light = min(x_square_light+1, Common_list.boards[stage-1][0][1])
                active_tower = None
                flag_build, flag_tower, text, active_tower = arrow_check(x_square_light, y_square_light, stage, active_tower)
                erase_useless_buttons(text_font)
                if flag_build:
                    Common_list.buttons.append(BuildButton1(screen, 600, 650, play_menu_text_surface))
                    Common_list.buttons.append(BuildButton2(screen, 890, 650, play_menu_text_surface))
                elif flag_tower:
                    Common_list.buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
                    Common_list.buttons.append(SellButton(screen, 900, 650, play_menu_text_surface))
                if event.key == pygame.K_z:
                    for button in Common_list.buttons:
                        if button.type == "upgrade_button":
                            if Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] > 1:
                                twr = Common_list.towers[Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                                money, text = button.upgrade_initiation(twr, money)
                        if button.type == "build_button_1":
                            flag_build = False
                            flag_tower = True
                            money, text, active_tower = button.build_initiation(money, screen, x_square_light, y_square_light,
                                                            button, play_menu_text_surface, stage, active_tower)
                elif event.key == pygame.K_x:
                    for button in Common_list.buttons:
                        if button.type == "sell_button":
                            twr = Common_list.towers[Common_list.is_free_for_tower[stage-1][y_square_light][x_square_light] - 2]
                            money += twr.price / 2
                            while twr.level > 1:
                                money += twr.upgrade_price[twr.level - 2] / 2
                                twr.level -= 1
                            money += 50
                            twr.level -= 1
                            twr.sell(stage)
                            text = "You can build tower there"
                            flag_build = True
                            flag_tower = False
                            active_tower = None
                        if button.type == "build_button_2":
                            flag_build = False
                            flag_tower = True
                            money, text, active_tower = button.build_initiation(money, screen, x_square_light, y_square_light,
                                                            button, play_menu_text_surface, stage, active_tower)
            
            elif event.type == pygame.QUIT:
                finished = True
            
        if pygame.key.get_pressed()[pygame.K_UP] and not flag_move:
            if type_move != "UP":
                time_move = 0
                type_move = "UP"
            time_move += 1
            if (time_move <= 30 and time_move % 10 == 0) or\
               (30 < time_move <= 60 and time_move % 5 == 0) or\
               (60 < time_move and time_move % 2 == 0):
                y_square_light = max(y_square_light-1, Common_list.boards[stage-1][1][0])
                flag_build, flag_tower, text, active_tower = arrow_check(x_square_light, y_square_light, stage,
                                                                         active_tower)
        elif pygame.key.get_pressed()[pygame.K_DOWN] and not flag_move:
            if type_move != "DOWN":
                time_move = 0
                type_move = "DOWN"
            time_move += 1
            if (time_move <= 30 and time_move % 10 == 0) or\
               (30 < time_move <= 60 and time_move % 5 == 0) or\
               (60 < time_move and time_move % 2 == 0):
                y_square_light = min(y_square_light+1, Common_list.boards[stage-1][1][1])
                flag_build, flag_tower, text, active_tower = arrow_check(x_square_light, y_square_light, stage,
                                                                         active_tower)
        elif pygame.key.get_pressed()[pygame.K_LEFT] and not flag_move:
            if type_move != "LEFT":
                time_move = 0
                type_move = "LEFT"
            time_move += 1
            if (time_move <= 30 and time_move % 10 == 0) or\
               (30 < time_move <= 60 and time_move % 5 == 0) or\
               (60 < time_move and time_move % 2 == 0):
                x_square_light = max(x_square_light-1, Common_list.boards[stage-1][0][0])
                flag_build, flag_tower, text, active_tower = arrow_check(x_square_light, y_square_light, stage,
                                                                         active_tower)
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and not flag_move:
            if type_move != "RIGHT":
                time_move = 0
                type_move = "RIGHT"
            time_move += 1
            if (time_move <= 30 and time_move % 10 == 0) or\
               (30 < time_move <= 60 and time_move % 5 == 0) or\
               (60 < time_move and time_move % 2 == 0):
                x_square_light = min(x_square_light+1, Common_list.boards[stage-1][0][1])
                flag_build, flag_tower, text, active_tower = arrow_check(x_square_light, y_square_light, stage,
                                                                         active_tower)
        else:
            time_move = 0
            type_move = ""
        
        erase_useless_buttons(text_font)
        if flag_build:
            Common_list.buttons.append(BuildButton1(screen, 600, 650, play_menu_text_surface))
            Common_list.buttons.append(BuildButton2(screen, 890, 650, play_menu_text_surface))
        elif flag_tower:
            Common_list.buttons.append(UpgradeButton(screen, 600, 650, play_menu_text_surface))
            Common_list.buttons.append(SellButton(screen, 900, 650, play_menu_text_surface))

        pygame.draw.polygon(screen, GREEN, ((x_square_light*SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE),
                                            (x_square_light*SIDE + SIDE, y_square_light*SIDE + SIDE),
                                            (x_square_light*SIDE, y_square_light*SIDE + SIDE)), 1)
        
        random_number = rnd.randint(0, 10000)
        p = e**(-4 + 1 / (0.8 * maximum_of_enemies[stage - 1]) * number_of_enemies)
        if random_number < p * 10000 / 2.5 and number_of_enemies < 0.8 * maximum_of_enemies[stage - 1]:
            if random_number < p * 10000 / 5:
                enemy = Enemy1(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time, stage)
            else:
                enemy = Enemy1(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time, stage)
            Common_list.enemies.append(enemy)
            number_of_enemies += 1
        elif random_number < p * 20000 / 2.5 and number_of_enemies < 0.8 * maximum_of_enemies[stage - 1]:
            if random_number < p * 10000 * 3 / 5:
                enemy = Enemy4(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time, stage)
            else:
                enemy = Enemy4(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time, stage)
            Common_list.enemies.append(enemy)
            number_of_enemies += 1
        elif random_number < p * 10000 and number_of_enemies < 0.8 * maximum_of_enemies[stage - 1]:
            if random_number < p * 10000 * 9 / 10:
                enemy = Enemy2(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time, stage)
            else:
                enemy = Enemy2(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time, stage)
            Common_list.enemies.append(enemy)
            number_of_enemies += 1
        elif random_number < 1000 and 0.8 * maximum_of_enemies[stage - 1] <= number_of_enemies < maximum_of_enemies[stage - 1]:
            if random_number < 1000 / 3:
                if random_number < p * 1000 / 6:
                    enemy = Enemy1(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time, stage)
                else:
                    enemy = Enemy1(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time, stage)
                Common_list.enemies.append(enemy)
                number_of_enemies += 1
            elif random_number < 1000 * 2 / 3:
                if random_number < p * 1000 / 2:
                    enemy = Enemy4(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time, stage)
                else:
                    enemy = Enemy4(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time, stage)
                Common_list.enemies.append(enemy)
                number_of_enemies += 1
            else:
                if random_number < p * 1000 * 5 / 6:
                    enemy = Enemy2(screen, start_positions[stage - 1][2], start_positions[stage - 1][0], time, stage)
                else:
                    enemy = Enemy2(screen, start_positions[stage - 1][2], start_positions[stage - 1][1], time, stage)
                Common_list.enemies.append(enemy)
                number_of_enemies += 1

        if active_tower:
            pygame.draw.circle(screen, GREEN, (active_tower.x, active_tower.y), active_tower.radius, 3)

        fortress.draw()

        for enemy in Common_list.enemies:
            enemy.move(stage)
            enemy.draw(time)

        for tower in sorted(Common_list.towers, key = lambda x: x.y):
            if tower.type == 1:
                if tower.t <= 0:
                    tower.shoot()
                    if tower.attacked_enemy:
                        tower.t = tower.speed
                tower.t -= 1
            if tower.type == 2:
                money = tower.shoot(money)
            tower.draw()
        
        for bullet in Common_list.bullets:
            money = bullet.hit_enemies(money)
        for bullet in Common_list.bullets:
            bullet.draw_and_move()
        
        fortress.hit()
        if not fortress.alive_or_not():
            finished = True
            loose = True
        if len(Common_list.enemies) == 0  and number_of_enemies >= maximum_of_enemies[stage - 1]:
            finished = True
            win = True
        time += Delta_t
        screen.blit(play_menu_surface, play_menu_rect)
        screen.blit(play_menu_text_surface.render(text, True, BLACK), (100, 675))
        for button in Common_list.buttons:
            button.draw()
        screen.blit(text_font.render("Money: " + str(int(money)) + ", Enemies: " + str(number_of_enemies), True, (0, 0, 0)), (10, 10))
        #screen.blit(text_font.render("FPS: " + str(int(clock.get_fps())), True, (0, 0, 0)), (500, 10))
        pygame.display.update()
    return finished, loose, win
