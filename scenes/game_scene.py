from scenes.scene import Scene
import pygame
from assets import ressources
from ui.label import Label
from game.map import Map
from game.tilemap import Tilemap
from game.player import Player
from game.camera import ScrollingCamera
from debug import tools
import numpy as np
pygame.init()

TILE_W = 64
TILE_H = 32

class GameScreen(Scene):

    def __init__(self):
        Scene.__init__(self)
        # placeholder surface for the current map
        # self.map_surface = pygame.Surface((200,200), pygame.SRCALPHA)
        # self.map_rectangle = self.map_surface.get_rect()
        self.x_m, self.y_m = 0, 0
        self.scaling_factor = 1
        # player object
        self.camera = ScrollingCamera()

        # levelobj holding infor about certain tiles a map coords
        self.level_obj = Map(self.camera)
        self.player = Player(pygame.math.Vector2(0,0), self.camera)

        # tilemap giving image of the tile to be rendered
        self.tilemap = Tilemap()
        self.grass = self.tilemap.green_textured
        self.green = self.tilemap.green_tile

        # where mapo drawing should start
        self.camera_offset_x = 0
        self.camera_offset_y = 0

        #text display for debugging
        self.title_label =Label(pygame.display.get_surface(),'Game Scene',45,ressources.COLORS.WHITE,(0,0),(0,0))
        self.debug_label = Label(pygame.display.get_surface(), 'Debug:', 30, ressources.COLORS.WHITE, (0, 70), (0, 0))
        self.debug_label_2 = Label(pygame.display.get_surface(), 'Debug:', 30, ressources.COLORS.WHITE, (0, 110), (0, 0))

        self.mouse_position = pygame.Vector2()

    def update(self):
        self.player.update()
        self.camera.update()

    def input(self, event):
        self.player.move(event)
        self.camera.input()

        debug_string = f'Mouse Position Screen: {str(pygame.mouse.get_pos())}'
        self.debug_label.set_text(debug_string)

    def render(self, screen: pygame.surface):
        screen.fill(ressources.COLORS.CORNFLOWER_BLUE)

        self.camera.render_context()

        self.title_label.draw()
        self.debug_label.draw()
        self.debug_label_2.draw()


