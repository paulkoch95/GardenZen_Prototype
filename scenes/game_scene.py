from scenes.scene import Scene
import pygame
from assets import colors
from ui.label import  Label
from game.level import Level
from game.tilemap import Tilemap
from debug import tools
import numpy as np
pygame.init()

TILE_W = 64
TILE_H = 32

class GameScreen(Scene):

    def __init__(self):
        Scene.__init__(self)
        # placegholder surface for the current map
        self.test_surface = pygame.Surface((1000,500),pygame.SRCALPHA)
        self.w,self.h = self.test_surface.get_width(),self.test_surface.get_height()
        # amount to zoomed in when using mousewheel
        self.scrolling_fac = 1

        # levelobj holding infor about certain tiles a map coords
        self.level_obj = Level()
        self.level = self.level_obj.get_level_data()

        # tilemap giving image of the tile to be rendered
        self.tilemap = Tilemap()
        # self.grass = self.tilemap.grass_tile
        self.grass = self.tilemap.green_textured
        self.green = self.tilemap.green_tile

        # where mapo drawing should start, //TODO replace by camera
        self.map_offset_x = 0
        self.map_offset_y = 0

        self.drawing_offset_x = 5*TILE_W
        self.drawing_offset_y = 0
        # create map //TODO replace by map gen
        self.create_array()

        #text display for debugging
        self.title_label =Label(pygame.display.get_surface(),'Game Scene',45,colors.WHITE,(0,0),(0,0))
        self.debug_label = Label(pygame.display.get_surface(), 'Debug:', 30, colors.WHITE, (0, 70), (0, 0))
        self.debug_label_2 = Label(pygame.display.get_surface(), 'Debug:', 30, colors.WHITE, (0, 110), (0, 0))


    def update(self):
        pass

    def input(self,event):
        for e in event:
            if e.type == pygame.MOUSEWHEEL:
                if e.y >=0:
                    self.w*=1+(.005*e.y**2)
                    self.h*=1+(.005*e.y**2)
                elif e.y < 0:
                    self.w*=1-(.005*e.y**2)
                    self.h*=1-(.005*e.y**2)
                else:
                    self.scrolling_fac = 1
        if pygame.mouse.get_pressed()[0]:
            self.x_m, self.y_m = pygame.mouse.get_rel()
            self.map_offset_x += self.x_m
            self.map_offset_y += self.y_m
        else:
            self.level_obj.set_level_data(1, 2, 0)
            self.create_array()

        # test 123
        debug_string = f'Mouse Position Screen: {str(pygame.mouse.get_pos())} | Scrollfactors: {self.w,self.h}'

        trans_matrix = np.matrix([[16, 32, -((self.map_offset_x+32+self.drawing_offset_x) *16) - ((self.map_offset_y)*32)],
                                  [-16, 32, ((self.map_offset_x+32+self.drawing_offset_x) * 16) -((self.map_offset_y)*32)],
                                  [0, 0, 1024]])

        tile_pos = (1 / 1024) * trans_matrix * np.matrix([[pygame.mouse.get_pos()[0]], [pygame.mouse.get_pos()[1]], [1]])

        self.debug_label.set_text(debug_string)
        self.debug_label_2.set_text(f'Offset: {self.map_offset_x,self.map_offset_y} Tile Pos: x:{np.floor((tile_pos[0])),np.floor(tile_pos[1])} Offset: {self.map_offset_x,self.map_offset_y}')

    def create_array(self):
        #img = pygame.image.load('assets/tile_dev.png')
        self.test_surface.fill((0,0,0,0))

        self.font = pygame.font.Font(None, 15)
        text_surface = self.font.render('test', True, colors.RED)

        for x in range(len(self.level[0])-1,-1,-1):
            for y in range(len(self.level)):

                if self.level[x][y]==1:
                    text_surface = self.font.render(f'{x,y}', True, colors.RED)
                    self.test_surface.blit(self.grass,(self.drawing_offset_x+(x-y)*(TILE_W/2),(x+y)*TILE_H/2))
                    self.test_surface.blit(text_surface, (self.drawing_offset_x+(x-y)*(TILE_W/2)+(0.5*TILE_W),((x+y)*TILE_H/2)+(0.5*TILE_H)))
                else:
                    self.test_surface.blit(self.green,((5*TILE_W)+(x-y)*(TILE_W/2),(x+y)*TILE_H/2))

    def render(self, screen: pygame.surface):
        screen.fill(colors.CORNFLOWER_BLUE)
        # test_surface_scaled = pygame.transform.scale(self.test_surface,(self.w,self.h))
        screen.blit(self.test_surface,(self.map_offset_x,self.map_offset_y))
        # screen.blit(self.test_surface_scaled,(self.map_offset_x,self.map_offset_y))
        # tools.draw_hitbox(pygame.display.get_surface(), self.test_surface,self.title_label.surface)
        # screen.blit(self.test_surface,(0,0))
        self.title_label.draw()
        self.debug_label.draw()
        self.debug_label_2.draw()


