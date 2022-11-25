import pygame, sys
from pygame.locals import *
from player import Player
from enemies import Enemies
from level import Level
from settings import *

WHITE:tuple = (255,255,255)
pygame.init()
FPS = pygame.time.Clock() 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill((255,255,255))
pygame.display.set_caption("Aliexpress Mario")

level = Level(level_data, DISPLAYSURF)


while(True):
    
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    level.run()
    # P1.update()
    # GOOMBA1.move()  
    
    # P1.draw(DISPLAYSURF)
    # GOOMBA1.draw(DISPLAYSURF)
    pygame.display.update()
    FPS.tick(30)  
