import pygame
import os
import sys
import button
pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614

game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chicken Invaders')
#background_image = pygame.image.load('image/bg.jpg').convert()
bg_image = pygame.image.load("image/back_loop.jpg").convert_alpha()
bg_height = bg_image.get_height()
back_scroll_speed=0

logo_image = pygame.transform.scale(pygame.image.load('image/logo.png'), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
play_image = pygame.transform.scale(pygame.image.load('image/play.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//15))
quit_image = pygame.transform.scale(pygame.image.load('image/quit.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//15))
setting_image = pygame.transform.scale(pygame.image.load('image/setting.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//15))
contact_image = pygame.transform.scale(pygame.image.load('image/contact.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//15))
option_image = pygame.transform.scale(pygame.image.load('image/option.png'), (SCREEN_WIDTH//5, SCREEN_HEIGHT//15))

music_image =  pygame.transform.scale(pygame.image.load('image/music_button.png'), (50, 50))
theme_song = pygame.mixer.Sound('music/aov_song.wav')
music_one_time = True   # chạy nhạc 1 lần

play_button=button.Button(400, 350, play_image)
setting_button=button.Button(400, 400, setting_image)
option_button=button.Button(400, 450, option_image)
contact_button=button.Button(400, 500, contact_image)
quit_button=button.Button(400, 550, quit_image)

def draw_background():
    global back_scroll_speed
    for x in range (2):
        game_screen.blit(bg_image, (0, ((-x * bg_height)-back_scroll_speed)))

run=True
while run:
    if music_one_time:
        theme_song.play()
        music_one_time = False
             
    draw_background()
    back_scroll_speed -= 0.1
    if abs(back_scroll_speed) > bg_height:
        back_scroll_speed=0
    #game_screen.blit(background_image, [0, 0])
    game_screen.blit(logo_image, [250,50])
    game_screen.blit(music_image, [850,530])

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