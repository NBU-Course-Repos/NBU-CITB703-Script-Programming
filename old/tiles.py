import pygame, sys, os
from  pygame.locals import *
# TO DO: Make the character colide with the tiles and detect on which 
# tile it's walking

data = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[12, 9, 9, 16, 0, 0, 0, 0, 13, 14, 15, 0, 0, 0, 0, 1, 2, 2, 2, 3],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 6],
[0, 0, 0, 13, 14, 14, 15, 0, 0, 0, 0, 0, 0, 0, 0, 12, 9, 9, 9, 16],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 3, 17, 17, 17, 4, 5, 5, 5, 5, 5, 6, 17, 17, 17, 17, 17, 1, 2, 3]]

pygame.init()
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT= 600
WHITE = (255,255,255)
TileWidth = 64
TileHeight = 64
MapHeight = 10
MapWidth = 20
fpsClock = pygame.time.Clock()

marioImg = pygame.image.load("mario.png")
marioImg = pygame.transform.scale(marioImg, (50,50))
marioX = 0
marioY = 50

tile = []
for i in range(1,19):
    tile.append( pygame.image.load("png\\Tiles\\"+str(i)+".png" ))
print(tile)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0, 32)
while True:
    DISPLAYSURF.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_RIGHT or event.key==K_d:
                marioX+=10 
            elif event.key==K_LEFT or event.key==K_a:
                marioX-=10
            elif event.key==K_UP or event.key==K_w:
                marioY-=10
            elif event.key==K_DOWN or event.key==K_s:
                marioY+=10
            elif event.key==K_SPACE:
                marioY-=20
                marioY+=10
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for i in range(0,MapHeight-1):
        for j in range(0,MapWidth-1):
            if data[i][j]>0:
                DISPLAYSURF.blit(tile[data[i][j]],
                                 ((j)*TileHeight,(i)*TileWidth))
    DISPLAYSURF.blit(marioImg, (marioX, marioY))
    pygame.display.update()
    fpsClock.tick(FPS)