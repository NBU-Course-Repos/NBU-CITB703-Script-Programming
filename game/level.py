import pygame
from tiles import Tile
from settings import *
from player import Player

class Level():
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
    
    def run(self):
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
    
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 1:
                    self.tiles.add(Tile((x,y),tile_size))
                if col == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
        
     