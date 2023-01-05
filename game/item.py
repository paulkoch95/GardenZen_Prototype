import pygame.sprite
from game.tilemap import Tilemap


class Item(pygame.sprite.Sprite):

    def __init__(self, pos: pygame.Vector2, camera_group: pygame.sprite.Group, collectable_group: pygame.sprite.Group, name: str = "Generic"):
        super().__init__(camera_group, collectable_group)
        self.tiles = Tilemap()

        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        self.image.blit(self.tiles.tilemap, (0,0), self.tiles.tile_by_index(0,0,16,16))
        self.rect = pygame.rect.Rect(pos, self.image.get_size())

        self.name = name

