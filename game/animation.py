import pygame
from game.tilemap import Tilemap

class Animation(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, width: int, height: int):
        super().__init__()
        self.frame_index = 0
        self.tiles = Tilemap()
        self.frames = self.tiles.load_player_animation()

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(pos, (width, height))

    def animate(self, dt):
        self.frame_index += 4 * (dt / 1000)
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

