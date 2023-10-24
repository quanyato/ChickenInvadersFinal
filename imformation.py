import pygame
import os
import sys
import button
from display_on_screen import text_multiple_line
pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chicken Invaders')

back_image = pygame.image.load('image/btn-back.png')
frame_image = pygame.image.load('image/frame-setting-menu.png')
member_frame_image = pygame.image.load('image/member-card.png')

bg_image = pygame.image.load("image/back_loop.jpg").convert_alpha()
bg_height = bg_image.get_height()
bg_scroll_position=0
def draw_background():
    global bg_scroll_position
    for x in range (2):
        game_screen.blit(bg_image, (0, ((-x * bg_height)-bg_scroll_position)))

pygame.mixer.music.load('music/aov_song.wav')
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

description_text = 'Trò chơi là cuộc chiến giữa một phi thuyền đơn độc và một chủng tộc gà đến từ không gian, sở hữu các công nghệ tiên tiến, những sinh vật có ý định chinh phục Trái đất.'

run=True
back_button = button.Button(200,140,back_image)
while run:
        
    draw_background()
    bg_scroll_position -= 0.1
    if abs(bg_scroll_position) > bg_height:
        bg_scroll_position=0

    game_screen.blit(frame_image, (190, 130))

    text_multiple_line(description_text,(230, 170), 500, 22)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
       
    if back_button.draw()==True:
        pygame.quit()
        os.system('python menu_main.py')
        sys.exit()

    pygame.display.update()
pygame.quit()
