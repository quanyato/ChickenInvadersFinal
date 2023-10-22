import pygame
import os
import sys
import button
from display_on_screen import display_setting

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614

pygame.display.set_caption('Chicken Invaders')
#background_image = pygame.image.load('image/bg.jpg').convert()
game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

back_image = pygame.image.load('image/back.png')
bg_image = pygame.image.load("image/back_loop.jpg").convert_alpha()
bg_height = bg_image.get_height()
back_scroll_speed=0
def draw_background():
    global back_scroll_speed
    for x in range (2):
        game_screen.blit(bg_image, (0, ((-x * bg_height)-back_scroll_speed)))

b1_image = pygame.transform.scale(pygame.image.load('image/btn_1.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//10))
b2_image = pygame.transform.scale(pygame.image.load('image/btn_2.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//10))
b3_image = pygame.transform.scale(pygame.image.load('image/btn_3.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//10))
sound = pygame.mixer.Sound('music/aov_song.wav')
music_one_time = True   # chạy nhạc 1 lần

run=True
back_button = button.Button(20,15,back_image)
b1 = button.Button(70,300,b1_image)
b2 = button.Button(370,300,b2_image)
b3 = button.Button(670,300,b3_image)
#============================================================================================
def level1():
    with open("setting_imformation",'w') as file:     # doc file
        file.write('10')
def level2():
    with open("setting_imformation",'w') as file:     # doc file
        file.write('20')
def level3():
    with open("setting_imformation",'w') as file:     # doc file
        file.write('30')


#=========================================================================
while run:

    draw_background()
    back_scroll_speed -= 0.1
    if abs(back_scroll_speed) > bg_height:
        back_scroll_speed=0
    
    if music_one_time:
        sound.play()
        music_one_time = False
    #game_screen.blit(background_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    if b1.draw()==True:
        pygame.quit()
        level1()
        os.system('python menu_main.py')
        sys.exit()
    
    if b2.draw()==True:
        pygame.quit()
        level2()
        os.system('python menu_main.py')
        sys.exit()

    if b3.draw()==True:
        pygame.quit()
        level3()
        os.system('python menu_main.py')
        sys.exit()

    if back_button.draw()==True:
        pygame.quit()
        os.system('python menu_main.py')
        sys.exit()
    
    display_setting()

    pygame.display.update()
pygame.quit()
