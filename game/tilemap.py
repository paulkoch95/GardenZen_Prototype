import pygame.image
import pygame
pygame.init()

class Tilemap:

    def __init__(self):
        self.tilemap = pygame.image.load('assets/tilemap.png')

        self.grass_tile = pygame.Surface((64,32),pygame.SRCALPHA)
        self.grass_tile.blit(self.tilemap,(0,0),(0,0,64,32))

        self.green_tile = pygame.Surface((64,32),pygame.SRCALPHA)
        self.green_tile.blit(self.tilemap,(0,0),(64,0,64,32))

