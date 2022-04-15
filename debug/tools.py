import pygame
from assets import colors
pygame.init()

def draw_hitbox(ref_surface: pygame.Surface, *surfaces: pygame.Surface):
 for s in surfaces:
     pygame.draw.rect(ref_surface, colors.BLUE, rect=s.get_bounding_rect(),width=2)