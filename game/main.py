import pygame, sys
from pygame.locals import *
from enum import Enum
import Player, Enemies

WHITE:tuple = (255,255,255)

pygame.init()
#Set FPS limit to 60, otherwise
#the the main loop will execute as fast as it can
FPS = pygame.time.Clock() 
#Display Const properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode\
                ((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill((255,255,255))
pygame.display.set_caption("Aliexpress Mario")

P1 = Player.Player()
GOOMBA1 = Enemies.Enemies()

while(True):
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    GOOMBA1.move()
    
    P1.draw(DISPLAYSURF)
    GOOMBA1.draw(DISPLAYSURF)
    
        
    pygame.display.update()
    FPS.tick(30)  
