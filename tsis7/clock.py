import pygame
import datetime

pygame.init()
sc = pygame.display.set_mode((829, 836))
bg = pygame.image.load(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\images\main-clock.png")
bg_rect = bg.get_rect(center=(829 // 2, 836 // 2))
left_hand = pygame.image.load(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\images\left-hand.png")
left_hand_rect = left_hand.get_rect(center=(829 // 2, 836 // 2))
right_hand = pygame.image.load(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\images\right-hand.png")
right_hand = pygame.transform.scale(right_hand, (right_hand.get_width() * 1.2, right_hand.get_height() * 1.2))
right_hand_rect = right_hand.get_rect(center=(829 // 2, 836 // 2))

check = True
angel_s = 0
angel_m = 0
while check:
    t = datetime.datetime.now()
    minute, second = t.minute, t.second
    angel_s = second * (-6) + 90
    angel_m = minute * (-6) + 80
    sc.fill('black')
    sc.blit(bg, bg_rect)
    rotated_lh = pygame.transform.rotate(left_hand, angel_s)
    rotated_lh_rect = rotated_lh.get_rect(center=(829 // 2, 836 // 2))
    rotated_rh = pygame.transform.rotate(right_hand, angel_m)
    rotated_rh_rect = rotated_rh.get_rect(center=(829 // 2, 836 // 2))
    sc.blit(rotated_lh, rotated_lh_rect)
    sc.blit(rotated_rh, rotated_rh_rect)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
    pygame.display.update()
