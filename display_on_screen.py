import pygame
import Base_modul
import Chicken_modul
import random
import sys
import boss_modul
pygame.init()
#======================================================================================
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font_large = pygame.font.Font('Fonts/Aldrich-Regular.ttf', 24)
font_small = pygame.font.Font('Fonts/Aldrich-Regular.ttf', 14)
font_regular = pygame.font.Font('Fonts/Aldrich-Regular.ttf', 18)

def draw_text_center(text="",font_size=0, frame_x=0, frame_y=0, frame_width=0, frame_height=0):
    font = pygame.font.Font('Fonts/Aldrich-Regular.ttf', font_size)
    width, height = font.size(text)
    text_render = font.render(text, True, (255,255,255))
    text_x_pos = frame_x + (frame_width//2 - width//2)
    text_y_pos = frame_y + (frame_height//2 - height//2)
    game_screen.blit(text_render, (text_x_pos, text_y_pos))

LIGHT_YELLOW = (255, 255, 204)
WHITE = (255, 255, 255)
BLUE = ( 0,0,255)
RED   = (255,   0,   0)

rocket_image = pygame.image.load('image/rocket.png')
rocket_image = pygame.transform.scale(rocket_image, (SCREEN_WIDTH//6, SCREEN_HEIGHT//3))
big_boom_image = pygame.image.load('image/vu_no_2.png')
big_boom_image = pygame.transform.scale(big_boom_image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
dui_ga_mini = pygame.image.load('image/dui_ga.png').convert_alpha()
dui_ga_mini =  pygame.transform.scale(dui_ga_mini, (SCREEN_WIDTH//45, SCREEN_HEIGHT//20))
hp_mini = pygame.image.load('image/hp.png').convert_alpha()
hp_mini =  pygame.transform.scale(hp_mini, (SCREEN_WIDTH//35, SCREEN_HEIGHT//25))
rocket_mini = pygame.image.load('image/rocket.png').convert_alpha()
rocket_mini =  pygame.transform.scale(rocket_mini, (SCREEN_WIDTH//25, SCREEN_HEIGHT//15))
boss_mini = pygame.image.load('image/ga_boss_1.png').convert_alpha()
boss_mini =  pygame.transform.scale(boss_mini, (SCREEN_WIDTH//25, SCREEN_HEIGHT//15))
game_over_image = pygame.image.load('image/begin2.png')
game_over_image = pygame.transform.scale(game_over_image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
base_destroyed_image = pygame.image.load('image/vu_no_3.png')
base_destroyed_image  = pygame.transform.scale(base_destroyed_image , (SCREEN_WIDTH//9, SCREEN_HEIGHT//9))
winner_image =  pygame.image.load('image/winner.png')
winner_image  = pygame.transform.scale(winner_image , (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
#================================================================================

def display_on_screen(base):
    score_text = 'Score: ' + str(base.score)
    display_text = font_regular.render(score_text, True, LIGHT_YELLOW)
    game_screen.blit(display_text , [30,30])

    if base.hp < 0: base.hp=0
    hp_left_text = font_regular.render(str(round(base.hp)*1.0) + ' %', True, LIGHT_YELLOW)
    game_screen.blit(hp_left_text, [60,60])
    game_screen.blit(hp_mini, [25,60])

    rk_left_text = font_regular.render(str(base.rocket), True, LIGHT_YELLOW)
    game_screen.blit(rk_left_text, [60,100])
    game_screen.blit(rocket_mini, [20,85])

    dui_ga_text = font_regular.render(str(base.num_chicken_thighs), True, LIGHT_YELLOW)
    game_screen.blit(dui_ga_text, [60,130])
    game_screen.blit(dui_ga_mini, [30,130])

def display_boss_hp(boss):
    pygame.draw.rect(game_screen, RED, (250,20,500*boss.hp/100,25))   # vẽ thanh máu
    pygame.draw.rect(game_screen, RED, (250,20,500,2))                                  # vẽ viền thanh máu
    pygame.draw.rect(game_screen, RED, (250,20+25,500,2))
    pygame.draw.rect(game_screen, RED, (250+500-2,20,2,25))
    pygame.draw.rect(game_screen, RED, (250,20,2,25))
    game_screen.blit(boss_mini, [200, 10])
    game_screen.blit(font_regular.render(str(round(boss.hp*10)/10.0) + " % HP", True, LIGHT_YELLOW), [250 +200, 20])

def display_game_over(base):
    if base.game_over == "checked":
        game_screen.blit(game_over_image, [220,50])
        game_screen.blit( base_destroyed_image, [base.x_loc-10, base.y_loc-10] )
        score_text = 'Score: ' + str(base.score)
        display_text = font_large.render(score_text, True, LIGHT_YELLOW)
        game_screen.blit(display_text , [350,400])
        score_text = 'Thank You For Playing'
        display_text = font_large.render(score_text, True, LIGHT_YELLOW)
        game_screen.blit(display_text , [180,480])

def display_winner(base):
    if base.winner == "checked":
        game_screen.blit(winner_image, [220,70])
        score_text = 'Score: ' + str(base.score)
        display_text = font_large.render(score_text, True, LIGHT_YELLOW)
        game_screen.blit(display_text , [400,400])
        score_text = 'Thank You For Playing'
        display_text = font_large.render(score_text, True, LIGHT_YELLOW)
        game_screen.blit(display_text , [250,480])