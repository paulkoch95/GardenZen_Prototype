import pygame.image
import pygame
from assets.ressources import COLORS
pygame.init()

class Tilemap:

    def __init__(self):
        self.tilemap = pygame.image.load('assets/img/tilemap.png').convert()
        self.character = pygame.image.load('assets/img/player.png').convert_alpha()
        self.ground_tile = pygame.image.load('assets/img/grass.png').convert()
        self.plains_tilemap = pygame.image.load('assets/img/plains.png').convert_alpha()

        self.rock_texture = pygame.Surface((16,16), pygame.SRCALPHA)
        self.rock_texture.blit(self.plains_tilemap, (0,0), (0, 7*16, 16, 16))

        self.grass_tile = pygame.Surface((64,32),pygame.SRCALPHA)
        self.grass_tile.blit(self.tilemap,(0,0),(0,0,64,32))

        self.green_tile = pygame.Surface((64,32),pygame.SRCALPHA)
        self.green_tile.blit(self.tilemap,(0,0),(64,0,64,32))

        self.green_textured = pygame.Surface((64,32), pygame.SRCALPHA)
        self.green_textured.blit(self.tilemap,(0,0), (64+64,0,64,32))

        self.red_texture = pygame.Surface((48,48), pygame.SRCALPHA)
        self.red_texture.blit(self.character, (0,0), (0,0,48,48))
