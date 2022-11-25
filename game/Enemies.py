import pygame
from pygame.locals import *
from settings import *

GOOMBA = "game\Assets\Enemies\goomba.svg"

class Enemies(pygame.sprite.Sprite):
    
    
    def __init__(self):
        self.MovingRight = True
        super().__init__()
        self.image = pygame.image.load(GOOMBA)
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (300,250)
    
    def move(self):
        if self.rect.right >= SCREEN_WIDTH:
            self.MovingRight = False
        if self.rect.left == 0:
            self.MovingRight = True
        if self.MovingRight:
            self.rect.move_ip(3,0)
        else:
            self.rect.move_ip(-3,0)
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)