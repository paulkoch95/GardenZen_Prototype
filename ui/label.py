import pygame
pygame.init()
from assets.ressources import COLORS, FONT
from ui import ui_component

class Label(ui_component.UIComponent):

    def __init__(self, surface: pygame.surface, text,font_size,text_color,pos, dim, connect=None):
        ui_component.UIComponent.__init__(self)
        # own render context
        self.surface = surface

        self.font_size = font_size
        self.text_color = text_color

        self.pos = pygame.Vector2(pos)
        self.dim = pygame.Vector2(dim)

        # button text to be displayed
        self.text = text

        self.background_rect = pygame.Rect(pos,dim)

        # color speci for button
        self.normal_color = COLORS.WHITE
        self.color = self.normal_color

        # representation of text rendering to be displayed on top of button
        self.font = FONT.pixel_font(self.font_size)
        self.text_surface = self.font.render(self.text,True, self.text_color)
        if self.text_surface.get_width() < self.dim[0]:
            self.background_rect.width = self.background_rect.width+self.text_surface.get_width()
    def set_text(self, text:str):
        self.text_surface = self.font.render(text,True, self.text_color)
        if self.text_surface.get_width() < self.dim[0]:
            self.background_rect.width = self.background_rect.width+self.text_surface.get_width()


    def draw(self):
        """
        All rendering task for the button go here, no logic is being done here regarding input!
        :return:
        """
        pygame.draw.rect(self.surface,self.color, self.background_rect)
        self.surface.blit(self.text_surface,(self.background_rect.center))

    def check_click(self):
        pass