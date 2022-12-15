from Classes import *
from Buttons import *
import Common_list
import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

main_back = MainBack()


def main_menu(text_font, clock, FPS, loose):
    game_level = 0
    main_menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.mixer.music.load("music/main_menu_music.mp3")
    pygame.mixer.music.play(-1)

    Common_list.buttons = [StartButton(main_menu_screen, 520, 200, text_font), ExitButton(main_menu_screen, 520, 700, text_font),
               SelectButton1(main_menu_screen, 520, 400, text_font),
               SelectButton2(main_menu_screen, 520, 500, text_font),
               SelectButton3(main_menu_screen, 520, 600, text_font)]

    intro = True
    while intro:
        main_back.draw()
        clock.tick(FPS)
        pygame.draw.rect(main_menu_screen, (164,116,73), (480, 100, 240, 50))
        main_menu_screen.blit(text_font.render("TOWER DEFENCE", True, BLACK), (490, 100))
        pygame.draw.rect(main_menu_screen, (164,116,73), (520, 300, 150, 50))
        main_menu_screen.blit(text_font.render("Select Level", True, BLACK), (520, 300))
        for button in Common_list.buttons:
            if button.type == "start_button" and game_level == 0:
                pass
            elif button.type == "level1_button" and game_level == 1:
                button.draw(WHITE)
            elif button.type == "level2_button" and game_level == 2:
                button.draw(WHITE)
            elif button.type == "level3_button" and game_level == 3:
                button.draw(WHITE)
            elif button.type == "exit_button":
                button.draw(BLACK, loose)
            else:
                button.draw(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in Common_list.buttons:
                        if button.is_pressed(event):
                            if button.type == "exit_button":
                                pygame.quit()
                                exit(0)
                            elif button.type == "start_button":
                                if game_level > 0:
                                    intro = False
                            elif button.type == "level1_button":
                                game_level = 1
                            elif button.type == "level2_button":
                                game_level = 2
                            elif button.type == "level3_button":
                                game_level = 3
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.update()
    return game_level


def game_over(text_font, clock, FPS, loose):
    game_over_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_over_font = pygame.font.Font(None, 75)
    pygame.mixer.music.pause()
    sound = pygame.mixer.Sound("music/game_over_sound.mp3")
    sound.play()
    Common_list.buttons = [ExitToMainMenuButton(game_over_screen, 500, 500, text_font), ExitButton(game_over_screen, 500, 600, text_font)]
    game_over_parameter = True
    stop_cycle = False

    while not stop_cycle and game_over_parameter:
        game_over_screen.fill(BLACK)
        clock.tick(FPS)
        game_over_label = game_over_font.render("YOU DIED", True, RED)
        game_over_screen.blit(game_over_label, (game_over_screen.get_width() / 2 - game_over_label.get_width() / 2, 200))
        for button in Common_list.buttons:
            if button.type == "exit_button":
                button.draw(WHITE, loose)
            else:
                button.draw(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_cycle = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in Common_list.buttons:
                        if button.is_pressed(event):
                            if button.type == "exit_button":
                                stop_cycle = True
                            if button.type == "start_button":
                                game_over_parameter = False
        pygame.display.update()
    return game_over_parameter


def winning(text_font, clock, FPS):
    winning_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    winning_font = pygame.font.Font(None, 75)
    pygame.mixer.music.load("music/win_music.mp3")
    pygame.mixer.music.play(-1)
    Common_list.buttons = [ExitToMainMenuButton(winning_screen, 500, 500, text_font),
                           ExitButton(winning_screen, 500, 600, text_font)]
    winning_parameter = True
    stop_cycle = False

    while not stop_cycle and winning_parameter:
        winning_screen.fill(WHITE)
        clock.tick(FPS)
        winning_label = winning_font.render("YOU WIN!!!", True, GREEN)
        winning_screen.blit(winning_label, (winning_screen.get_width() / 2 - winning_label.get_width() / 2, 200))
        for button in Common_list.buttons:
            if button.type == "exit_button":
                button.draw(BLACK, True)
            else:
                button.draw(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_cycle = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in Common_list.buttons:
                        if button.is_pressed(event):
                            if button.type == "exit_button":
                                stop_cycle = True
                            if button.type == "start_button":
                                winning_parameter = False
        pygame.display.update()
    return winning_parameter