import scenes.menu_scene
from scenes.scene import Scene
import pygame
from assets.ressources import COLORS
pygame.init()


class SplashScreen(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.font = pygame.font.Font(None, 30)
        self.logo = pygame.image.load('assets/img/splash_image.png')
        self.logo = pygame.transform.scale(self.logo, (self.logo.get_width()*2,self.logo.get_height()*2))
        self.logo.set_alpha(0)
        self.w, self.h = pygame.display.get_surface().get_size()

        self.logo_x = self.w/2-(self.logo.get_width()/2)
        self.logo_y = self.h/2


    def update(self, dt):
        # logo movement animation timestep
        self.logo_y = self.logo_y - 1
        # logo fade in logic
        if self.logo.get_alpha() < 255:
            self.logo.set_alpha(self.logo.get_alpha()+2)
        else:
            self.next = scenes.menu_scene.MenueScene()

    def input(self,events):
        pass

    def render(self, screen: pygame.surface):
        screen.fill(COLORS.BLACK)
        screen.blit(self.logo,(self.logo_x,self.logo_y))
