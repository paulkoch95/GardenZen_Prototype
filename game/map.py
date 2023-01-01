import pygame.surface
from game.tilemap import Tilemap

class Map(pygame.sprite.Sprite):

    TILE_WIDTH = 16
    TILE_HEIGHT = 16

    def __init__(self, camera_group: pygame.sprite.Group):
        super().__init__(camera_group)
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.width, self.height = len(self.map_data)*self.TILE_HEIGHT, len(self.map_data[0])*self.TILE_WIDTH
        self.render_context = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.tiles = Tilemap()
        self.ground_tile = self.tiles.ground_tile
        self.rock_tile = self.tiles.rock_texture

        self.generate_map()

        self.image = self.render_context
        self.rect = self.image.get_rect(topleft=(0,0))

    def generate_map(self):
        for y, y_val in enumerate(self.map_data):
            for x, x_val in enumerate(y_val):
                tile_rect = pygame.rect.Rect(x*self.TILE_WIDTH, y*self.TILE_HEIGHT, self.TILE_WIDTH, self.TILE_HEIGHT)
                self.render_context.blit(self.ground_tile, tile_rect)
                if x_val == 1:
                    self.render_context.blit(self.rock_tile, tile_rect)

    def get_level_data(self):
        return self.map_data

    def set_level_data(self, map_x, map_y, value):
        self.map_data[map_y][map_x] = value



