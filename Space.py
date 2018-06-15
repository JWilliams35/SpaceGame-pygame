import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

H, W= 500, 500
win =  pygame.display.set_mode((H, W))
#background image
background = pygame.image.load("assest/space.jpg").convert()
B = 0
#name
pygame.display.set_caption("Insert name")


#------class-----
class player(object):
    def __init__(self, x, y, LA, LO):
        
        self.LA = LA #hero size (LA = width, LO = height)
        self.LO = LO
        self.x = x #starting position
        self.y = y
        self.vel = 5 #space between boundary and ship
        self.speed = 15 #speed of the ship
        self.left = False
        self.right = False
        self.down = False

    def draw(self,win):
        hero = pygame.image.load('assest/idle/idleH.png')
        hero = pygame.transform.scale(hero, (self.LA, self.LO))
        rect = hero.get_rect()
        rect = rect.move((self.x, self.y))
        flyRight = pygame.image.load('assest/right/rightH.png')
        flyRight = pygame.transform.scale(flyRight, (self.LA, self.LO))
        flyLeft = pygame.image.load('assest/left/leftH.png')
        flyLeft = pygame.transform.scale(flyLeft, (self.LA, self.LO))
        flyBack = pygame.image.load('assest/back/back.png')
        flyBack = pygame.transform.scale(flyBack, (self.LA, self.LO))

        #change sprite
        if self.left:
            win.blit(flyLeft,(self.x,self.y))
        elif self.right:
            win.blit(flyRight,(self.x,self.y))
        elif self.down:
            win.blit(flyBack, (self.x,self.y))
        else:
            win.blit(hero, (self.x,self.y))


#--------------------

def DrawAssest():
    global B
    
    rel_B = B % background.get_rect().height#background 
    win.blit(background, (0,rel_B - background.get_rect().height ))
    if rel_B < W:
        win.blit(background, (0, rel_B)) 
    B +=5 #background speed 

    PC.draw(win)
    pygame.display.update()

#main loop
PC = player(220, 240, 85, 80)
run = True
while run:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and PC.x > PC.vel:
        PC.x -= PC.speed
        PC.left = True
        PC.right = False
        
    elif keys[pygame.K_RIGHT] and PC.x < W - PC.LA - PC.vel:
        PC.x += PC.speed
        PC.right = True
        PC.left = False
        
    else:
        PC.right = False
        PC.left = False
        
    if keys[pygame.K_UP] and PC.y > PC.vel:
        PC.y -= PC.speed
    elif keys[pygame.K_DOWN] and PC.y < H - PC.LO - PC.vel: 
        PC.y += PC.speed
        PC.down = True
    else:
        PC.down = False


    DrawAssest()

    
pygame.quit()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

