from scenes.scene import Scene
import pygame
from assets import colors
from ui.label import Label
from game.level import Level
from game.tilemap import Tilemap
from game.player import Player
from debug import tools
import numpy as np
pygame.init()

TILE_W = 64
TILE_H = 32

class GameScreen(Scene):

    def __init__(self):
        Scene.__init__(self)
        # placegholder surface for the current map
        self.map_surface = pygame.Surface((1000, 500), pygame.SRCALPHA)
        self.w,self.h = self.map_surface.get_width(),self.map_surface.get_height()
        self.x_m, self.y_m = 0,0

        # player object
        self.player = Player(pygame.display.get_surface())

        # levelobj holding infor about certain tiles a map coords
        self.level_obj = Level()
        self.level = self.level_obj.get_level_data()

        # tilemap giving image of the tile to be rendered
        self.tilemap = Tilemap()
        # self.grass = self.tilemap.grass_tile
        self.grass = self.tilemap.green_textured
        self.green = self.tilemap.green_tile

        # where mapo drawing should start
        self.camera_offset_x = 0
        self.camera_offset_y = 0

        self.drawing_offset_x = 5*TILE_W
        self.drawing_offset_y = 0
        # create map //TODO replace by map gen
        self.create_array()

        #text display for debugging
        self.title_label =Label(pygame.display.get_surface(),'Game Scene',45,colors.WHITE,(0,0),(0,0))
        self.debug_label = Label(pygame.display.get_surface(), 'Debug:', 30, colors.WHITE, (0, 70), (0, 0))
        self.debug_label_2 = Label(pygame.display.get_surface(), 'Debug:', 30, colors.WHITE, (0, 110), (0, 0))

        self.mouse_position = pygame.Vector2()

    def update(self):
        self.x_m, self.y_m = pygame.mouse.get_rel()

    def input(self,event):
        for e in event:
            pass

        if pygame.mouse.get_pressed()[0]:
            self.mouse_position = pygame.Vector2(self.x_m, self.y_m)
            self.camera_offset_x += self.x_m
            self.camera_offset_y += self.y_m
        else:
            self.level_obj.set_level_data(1, 2, 0)
            self.create_array()

        # test 123
        debug_string = f'Mouse Position Screen: {str(pygame.mouse.get_pos())} | {self.mouse_position}'

        trans_matrix = np.matrix([[16, 32, -((self.camera_offset_x + 32 + self.drawing_offset_x) * 16) - ((self.camera_offset_y) * 32)],
                                  [-16, 32, ((self.camera_offset_x + 32 + self.drawing_offset_x) * 16) - ((self.camera_offset_y) * 32)],
                                  [0, 0, 1024]])

        tile_pos = (1 / 1024) * trans_matrix * np.matrix([[pygame.mouse.get_pos()[0]], [pygame.mouse.get_pos()[1]], [1]])

        self.debug_label.set_text(debug_string)
        self.debug_label_2.set_text(f'Offset: {self.camera_offset_x,self.camera_offset_y} Tile Pos: x:{np.floor((tile_pos[0])),np.floor(tile_pos[1])} Offset: {self.camera_offset_x,self.camera_offset_y}')

    def create_array(self):
        self.map_surface.fill((0, 0, 0, 0))

        self.font = pygame.font.Font(None, 15)
        # text_surface = self.font.render('test', True, colors.RED)

        for x in range(len(self.level[0])-1,-1,-1):
            for y in range(len(self.level)):
                if self.level[x][y]==1:
                    text_surface = self.font.render(f'{x,y}', True, colors.RED)
                    self.map_surface.blit(self.grass, (self.drawing_offset_x + (x - y) * (TILE_W / 2), (x + y) * TILE_H / 2))
                    self.map_surface.blit(text_surface, (self.drawing_offset_x + (x - y) * (TILE_W / 2) + (0.5 * TILE_W), ((x + y) * TILE_H / 2) + (0.5 * TILE_H)))
                else:
                    self.map_surface.blit(self.green, ((5 * TILE_W) + (x - y) * (TILE_W / 2), (x + y) * TILE_H / 2))

    def render(self, screen: pygame.surface):
        screen.fill(colors.CORNFLOWER_BLUE)
        # test_surface_scaled = pygame.transform.scale(self.test_surface,(self.w,self.h))
        screen.blit(self.map_surface, (self.camera_offset_x, self.camera_offset_y))
        # tools.draw_hitbox(pygame.display.get_surface(), self.test_surface,self.title_label.surface)
        self.title_label.draw()
        self.debug_label.draw()
        self.debug_label_2.draw()
        self.player.render()


