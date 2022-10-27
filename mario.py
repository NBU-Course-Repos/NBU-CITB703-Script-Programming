import pygame, sys
from  pygame.locals import *

pygame.init()
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT= 600
BOTTOM_BORDER = 470
WHITE = (255,255,255)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0, 32)
pygame.display.set_caption("Aliexpress Mario")
marioImg = pygame.image.load("mario.png")
pygame.display.set_icon(marioImg)
marioImg = pygame.transform.scale(marioImg, (50,50))
marioFacingFront = True
marioX = 0
marioY = BOTTOM_BORDER
pygame.key.set_repeat(30, 30)
pygame.mixer.music.load("theme.mp3")
pygame.mixer.music.play()
marioBackground = pygame.image.load("images.png")
marioBackground = pygame.transform.scale(marioBackground, (800,600))
while True:
    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(marioBackground, (0,0))    
    DISPLAYSURF.blit(marioImg, (marioX, marioY))
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_RIGHT or event.key==K_d:
                if marioFacingFront == False:
                    marioFacingFront = True
                    marioImg = pygame.transform.flip(marioImg,flip_x = True, flip_y = False)
                marioX+=10 
            elif event.key==K_LEFT or event.key==K_a:
                if marioFacingFront == True:
                    marioFacingFront = False
                    marioImg = pygame.transform.flip(marioImg, flip_x = True, flip_y = False)
                marioX-=10
            elif event.key==K_UP or event.key==K_w:
                marioY-=10
            elif event.key==K_DOWN or event.key==K_s:
                if marioY==BOTTOM_BORDER:
                    continue
                marioY+=10
            elif event.key==K_SPACE:
                marioY-=20
                marioY+=10
            # elif event.key==K_m:
            #     pygame.mixer.music.stop()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
        
        