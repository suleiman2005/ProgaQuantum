from Game_process import *

FPS = 60
pygame.init()
text_font = pygame.font.SysFont('Comic Sans MS', 24, True)
clock = pygame.time.Clock()
finished = False
lose = False
win = False

while not finished and not lose and not win:
    stage = main_menu(text_font, clock, FPS, lose)
    finished, lose, win = game_process(text_font, stage, clock, FPS)
    if lose:
        lose = game_over(text_font, clock, FPS, lose)
        if not lose:
            finished = False
    if win:
        win = winning(text_font, clock, FPS)
        if not win:
            finished = False
pygame.quit()
