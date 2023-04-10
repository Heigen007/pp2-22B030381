import pygame
import math

def draw_triangle(start_pos, end_pos, sc, color):
    point1 = start_pos
    point2 = (end_pos[0], start_pos[1])
    point3 = (start_pos[0] + (end_pos[0] - start_pos[0]) // 2, end_pos[1])
    sc.fill('black')
    pygame.draw.polygon(sc, color, [point1, point2, point3], 0)


def draw_e_triangle(start_pos, end_pos, sc, color):
    side_length = int(math.sqrt((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2))
    height = int(math.sqrt(3) * side_length / 2)

    point1 = start_pos
    point2 = (start_pos[0] + side_length, start_pos[1])
    point3 = (start_pos[0] + side_length // 2, start_pos[1] - height)

    sc.fill('black')
    pygame.draw.polygon(sc, color, [point1, point2, point3], 0)
