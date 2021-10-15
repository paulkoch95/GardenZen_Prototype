import scenes.menu_scene
from scenes.scene import Scene
import pygame
from assets import colors
pygame.init()


class OptionsScreen(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.font = pygame.font.Font(None, 30)

    def update(self):
        pass

    def input(self,event):
        print("Input overwritten in Debug Scene!")

    def render(self, screen: pygame.surface):
        debug_text = self.font.render(str(f"Option Screen scene"),True, colors.RED)
        screen.fill(colors.BLACK)
        screen.blit(debug_text,(50,80))
