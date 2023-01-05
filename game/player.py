import pygame
from game.tilemap import Tilemap
from enum import Enum
from game.animation import Animation
from game.item import Item
class STATES(Enum):
    IDLE = 0,
    INTERACTION = 1,
    WALKING = 2
class Player(pygame.sprite.Sprite):

    def __init__(self, pos: pygame.math.Vector2, camera_group: pygame.sprite.Group, collectables: pygame.sprite.Group):
        super().__init__(camera_group)
        # load tiles and textures for the player
        self.tiles = Tilemap()

        self.camera_group = camera_group

        # self.image = self.tiles.player_texture
        self.texture = Animation(pos, 48, 48)
        self.image = self.texture.image

        self.inventory: list[Item] = []

        # player position and movement
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.move_vector = pygame.math.Vector2((0, 0))

        # player animation
        self.frame_index = 0

        # player states
        self.player_state = STATES.IDLE
        self.collectables: pygame.sprite.Group = collectables
    def get_tile_referenced_position(self):
        center = pygame.math.Vector2(self.rect.center)
        return pygame.math.Vector2(
            center.x // 16,
            center.y // 16
        )

    def collisions(self):
        for collectable in self.collectables.sprites():
            if self.rect.colliderect(collectable.rect):
                self.inventory.append(collectable)
                collectable.kill()

    def drop_items(self):
        if self.inventory:
            item = self.inventory.pop(0)
            item.rect.right = self.rect.left
            item.rect.bottom = self.rect.top
            self.collectables.add(item)
            self.camera_group.add(item)

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
                if event.key == pygame.K_SPACE:
                    self.drop_items()

                self.move_vector = pygame.math.Vector2(0, 0)

    def animate(self, dt):
        self.texture.animate(dt)
        self.image = self.texture.image

    def update(self):
        self.rect.center += self.move_vector
        self.collisions()
