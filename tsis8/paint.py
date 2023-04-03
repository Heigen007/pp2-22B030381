import pygame
import math
pygame.init()
sc = pygame.display.set_mode((600, 400))
check = True
check_draw = False
color = "white"
start_pos = (0, 0)
end_pps = (0, 0)
rect_flag = False
circle_flag = False
width_line = 2
eraser = pygame.image.load(
    r"images\pngimg.com - eraser_PNG15.png")
eraser = pygame.transform.scale(eraser, (100, 80))
while check:
    sc.blit(eraser, (390, 310))
    pygame.draw.circle(sc, 'red', (50, 350), 40)
    pygame.draw.circle(sc, 'blue', (150, 350), 40)
    pygame.draw.circle(sc, 'green', (250, 350), 40)
    pygame.draw.circle(sc, 'white', (350, 350), 40)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            rect_flag = True
            check_draw = False
            circle_flag = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            rect_flag = False
            check_draw = False
            circle_flag = True
        if rect_flag and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and circle_flag:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            check_draw = True
            rect_flag = False
            circle_flag = False
        if event.type == pygame.MOUSEMOTION:
            if check_draw:
                end_pos = event.pos
                pygame.draw.line(sc, color, start_pos, end_pos, width_line)
                start_pos = end_pos
            if rect_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                sc.fill('black')
                pygame.draw.rect(sc, color, pygame.Rect(x, y, width_rect, height_rect))
            if circle_flag:
                end_pos = event.pos
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]
                radius = int(math.sqrt(dx ** 2 + dy ** 2))
                cent = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(sc, color, cent, radius, 2)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            check_draw = False
            rect_flag = False
            circle_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 10 <= event.pos[0] <= 90 and 310 <= event.pos[1] <= 390:
                color = 'red'
                width_line = 2
            elif 110 <= event.pos[0] <= 190 and 310 <= event.pos[1] <= 390:
                color = "blue"
                width_line = 2
            elif 210 <= event.pos[0] <= 290 and 310 <= event.pos[1] <= 390:
                width_line = 2
                color = "green"
            elif 310 <= event.pos[0] <= 390 and 310 <= event.pos[1] <= 390:
                color = "white"
                width_line = 2
            elif 390 <= event.pos[0] <= 490 and 310 <= event.pos[1] <= 490:
                color = "black"
                width_line = 40
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            sc.fill(0)
    pygame.display.update()

pygame.quit()
