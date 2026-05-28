import pygame
import numpy as np
from typehints import *


def draw_vector_field(surface: Surface, field: np.ndarray[float]) -> pygame.Surface:
    rows, columns, _ = field.shape

    for y in range(rows):
        for x in range(columns):
            vector_x, vector_y = field[y, x]
            pygame.draw.line(
                surface,
                (100, 100, 255),
                (x, y),
                (x + vector_x, y + vector_y),
            )

    return surface
