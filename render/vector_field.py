import pygame
import numpy as np
from typehints import *


def draw_vector_field(surface: Surface, field: np.ndarray[float], spacing: int) -> pygame.Surface:
    rows, columns, _ = field.shape

    for y in range(rows):
        for x in range(columns):
            vector_y, vector_x = field[y, x]
            vector_x = int(vector_x)
            vector_y = int(vector_y)
            pygame.draw.line(
                surface,
                (100, 100, 255),
                (x * spacing, y * spacing),
                (x * spacing + vector_x, y * spacing + vector_y),
            )

    return surface
