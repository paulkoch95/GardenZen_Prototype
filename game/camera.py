import pygame.sprite
from assets.ressources import COLORS

class ScrollingCamera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.intermediate_surface = pygame.Surface(self.display_surface.get_size(), pygame.SRCALPHA)
        self.camera_offset = pygame.math.Vector2(0,0)
        self.x_m, self.y_m = 0, 0

    def input(self):
        self.x_m, self.y_m = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed()[0]:
            self.camera_offset += pygame.math.Vector2(self.x_m//2, self.y_m//2)

    def render_context(self) -> None:
        self.intermediate_surface.fill(COLORS.CORNFLOWER_BLUE)

        for sprite in self.sprites():
            offset_rect = sprite.rect.topleft + self.camera_offset
            self.intermediate_surface.blit(sprite.image, offset_rect)
            pygame.draw.rect(self.intermediate_surface,COLORS.RED, (offset_rect,sprite.image.get_size()),1)
        surf_size = pygame.math.Vector2(self.intermediate_surface.get_size())
        scaled_surface = pygame.transform.scale(self.intermediate_surface, surf_size*2)

        self.display_surface.blit(scaled_surface, (0,0))