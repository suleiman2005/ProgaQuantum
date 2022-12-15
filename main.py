from Game_process import *

FPS = 60
pygame.init()
text_font = pygame.font.SysFont('Comic Sans MS', 24, True)
clock = pygame.time.Clock()
finished = False
loose = False

while not finished and not loose:
    stage = main_menu(text_font, clock, FPS, loose)
    finished, loose = game_process(text_font, stage, clock, FPS)
    if loose:
        loose = game_over(text_font, clock, FPS, loose)
        if not loose:
            finished = False
pygame.quit()
