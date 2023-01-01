import pygame
from game.tilemap import Tilemap


class Player(pygame.sprite.Sprite):

    def __init__(self, pos: pygame.math.Vector2, camera_group: pygame.sprite.Group):
        super().__init__(camera_group)
        self.tiles = Tilemap()
        self.image = self.tiles.red_texture
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.move_vector = pygame.math.Vector2((0, 0))

    def move(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.move_vector += pygame.math.Vector2(-1,0)
                if event.key == pygame.K_w:
                    self.move_vector += pygame.math.Vector2(0,-1)
                if event.key == pygame.K_s:
                    self.move_vector += pygame.math.Vector2(0,1)
                if event.key == pygame.K_d:
                    self.move_vector += pygame.math.Vector2(1,0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.move_vector *= pygame.math.Vector2(0, 1)
                if event.key == pygame.K_w:
                    self.move_vector *= pygame.math.Vector2(1, 0)
                if event.key == pygame.K_s:
                    self.move_vector *= pygame.math.Vector2(1, 0)
                if event.key == pygame.K_d:
                    self.move_vector *= pygame.math.Vector2(0, 1)

                self.move_vector = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.center += self.move_vector