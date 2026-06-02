import pygame
import numpy as np
from numba import njit
from type_hints import *


def draw_vector_field(surface: Surface, field: np.ndarray[float], start_position) -> Surface:
    offset_ints = field.astype(np.int32)
    offset = offset_ints[..., ::-1]

    end_position = start_position + offset

    start_position = start_position.reshape(-1, 2)
    end_position = end_position.reshape(-1, 2)
    start_position = zip(start_position[:, 0].tolist(), start_position[:, 1].tolist())
    end_position = zip(end_position[:, 0].tolist(), end_position[:, 1].tolist())

    draw_line = pygame.draw.line
    color = (100, 100, 255)

    for start, end in zip(start_position, end_position):
        draw_line(
            surface,
            color,
            start,
            end,
        )

    return surface


def draw_vector_field_array(surface: Surface, field: np.ndarray[float], start_position) -> Surface:
    offset_ints = field.astype(np.int32)
    offset = offset_ints[..., ::-1]

    end_position = start_position + offset

    start_position = start_position.reshape(-1, 2)
    end_position = end_position.reshape(-1, 2)
    start_position = start_position.astype(np.int32)
    end_position = end_position.astype(np.int32)

    color = (100, 100, 255)
    pixels = pygame.surfarray.pixels3d(surface)
    rasterize_lines(pixels, start_position, end_position, *color)
    del pixels

    surface.unlock()

    return surface


@njit(parallel=True, cache=True)
def rasterize_lines(pixels, starts, ends, r, g, b):
    num_lines = starts.shape[0]
    width, height, _ = pixels.shape

    for idx in range(num_lines):
        start_x, start_y = starts[idx]
        end_x, end_y = ends[idx]

        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)
        sx = 1 if start_x < end_x else -1
        sy = 1 if start_y < end_y else -1

        error = dx - dy

        x, y = start_x, start_y

        while True:
            if 0 <= x < width and 0 <= y < height:
                pixels[x, y, 0] = r
                pixels[x, y, 1] = g
                pixels[x, y, 2] = b

            if x == end_x and y == end_y:
                break

            error_2 = 2 * error

            if error_2 > -dy:
                error -= dy
                x += sx

            if error_2 < dx:
                error += dx
                y += sy
