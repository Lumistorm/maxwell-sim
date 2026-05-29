import pygame
import numpy as np
from type_hints import *


def draw_vector_field(surface: Surface, field: np.ndarray[float], spacing: int) -> pygame.Surface:
    rows, columns, _ = field.shape
    y_axis = np.arange(rows) * spacing
    x_axis = np.arange(columns) * spacing
    grid = np.meshgrid(x_axis, y_axis)
    start_position = np.stack(grid, axis=-1)

    vector_offset = field[..., ::-1].astype(int)
    end_position = start_position + vector_offset

    start_position = start_position.reshape(-1, 2)
    end_position = end_position.reshape(-1, 2)

    for start, end in zip(start_position, end_position):
        pygame.draw.line(
            surface,
            (100, 100, 255),
            start,
            end,
        )

    return surface
