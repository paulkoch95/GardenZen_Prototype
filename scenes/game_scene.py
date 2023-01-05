from scenes.scene import Scene
import pygame
from assets.ressources import COLORS, FONT
from ui.label import Label
from ui.widget_group import WidgetGroup
from game.map import Map
from game.player import Player
from game.camera import ScrollingCamera
from game.item import Item
pygame.init()

TILE_W = 64
TILE_H = 32

class GameScreen(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.x_m, self.y_m = 0, 0
        self.scaling_factor = 1

        # player object
        self.camera = ScrollingCamera()

        self.collectable_group = pygame.sprite.Group()

        self.map_obj = Map(self.camera)
        self.player = Player(pygame.math.Vector2(0,0), self.camera, self.collectable_group)

        self.item = Item(pygame.Vector2(30,30), self.camera, self.collectable_group, "Item 1")
        self.item2 = Item(pygame.Vector2(80,30), self.camera, self.collectable_group, "Item 2")
        self.item3 = Item(pygame.Vector2(30,70), self.camera, self.collectable_group, "Item 3")

        # where mapo drawing should start
        self.camera_offset_x = 0
        self.camera_offset_y = 0

        #text display for debugging
        self.wg = WidgetGroup()
        self.wg.add_widget("title", Label(pygame.display.get_surface(),'Game Scene',45,COLORS.WHITE,(0,0),(0,0)))
        self.wg.add_widget("debug_fps", Label(pygame.display.get_surface(), 'Debug:', 30, COLORS.WHITE, (0, 70), (0, 0)))
        self.wg.add_widget("debug_stats", Label(pygame.display.get_surface(), 'Debug:', 30, COLORS.WHITE, (0, 110), (0, 0)))
        self.wg.add_widget("player_inventory", Label(pygame.display.get_surface(), 'Debug:', 30, COLORS.BLUE, (0, 140), (0, 0)))
        self.mouse_position = pygame.Vector2()

    def update(self, dt):
        self.player.update()
        # self.camera.update()
        self.player.animate(dt)

        self.wg.widgets.get('debug_fps').set_text(
            f"frame time: {dt}"
        )

        self.wg.widgets.get('player_inventory').set_text(
            ":".join(item.name for item in self.player.inventory)
        )

    def input(self, event):
        self.player.move(event)
        self.camera.input()
        self.camera.update()

        self.wg.widgets.get('debug_stats').set_text(
            f'Mouse Position Screen: {str(pygame.mouse.get_pos())}| Player Tile: {self.player.get_tile_referenced_position()}| {self.collectable_group.sprites()}'
        )

    def render(self, screen: pygame.surface):
        screen.fill(COLORS.CORNFLOWER_BLUE)

        # game rendering
        self.camera.render_context()
        # interface rendering
        self.wg.render()


