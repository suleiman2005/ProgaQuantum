from Classes import *
from Buttons import *
import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main_menu(text_font, clock, FPS):
    game_level = 0
    main_menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))

    buttons = [StartButton(main_menu_screen, 500, 200, text_font), ExitButton(main_menu_screen, 500, 700, text_font),
               SelectButton1(main_menu_screen, 550, 400, text_font),
               SelectButton2(main_menu_screen, 550, 500, text_font),
               SelectButton3(main_menu_screen, 550, 600, text_font)]

    intro = True
    while intro:
        main_menu_screen.fill((255, 255, 0))
        clock.tick(FPS)
        main_menu_screen.blit(text_font.render("TOWER DEFENCE", True, BLACK), (300, 100))
        main_menu_screen.blit(text_font.render("Select Level", True, BLACK), (500, 300))
        for button in buttons:
            if button.type == "start_button" and game_level == 0:
                pass
            elif button.type == "level1_button" and game_level == 1:
                button.draw(RED)
            elif button.type == "level2_button" and game_level == 2:
                button.draw(RED)
            elif button.type == "level3_button" and game_level == 3:
                button.draw(RED)
            else:
                button.draw(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        if button.is_pressed(event):
                            if button.type == "exit_button":
                                pygame.quit()
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
        pygame.display.update()
    return game_level


def game_over(text_font, clock, FPS):
    game_over_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_over_font = pygame.font.Font(None, 75)
    buttons = [ExitToMainMenuButton(game_over_screen, 500, 500, text_font), ExitButton(game_over_screen, 500, 600, text_font)]
    game_over_parameter = True

    while game_over_parameter:
        game_over_screen.fill(BLACK)
        clock.tick(FPS)
        game_over_screen.blit(game_over_font.render("YOU DEAD", True, RED), (400, 200))
        for button in buttons:
            button.draw(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        if button.is_pressed(event):
                            if button.type == "exit_button":
                                pygame.quit()
                            if button.type == "start_button":
                                game_over_parameter = False

        pygame.display.update()