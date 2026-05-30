import pygame
import numpy as np
from type_hints import *


def draw_vector_field(surface: Surface, field: np.ndarray[float], spacing: int) -> Surface:
    rows, columns, _ = field.shape

    start_position = np.empty((rows, columns, 2))
    start_position[..., 0] = np.arange(columns)
    start_position[..., 1] = np.arange(rows)[:, None]
    start_position *= spacing

    offset_ints = field.astype(np.int32)
    offset = offset_ints[..., ::-1]

    end_position = start_position + offset

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

