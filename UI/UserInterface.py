import pygame.sprite
from assets.ressources import COLORS
class UserInterface(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.drawing_surface = pygame.display.get_surface()

    def input(self, events):
        for widget in self.sprites():
            if hasattr(widget, "input"):
                widget.input(events)

    def render(self):
        for widget in self.sprites():
            self.drawing_surface.blit(widget.image, widget.rect)
            # pygame.draw.rect(self.drawing_surface, COLORS.RED, widget.rect, 1)
