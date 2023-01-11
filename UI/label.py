import pygame
pygame.init()
from assets.ressources import COLORS, FONT
from UI.UserInterface import UserInterface

class Label(pygame.sprite.Sprite):

    def __init__(self, ui: pygame.sprite.Group, text, font_size, text_color, background_color, pos, padding: pygame.Vector2 = pygame.Vector2(20, 20)):
        super().__init__(ui)

        self.text = text
        self.font_size = font_size
        self.font = FONT.pixel_font(self.font_size)
        self.text_color = text_color
        self.background_color = background_color

        self.image = pygame.Surface(self.font.size(self.text))

        self.padding = pygame.Vector2(padding)

        self.pos = pygame.Vector2(pos)
        self.dim = self.font.size(self.text)
        self.rect = pygame.Rect(self.pos, self.dim)
        self.rect.inflate_ip(self.padding)

        self.draw()

    def resize(self, new_width, new_height):
        self.image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)

    def set_text(self, text: str):
        self.dim = self.font.size(self.text)
        self.rect = pygame.Rect(self.pos, self.dim)
        self.rect.inflate_ip(self.padding)
        self.text = text
        self.draw()

    def draw(self):
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # pygame.draw.rect(self.image, self.background_color, ((0,0), self.rect.size))
        text_tex = self.font.render(self.text, True, self.text_color)
        self.image.blit(text_tex, (self.padding // 2))

