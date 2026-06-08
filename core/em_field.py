import numpy as np
from numba import njit
from type_hints import *
from core.operators import *
from constants import *


class EMField:
    def __init__(self, size: Size) -> None:
        self.ex = np.zeros((size[0] - 1, size[1]), np.float32)
        self.ey = np.zeros((size[0], size[1] - 1), np.float32)
        self.bz = np.zeros((size[0] - 1, size[1] - 1), np.float32)

    def step(self):
        faraday(self.ex, self.ey, self.bz)
        ampere_maxwell(self.ex, self.ey, self.bz)


@ njit
def faraday(ex: np.ndarray, ey: np.ndarray, bz: np.ndarray) -> None:
    width, height = bz.shape

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            d_ex_dy = (ex[x, y + 1] - ex[x, y]) / DX
            d_ey_dx = (ey[x + 1, y] - ey[x, y]) / DX
            curl_e = d_ex_dy - d_ey_dx
            bz[x, y] += DELTA_TIME * curl_e


@ njit
def ampere_maxwell(ex: np.ndarray, ey: np.ndarray, bz: np.ndarray) -> None:
    width, height = bz.shape

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            ex[x, y] += DELTA_TIME * (bz[x, y] - bz[x, y - 1]) / DX
            ey[x, y] -= DELTA_TIME * (bz[x, y] - bz[x - 1, y]) / DX
