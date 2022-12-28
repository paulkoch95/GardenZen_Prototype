import pygame
from game.tilemap import Tilemap

class Player:

    def __init__(self, surface: pygame.Surface):
        self.position = pygame.Vector2((0,0))
        self.surf = surface
        self.tiles = Tilemap()
        self.tex = self.tiles.red_texture

    def move(self, event):
        pass
    def render(self):
        self.surf.blit(self.tex, self.position)