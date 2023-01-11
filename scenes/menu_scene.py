from scenes.scene import Scene
from scenes import title_scene,option_scene, game_scene

from assets.ressources import COLORS, FONT
from UI.UserInterface import UserInterface
from UI.button import Button
from UI.label import Label

class MenueScene(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.font = FONT.pixel_font(30)

        self.menu_start_x, self.menu_start_y = 10, 100

        self.user_interface = UserInterface()

        self.b_start = Button(self.user_interface, 'Start', (self.menu_start_x, self.menu_start_y), (100, 50))
        self.b_options = Button(self.user_interface, 'Options', (self.menu_start_x, self.menu_start_y + 60), (100, 50))
        self.b_quit = Button(self.user_interface,'Quit',(self.menu_start_x,self.menu_start_y+120),(100,50))
        self._label = Label(self.user_interface, "Hallo Welt", 24, COLORS.BLACK,COLORS.WHITE, (200,200))
        self.b_start.connect = self.switch_to_game
        self.b_options.connect = self.switch_to_options
        self.b_quit.connect = self.switch_to_slpash

    def switch_to_slpash(self):
        self.next = title_scene.SplashScreen()

    def switch_to_options(self):
        self.next = option_scene.OptionsScreen()

    def switch_to_game(self):
        self.next = game_scene.GameScreen()

    def input(self,event):
        self.user_interface.input(event)

    def update(self, dt = 1):
        pass
        # for c in self.ui_components:
        #     c.check_click()

    def render(self, screen):
        screen.fill(COLORS.BLACK)
        self.user_interface.render()