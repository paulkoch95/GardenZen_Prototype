import pygame
from assets import ressources
pygame.init()

def draw_hitbox(ref_surface: pygame.Surface, *surfaces: pygame.Surface):
 for s in surfaces:
     print("Offset: ", s.get_abs_offset())
     pygame.draw.rect(ref_surface, ressources.COLORS.BLUE, rect=s.get_bounding_rect(),width=2)