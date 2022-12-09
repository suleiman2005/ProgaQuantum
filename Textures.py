import pygame
from random import randint
import numpy as np
m = randint(3, 5)
n = randint(3, 5)
l = randint(3, 5)
k = randint(3, 5)
o = randint(5, 6)
p = randint(5, 7)


abv = [[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
       ],
       [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
       ],
       [[1,1,1,1,1,m,1,1,1,1,1,1,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,9,9,1,1,1,1,1,9,9,9,1,1,1,k,1,1,1,1,0,1],
        [1,0,9,1,1,1,1,n,1,1,1,1,1,9,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,m,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,1,1,1,1,1,1,9,0,0,0,0,0,0,0,9,1,1,6,1,1,1,1,m,n,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,0,l,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,9,1,1,1,l,1,1],
        [1,1,1,1,1,m,1,1,1,0,9,1,1,1,1,1,1,1,1,1,1,1,l,1,1,1,1,1,1,1],
        [0,0,9,1,k,1,1,1,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,o,9,1,1,1,1],
        [1,0,1,9,1,1,1,1,1,1,1,1,1,1,1,0,1,1,9,1,1,1,1,1,9,1,1,1,1,1],
        [1,0,1,1,1,1,1,1,p,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,9,1,1,1,1,1,1,1,1,1,1,1,9,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,n,1,1,1,1,1,1,1,1,1,1,1,1,1,1,n,1,1,1,1,1,1,1]
       ]
      ]

stage = 3      

grass_surf = pygame.image.load("img/t1gr.png")
grass1_surf = pygame.image.load("img/t2gr.png")
road_surf = pygame.image.load("img/t1ro.png")
cloud_surf = pygame.image.load("img/cloud.png")
ss1_surf = pygame.image.load("img/ss1.png")
ss2_surf = pygame.image.load("img/ss2.png")
ss3_surf = pygame.image.load("img/ss3.png")
stone_surf = pygame.image.load("img/stone.png")
lake_surf = pygame.image.load("img/lake.png")
enemy1_surf = pygame.image.load("img/enemy1-t.png")
enemy2_surf = pygame.image.load("img/enemy2-t.png")
fort_surf = pygame.image.load("img/mom-tower-t.png")
WIDTH = 1200
HEIGHT = 800
BULLET_SPEED = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def textures():
    for a in range(15):
        for b in range(30):
            if abv[stage-1][a][b] == 1:
                i = grass_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(grass_surf, i)
            elif abv[stage-1][a][b] == 9:
                i = grass1_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(grass1_surf, i)
            elif abv[stage-1][a][b] == 0:
                i = road_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(road_surf, i)
            elif abv[stage-1][a][b] == 3:
                i = ss1_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(ss1_surf, i)
            elif abv[stage-1][a][b] == 4:
                i = ss2_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(ss2_surf, i)
            elif abv[stage-1][a][b] == 5:
                i = ss3_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(ss3_surf, i)
            elif abv[stage - 1][a][b] == 6:
                i = stone_surf.get_rect(center=(0 + (b * 40), (a * 40) + 0))
                screen.blit(stone_surf, i)
            elif abv[stage - 1][a][b] == 7:
                i = lake_surf.get_rect(center=(0 + (b * 40), (a * 40) + 0))
                screen.blit(lake_surf, i)


def draw_bullet(x, y):
	pygame.draw.circle(screen, BLACK, (x, y), 1)

def draw_tower(x, y, z):
    if z == 0:
        tower_surf = pygame.image.load("img/test_bashnya.png")
        i = tower_surf.get_rect(center=(x, y))
        screen.blit(tower_surf, i)
    if z == 1:
        tower_surf = pygame.image.load("img/test_bashnya1.png")
        i = tower_surf.get_rect(center=(x, y))
        screen.blit(tower_surf, i)
    if z == 2:
        tower_surf = pygame.image.load("img/test_bashnya2.png")
        i = tower_surf.get_rect(center=(x, y))
        screen.blit(tower_surf, i)
    if z == 3:
        tower_surf = pygame.image.load("img/test_bashnya3.png")
        i = tower_surf.get_rect(center=(x, y))
        screen.blit(tower_surf, i)

def draw_enemy(enemy, time):
    #if float((time - time_creation)//100) == float((time - time_creation)/100):
    #       pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)
    change = time - enemy.time_creation
    if change//40 == change/40:
        enemy.tik *= -1
    if enemy.tik == 1:
        #pygame.draw.circle(enemy.screen, (255, 0, 0), (enemy.x, enemy.y), 10)
        i = enemy1_surf.get_rect(center=( (enemy.x), (enemy.y) ))
        screen.blit(enemy1_surf, i)
    if enemy.tik == -1:
        #pygame.draw.circle(enemy.screen, (0, 255, 0), (enemy.x, enemy.y), 10)
        i = enemy2_surf.get_rect(center=(  (enemy.x), (enemy.y)  ))
        screen.blit(enemy2_surf, i)
def draw_fort(fort):
    i = fort_surf.get_rect(center=((860), (290)))
    screen.blit(fort_surf, i)

