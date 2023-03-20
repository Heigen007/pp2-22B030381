import pygame

pygame.init()
sc = pygame.display.set_mode((600, 400))
check = True
x, y = 300, 200
x_m = 0
y_m = 0
while check:
    sc.fill('white')
    pygame.draw.circle(sc, 'red', (x, y), 25)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
            elif event.key == pygame.K_w and y > 20:
                x_m = 0
                y_m = -20
            elif event.key == pygame.K_a and x > 20:
                x_m = -20
                y_m = 0
            elif event.key == pygame.K_s and y < 380:
                y_m = 20
                x_m = 0
            elif event.key == pygame.K_d and x < 580:
                x_m = 20
                y_m = 0

    x += x_m
    y += y_m
    y_m = 0
    x_m = 0
    pygame.display.update()
