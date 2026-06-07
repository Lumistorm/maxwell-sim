import numpy as np
from numba import njit
from type_hints import *


def draw_vector_field(surface: Surface, field: np.ndarray, start_position) -> Surface:
    offset = field[..., ::-1].astype(np.int32)

    end_position = start_position + offset.reshape(-1, 2)

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


def draw_vector_field_array(surface: Surface, field: np.ndarray, start_position) -> Surface:

    offset = field[..., ::-1].astype(np.int32)

    end_position = start_position + offset.reshape(-1, 2)

    color = (100, 100, 255)
    pixels = pygame.surfarray.pixels3d(surface)
    print(type(pixels))

    rasterize_lines(pixels, start_position, end_position, *color)
    del pixels

    return surface


@njit(cache=True, fastmath=True)
def rasterize_lines(pixels, starts, ends, r, g, b) -> np.ndarray:
    width, height, _ = pixels.shape

    num_lines = starts.shape[0]

    for index in range(num_lines):
        start_x = starts[index, 0]
        start_y = starts[index, 1]
        end_x = ends[index, 0]
        end_y = ends[index, 1]

        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)
        sx = 1 if start_x < end_x else -1
        sy = 1 if start_y < end_y else -1

        error = dx - dy

        x, y = start_x, start_y

        while True:
            if x == end_x and y == end_y:
                break

            if 0 <= x < width and 0 <= y < height:
                pixels[x, y, 0] = r
                pixels[x, y, 1] = g
                pixels[x, y, 2] = b

            error_2 = 2 * error

            if error_2 > -dy:
                error -= dy
                x += sx

            if error_2 < dx:
                error += dx
                y += sy

    return pixels
