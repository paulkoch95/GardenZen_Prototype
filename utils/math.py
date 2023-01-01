import pygame
import numpy as np

class ISOMETRIC:
    @classmethod
    def calculate_isometric_position(cls, camera_offset_x, camera_offset_y, drawing_offset_x, drawing_offset_y):
        trans_matrix = np.matrix(
            [[16, 32, -((camera_offset_x + 32 + drawing_offset_x) * 16) - ((camera_offset_y) * 32)],
             [-16, 32, ((camera_offset_x + 32 + drawing_offset_x) * 16) - ((camera_offset_y) * 32)],
             [0, 0, 1024]])

        tile_pos = (1 / 1024) * trans_matrix * np.matrix(
            [[pygame.mouse.get_pos()[0]], [pygame.mouse.get_pos()[1]], [1]])

class TWO_DIMENSIONAL:
    pass