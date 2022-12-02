import pygame
import numpy as np

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

abv = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
      ]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


grass_surf = pygame.image.load("img/grass.png")
road_surf = pygame.image.load("img/road.png")
def textures():
       for a in range(15):
              for b in range(30):
                     if abv[a][b] == 1:
                            i = grass_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                            screen.blit(grass_surf, i)
                     elif abv[a][b] == 0:
                            i = road_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                            screen.blit(road_surf, i)

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
              pygame.draw.circle(enemy.screen, (255, 0, 0), (enemy.x, enemy.y), 10)
       if enemy.tik == -1:
              pygame.draw.circle(enemy.screen, (0, 255, 0), (enemy.x, enemy.y), 10)