import numpy as np
from numba import njit
from constants import *


@njit
def laplacian(field_x, field_y):
    width, height = field_x.shape
    laplacian_x = np.zeros_like(field_x)
    laplacian_y = np.zeros_like(field_y)
    dx_squared = (DX * DX)

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            laplacian_x[x, y] = (
                field_x[x + 1, y] +
                field_x[x - 1, y] +
                field_x[x, y + 1] +
                field_x[x, y - 1] +
                -4 * field_x[x, y]
            ) / dx_squared

            laplacian_y[x, y] = (
                field_y[x + 1, y] +
                field_y[x - 1, y] +
                field_y[x, y + 1] +
                field_y[x, y - 1] +
                -4 * field_y[x, y]
            ) / dx_squared

    return laplacian_x, laplacian_y


@njit
def gradient(scalar_field):
    width, height = scalar_field.shape

    dx = np.zeros_like(scalar_field)
    dy = np.zeros_like(scalar_field)

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            dx[x, y] = (scalar_field[x + 1, y] - scalar_field[x - 1, y]) / (2 * DX)
            dy[x, y] = (scalar_field[x, y + 1] - scalar_field[x, y - 1]) / (2 * DX)

    return dx, dy


@njit
def curl(field_x: np.ndarray, field_y: np.ndarray) -> np.ndarray:
    width, height = field_x.shape
    out = np.zeros((width, height))

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            out[x, y] = (
                (field_x[x, y + 1] - field_x[x, y]) / DX
                - (field_y[x + 1, y] - field_y[x, y]) / DX
            )
    return out
