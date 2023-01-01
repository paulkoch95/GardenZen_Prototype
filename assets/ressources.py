import pygame
pygame.init()

class COLORS:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    CORNFLOWER_BLUE=(100, 149, 237)

class TILEMAP:
    pass

class FONT:
    # @ ALT + L
    @classmethod
    def pixel_font(cls, size: int) -> pygame.font.Font:
        font = pygame.font.Font('assets/font/alterebro-pixel-font.ttf', size)
        return font
