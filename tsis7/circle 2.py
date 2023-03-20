import pygame

pygame.init()
sc = pygame.display.set_mode((600, 400))
check = True
x, y = 300, 200
x_m = 0
y_m = 0
flup, flrigth, flleft, fldown = False, False, False, False
clock = pygame.time.Clock()
while check:
    sc.fill('white')
    pygame.draw.circle(sc, 'red', (x, y), 25)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
            elif event.key == pygame.K_w:
                flup = True

            elif event.key == pygame.K_a:
                flleft = True

            elif event.key == pygame.K_s:
                fldown = True

            elif event.key == pygame.K_d:
                flrigth = True

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                flup, flrigth, flleft, fldown = False, False, False, False

    if flrigth and x < 580:
        x += 20
    if flleft and x > 20:
        x -= 20
    if fldown and y < 380:
        y += 20
    if flup and y > 20:
        y -= 20

    pygame.display.update()

    clock.tick(45)
