import pygame as pg 
from actual_date_sim import *
import time

from pygame.constants import WINDOWHITTEST

from actual_date_sim import Enemy
pg.init()
pg.font.init()

WIDTH = 1500
HEIGHT = 1200

BLACK = (0,0,0)
WHITE =(255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
COLOUR = (177,0,13)

comic_sans30 = pg.font.SysFont("Comic Sans M",30)

ting_pos_x = 380
ting_pos_y = 280
ting_size_x = 1
ting_size_y = 1

direction = 0
direction_y = 0

speed = 2

visual = pg.display.set_mode((WIDTH,HEIGHT))

clock = pg.time.Clock()
FPS = 240

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

small_slime = distraction()
small_slime = enemies
Big_Slime = Big_Slime()
slime = Enemy()
all_sprites.add(slime)
enemies.add(slime)
sword = Player()
all_sprites.add(sword, Big_Slime)

SCORE = -0
    
playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
    
    
    visual.fill(BLUE)
    #object = (ting_pos_x,ting_pos_y , ting_size_x, ting_size_y)
    #pg.draw.rect(visual, GREEN, object)
    
    
    all_sprites.draw(visual)
    
    all_sprites.update()
    
    hits = pg.sprite.spritecollide(sword, enemies, True)
    if hits:
       SCORE += 1 
    
    while len(enemies) <10000:
        slime = Enemy()
        all_sprites.add(slime)
        enemies.add(slime)
        
    poeng = comic_sans30.render(str(SCORE), False, (WHITE))
    visual.blit(poeng, (1400,20))
        
    pg.display.update()
    
    #if ting_pos_x + ting_size_x > WIDTH:
        #ting_pos_x = WIDTH - ting_size_x
        
    #if ting_pos_y > 590:
        #ting_pos_y = HEIGHT - ting_size_y
    
    #if ting_pos_x < 0:
        #ting_pos_x = 0
    
    #if ting_pos_y < 0:
        #ting_pos_y = 0
    




time.sleep(5)