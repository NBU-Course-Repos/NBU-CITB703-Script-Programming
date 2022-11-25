import pygame
from pygame.locals import *
from settings import *
BASE_PLAYER_IMAGE = "game\Assets\Playable_character\mario.png"


class Player(pygame.sprite.Sprite):
    FacingRight = True
    def __init__(self, pos:tuple):
        super().__init__()
        self.image = pygame.image.load(BASE_PLAYER_IMAGE)
        self.image = pygame.transform.scale(self.image, (tile_size,tile_size))
        self.rect = self.image.get_rect(topleft = pos)
        # self.rect.center = (160,250)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left >0:
            if pressed_keys[K_a]:
                if self.FacingRight:
                    self.FacingRight = False
                    self.image = pygame.transform.flip(self.image,flip_x = True, flip_y = False)
                self.rect.move_ip(-5,0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_d]:
                if not self.FacingRight:
                    self.FacingRight = True
                    self.image = pygame.transform.flip(self.image,flip_x = True, flip_y = False)
                self.rect.move_ip(5,0) 
                
        
        