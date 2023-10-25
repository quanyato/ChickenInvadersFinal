import pygame
import random
import sys

pygame.mixer.init()

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
BLUE = ( 0,0,255)
font = pygame.font.Font('Fonts/Aldrich-Regular.ttf', 18)

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

base_image = pygame.image.load('image/ship.png')
base_width = base_image.get_rect().width   
base_height = base_image.get_rect().height

xe_no_image = pygame.image.load('image/vu_no_3.png')
xe_no_image = pygame.transform.scale(xe_no_image, (SCREEN_WIDTH//8, SCREEN_HEIGHT//8))
vu_no_image = pygame.image.load('image/vu_no.png')
vu_no_image = pygame.transform.scale(vu_no_image, (SCREEN_WIDTH//9, SCREEN_HEIGHT//9))

base_missile_image = pygame.image.load('image/bullet.png')
base_missile_width = base_missile_image.get_rect().width
base_missile_height = base_missile_image.get_rect().height

defense_image =  pygame.image.load('image/sheld-small.png')
defense_width = defense_image.get_width()
defense_height = defense_image.get_height()

game_over_sound = pygame.mixer.Sound('music/game_over_music.mp3')
winner_sound = pygame.mixer.Sound('music/winner.mp3')
#==============================================================================================
class Base:

    x_loc = SCREEN_WIDTH//2 - base_width//2
    y_loc = 550
    time_boom =  0
    hp = 100
    num_chicken_thighs =  0
    score = 0
    rocket = 1
    game_over = "false" # "true" , "checked"
    winner = "false" # "true" , "checked"
    #---------------------------------------------------------------------------
    def draw_base(self):
        if self.time_boom > 0:
            self.time_boom -= 1
            game_screen.blit(vu_no_image,[self.x_loc, self.y_loc] )
        else:
            game_screen.blit(base_image, [self.x_loc, self.y_loc] )
    pass
    #---------------------------------------------------------------------------
    def update_roket_and_defense(self,base_defense):
        if  self.num_chicken_thighs >= 10:
            self.num_chicken_thighs = 0
            self.rocket += 1 
            base_defense.time = 600
    
    def check_game_over(self):
        if self.hp <= 0 and self.game_over == "false":
            self.game_over = "true"
            self.hp = 0
            game_over_sound.play()
        if self.game_over == "true": self.game_over = "checked"
    
    def check_winner(self,boss):
        if boss.hp <= 0 and self.winner == "false":
            self.winner = "true"
            boss.hp = 0
            boss.statu = 'disappear'
            winner_sound.play()
        if self.winner == "true": self.winner = "checked"    

#============================================================================
class Base_missile ():
    x_loc = 0
    y_loc = 0
    missile_firing = False
    sub_hp_boss = 1

    #------------------------------------
    def draw_base_missile(self):
        if self.missile_firing != False:  game_screen.blit(base_missile_image,[self.x_loc, self.y_loc])
    #-------------------------------------
    
    def move(self):
        if self.missile_firing == True:
            self.y_loc -= 10
            if self.y_loc < 0:
                self.missile_firing = False

#==============================================================================
class Base_defense(Base):
    time = 200

    def draw_defense(self,base):
        sheld_x = base.x_loc - defense_width//2 + base_width//2
        sheld_y = base.y_loc - defense_height//2 + base_height//2
        if self.time > 0:
            if self.time >= 200:
                game_screen.blit(defense_image, [sheld_x, sheld_y])
            else:
                if self.time % 12 == 0:
                    game_screen.blit(defense_image, [sheld_x, sheld_y])
                game_screen.blit(font.render("RUN OUT OF TIME", True, (255,255,255)), [400,400])
            self.time -= 1
