import pygame.image
import pygame
from assets.ressources import COLORS
pygame.init()

class Tilemap:

    def __init__(self):
        self.character = pygame.image.load('assets/img/player.png').convert_alpha()
        self.ground_tile = pygame.image.load('assets/img/grass.png').convert()
        self.plains_tilemap = pygame.image.load('assets/img/plains.png').convert_alpha()
        self.tilemap = pygame.image.load('assets/img/tilemap_new.png').convert_alpha()
        self.map_texture = pygame.image.load('assets/img/map_test.png').convert_alpha()

        self.rock_texture = pygame.Surface((16,16), pygame.SRCALPHA)
        self.rock_texture.blit(self.plains_tilemap, (0,0), self.tile_by_index(0, 7))

        self.player_texture = pygame.Surface((48, 48), pygame.SRCALPHA)
        self.player_texture.blit(self.character, (0, 0), self.tile_by_index(0, 0, 48, 48))
    @classmethod
    def tile_by_index(cls, index_x, index_y, w = 16, h = 16):
        return pygame.rect.Rect((index_x*w, index_y*h), (w, h))

    def load_animation(self, tex, start_index_x, start_index_y, frame_len, frame_height, frame_width) -> list[pygame.Surface]:
        frames = []
        for frame in range(frame_len):
            anim_frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            anim_frame.blit(tex, (0, 0), self.tile_by_index(start_index_x+frame, start_index_y, frame_width, frame_height))
            frames.append(anim_frame)
        return frames

    def load_player_animation(self) -> list[pygame.Surface]:
        frames= []
        for frame in range(5):
            anim_frame = pygame.Surface((48, 48), pygame.SRCALPHA)
            anim_frame.blit(self.character, (0, 0), self.tile_by_index(frame, 0, 48, 48))
            frames.append(anim_frame)
        return frames
