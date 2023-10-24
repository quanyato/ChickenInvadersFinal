import pygame
import os
import sys
import button
from display_on_screen import draw_text_center

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614

pygame.display.set_caption('Chicken Invaders')
game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

back_image = pygame.image.load('image/btn-back.png')
bg_image = pygame.image.load("image/back_loop.jpg").convert_alpha()
bg_height = bg_image.get_height()
back_scroll_speed=0
def draw_background():
    global back_scroll_speed
    for x in range (2):
        game_screen.blit(bg_image, (0, ((-x * bg_height)-back_scroll_speed)))

b1_image = pygame.image.load('image/btn-green.png')
b2_image = pygame.image.load('image/btn-yellow.png')
b3_image = pygame.image.load('image/btn-red.png')
frame_image = pygame.image.load('image/frame-setting-menu.png')
btn_height = b1_image.get_height()
btn_width = b1_image.get_width()

sound = pygame.mixer.music.load('music/aov_song.wav')
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

run=True
back_button = button.Button(200,140,back_image)
b1 = button.Button(360,234,b1_image)
b2 = button.Button(360,283,b2_image)
b3 = button.Button(360,334,b3_image)
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
    
    game_screen.blit(frame_image, (190, 130))
    draw_text_center("SET THE NUMBER OF CHICKENS", 24, 190, 130, 580, 84)
    draw_text_center("10 CHICKENS", 18, 360, 234, btn_width, btn_height)
    draw_text_center("20 CHICKENS", 18, 360, 284, btn_width, btn_height)
    draw_text_center("30 CHICKENS", 18, 360, 334, btn_width, btn_height)

    pygame.display.update()
pygame.quit()
