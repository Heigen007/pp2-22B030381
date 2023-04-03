import random

import pygame
from random import *

pygame.init()
sc = pygame.display.set_mode((400, 600))
speed = 5
x = 165
y_c = 0
x_c = randint(0, 340)
f = pygame.font.SysFont('arial', 30)
score = 0
clock = pygame.time.Clock()
car = pygame.image.load(r"images\toppng.com-toy-car-top-view-2400x1190.png").convert_alpha()
car = pygame.transform.scale(car, (car.get_width() // 6, car.get_height() // 6))
car = pygame.transform.rotate(car, 90)
# car_cent = car.get_rect(center=(x, 525))
road = pygame.image.load(r"images\—Pngtree—asphalt road plane material display_2941722.png")
road_cent = road.get_rect(center=(200, 300))
coin = pygame.image.load(r"images\pngegg (1).png")
coin_half = pygame.transform.scale(coin, (coin.get_width() // 40, coin.get_height() // 40))
coin_full = pygame.transform.scale(coin, (coin.get_width() // 25, coin.get_height() // 25))
check = True
flright = False
flleft = False
coin_s = choice([0.5, 1])
if coin_s == 0.5:
    coin = coin_half
if coin_s == 1:
    coin = coin_full

while check:
    sc.fill('white')
    sc.blit(road, road_cent)
    sc.blit(coin, (x_c, y_c))
    sc.blit(car, (x, 460))
    score_table = f.render(str(score), True, 'red')
    sc.blit(score_table, (0, 0))
    if y_c > 600:
        check = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
            if event.key == pygame.K_a:
                flleft = True

            if event.key == pygame.K_d:
                flright = True

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                flright, flleft = False, False,

    if x_c + 60 >= x + 35 >= x_c and 600 >= y_c >= 410:
        y_c = 0
        x_c = randint(0, 340)
        score += coin_s
        coin_s = choice([0.5, 1])
        if coin_s == 0.5:
            coin = coin_half
        if coin_s == 1:
            coin = coin_full
        if score % 3 == 0 and score != 0:
            speed += 2
        elif (score - 0.5) % 3 == 0 and (score - 0.5) != 0:
            speed += 2
    if flright and x < 330:
        x += 10
    if flleft and x > 0:
        x -= 10
    y_c += speed
    pygame.display.update()
    clock.tick(60)
pygame.quit()