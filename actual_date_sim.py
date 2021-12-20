import pygame as pg
vec = pg.math.Vector2
from random import randint

big_pyro_slime_image = pg.image.load("Enemy_Large_Pyro_Slime.png")
pyro_slime_image = pg.image.load("Enemy_Pyro_Slime_1.png")
cryo_slime_image = pg.image.load("Enemy_Cryo_Slime.png")
player_image = pg.image.load("sword_light_no_bg_light.png")
distraction_image = pg.image.load("Enemy_Cryo_Slime.png")


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.pos = vec(randint(100,200),randint(100,1100))
        self.life = 10
        self.rect.center =self.pos
        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_s]:
            self.pos.y+= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed
            
        if keys[pg.K_UP]:
            self.pos.y -= self.speed
        if keys[pg.K_LEFT]:
            self.pos.x -= self.speed
        if keys[pg.K_DOWN]:
            self.pos.y += self.speed
        if keys[pg.K_RIGHT]:
            self.pos.x += self.speed
            
        

        self.rect.center = self.pos

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pyro_slime_image
        self.image = pg.transform.scale(self.image, (100,75))
        self.rect = self.image.get_rect()
        self.pos = vec(randint(1450,1500),randint(100,1200))
        self.life = 10
        self.rect.center =self.pos
        self.speed_x = 2
        self.speed_y =2
    
    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y
        if self.pos.x > 1450:
            self.speed_x = -5
            
        if self.pos.x <50:
            self.speed_x = 5
            
        if self.pos.y > 1150:
            self.speed_y = -5
            
        if self.pos.y <50:
            self.speed_y = 5
            
        
        self.rect.center =self.pos
        
class Big_Slime(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = big_pyro_slime_image
        self.image = pg.transform.scale(self.image, (225,175))
        self.rect = self.image.get_rect()
        self.pos = vec(randint(100,100),randint(100,100))
        self.rect.center =self.pos
        self.speed_x = 2
        self.speed_y =2
    
    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y
        if self.pos.x > 1450:
            self.speed_x = -1
            
        if self.pos.x <50:
            self.speed_x = 1
            
        if self.pos.y > 1150:
            self.speed_y = -2
            
        if self.pos.y <50:
            self.speed_y = 2
            
        
        self.rect.center =self.pos
        
        
class distraction(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = distraction_image
        self.image = pg.transform.scale(self.image, (125,75))
        self.rect = self.image.get_rect()
        self.pos = vec(randint(100,100),randint(100,100))
        self.rect.center =self.pos
        self.speed_x = 2
        self.speed_y =2
    
    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y
        if self.pos.x > 1450:
            self.speed_x = -2
            
        if self.pos.x <50:
            self.speed_x = 2
            
        if self.pos.y > 1150:
            self.speed_y = -2
            
        if self.pos.y <50:
            self.speed_y = 2
            
        self.rect.center = self.pos
        