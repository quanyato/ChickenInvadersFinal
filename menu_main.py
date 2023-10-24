import pygame
import os
import sys
import button
from display_on_screen import draw_text_center
pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614

game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chicken Invaders')

bg_image = pygame.image.load("image/back_loop.jpg").convert_alpha()
bg_height = bg_image.get_height()
bg_scroll_position=0
def draw_background():
    global bg_scroll_position
    for x in range (2):
        game_screen.blit(bg_image, (0, ((-x * bg_height)-bg_scroll_position)))

logo_image = pygame.image.load('image/logo-small-scale.png')
play_image = pygame.image.load('image/btn-frame.png')
quit_image = pygame.image.load('image/btn-frame.png')
setting_image = pygame.image.load('image/btn-frame.png')
contact_image = pygame.image.load('image/btn-frame.png')
option_image = pygame.image.load('image/btn-frame.png')
music_image =  pygame.image.load('image/btn-mute.png')

pygame.mixer.music.load('music/aov_song.wav')
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play(-1)

play_button=button.Button(360, 284, play_image)
setting_button=button.Button(360, 334, setting_image)
option_button=button.Button(360, 384, option_image)
contact_button=button.Button(360, 434, contact_image)
quit_button=button.Button(360, 484, quit_image)

run=True
while run: 
    draw_background()
    bg_scroll_position -= 0.1
    if abs(bg_scroll_position) > bg_height:
        bg_scroll_position=0

    draw_text_center('PLAY', 18, 360, 284, play_image.get_width(), play_image.get_height())
    draw_text_center('SETTING', 18, 360, 334, play_image.get_width(), play_image.get_height())
    draw_text_center('INFORMATION', 18, 360, 384, play_image.get_width(), play_image.get_height())
    draw_text_center('CONTACT US', 18, 360, 434, play_image.get_width(), play_image.get_height())
    draw_text_center('QUIT', 18, 360, 484, play_image.get_width(), play_image.get_height())

    game_screen.blit(logo_image, [295,60])
    game_screen.blit(music_image, [870,530])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    if quit_button.draw()==True:
        pygame.quit()
        sys.exit() 

    if contact_button.draw()==True:
        pygame.quit()
        os.system('python contact.py')
        sys.exit() 

    if option_button.draw() == True:
        pygame.quit()
        os.system('python imformation.py')
        sys.exit() 
    
    if setting_button.draw() == True:
        pygame.quit()
        os.system('python setting_main.py')
        sys.exit() 

    if play_button.draw()==True: 
        pygame.quit()
        os.system('python game_main.py')
        os.system('python menu_main.py')
        sys.exit()

    pygame.display.update()

pygame.quit()