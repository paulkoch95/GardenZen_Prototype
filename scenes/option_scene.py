import scenes.menu_scene
from scenes.scene import Scene
import pygame
from assets.ressources import FONT, COLORS
pygame.init()


class OptionsScreen(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.font = FONT.pixel_font(30)

    def update(self):
        pass

    def render(self, screen: pygame.surface):
        debug_text = self.font.render(str(f"Option Screen scene"), True, COLORS.RED)
        screen.fill(COLORS.BLACK)
        screen.blit(debug_text,(50,80))
