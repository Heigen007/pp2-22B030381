import pygame
import os

pygame.init()
sc = pygame.display.set_mode((1, 1), pygame.NOFRAME)
pygame.mixer.music.load(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\musics\Red Hot Chili Peppers — Can't Stop.mp3")
pygame.mixer.music.play()
check = True
p = False
play_list = os.listdir(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\musics")
while check:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
            elif event.key == pygame.K_SPACE:
                p = not p
                if p:
                    pygame.mixer.music.pause()
                elif not p:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.load(fr"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\musics\{play_list[0]}")
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.load(fr"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\musics\{play_list[1]}")
                pygame.mixer.music.play()
