import ui.ui_component
from scenes.scene import Scene
from scenes import title_scene,option_scene, game_scene

import pygame
from assets import colors
pygame.init()
from ui import button, label

class MenueScene(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.font = pygame.font.Font(None, 30)

        self.menu_start_x, self.menu_start_y = 10,100

        self.b_start = button.Button(pygame.display.get_surface(),'Start',(self.menu_start_x,self.menu_start_y),(100,50))
        self.b_options = button.Button(pygame.display.get_surface(),'Options',(self.menu_start_x,self.menu_start_y+60),(100,50))
        self.b_quit = button.Button(pygame.display.get_surface(),'Quit',(self.menu_start_x,self.menu_start_y+120),(100,50))
        self.b_start.connect = self.switch_to_game
        self.b_options.connect = self.switch_to_options
        self.b_quit.connect = self.switch_to_slpash

        self.title_label = label.Label(pygame.display.get_surface(), 'Menue',40,colors.WHITE, (self.menu_start_x, self.menu_start_y-80), (0, 0))

        self.ui_components = []
        self.ui_components.append(self.b_start)
        self.ui_components.append(self.b_options)
        self.ui_components.append(self.b_quit)
        self.ui_components.append(self.title_label)
        # self.

    def switch_to_slpash(self):
        self.next = title_scene.SplashScreen()

    def switch_to_options(self):
        self.next = option_scene.OptionsScreen()

    def switch_to_game(self):
        self.next = game_scene.GameScreen()

    def input(self,event):
        pass

    def update(self):
        for c in self.ui_components:
            c.check_click()

    def render(self, screen):
        screen.fill(colors.BLACK)
        for c in self.ui_components:
            c.draw()
