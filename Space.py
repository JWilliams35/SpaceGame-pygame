import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

#size of the game
W, H = 500,500
win =  pygame.display.set_mode((W, H))
#background image
background = pygame.image.load("assest/space.jpg").convert()
B = 0
#name
pygame.display.set_caption("Insert name")


#------reference-----

#hero size (LA = width, LO = height)
LA, LO = 85, 80
#starting position
#(changes in starting position will have to be made manually,
#otherwise it will be based on the window size)
x = W * 0.44
y = H * 0.84
#Hero hitbox (don't touch unless you want the hitbox to not match the sprite)
widthH, heightH = LA, LO
#space between boundary and ship
vel = 5
#speed of the ship
speed = 15
#do not touch
left = False
right = False
down = False
#--------------------

def DrawAssest():
    global LA, LO
    global B
    
    #background
    rel_B = B % background.get_rect().height
    win.blit(background, (0,rel_B - background.get_rect().height ))
    if rel_B < W:
        win.blit(background, (0, rel_B))
    #background speed
    B +=5
    #character
    hero = pygame.image.load('assest/idle/idleH.png')
    hero = pygame.transform.scale(hero, (LA, LO))
    rect = hero.get_rect()
    rect = rect.move((x, y))
    flyRight = pygame.image.load('assest/right/rightH.png')
    flyRight = pygame.transform.scale(flyRight, (LA, LO))
    flyLeft = pygame.image.load('assest/left/leftH.png')
    flyLeft = pygame.transform.scale(flyLeft, (LA, LO))
    flyBack = pygame.image.load('assest/back/back.png')
    flyBack = pygame.transform.scale(flyBack, (LA, LO))

    #change sprite
    if left:
        win.blit(flyLeft,(x,y))
    elif right:
        win.blit(flyRight,(x,y))
    elif down:
        win.blit(flyBack, (x,y))
    else:
        win.blit(hero, (x,y))
        
    pygame.display.update()

run = True
while run:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= speed
        left = True
        right = False
        
    elif keys[pygame.K_RIGHT] and x < W - widthH - vel:
        x += speed
        right = True
        left = False
        
    else:
        right = False
        left = False
        
    if keys[pygame.K_UP] and y > vel:
        y -= speed
    elif keys[pygame.K_DOWN] and y < H - heightH - vel: 
        y += speed
        down = True
    else:
        down = False



    DrawAssest()

    
pygame.quit()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

