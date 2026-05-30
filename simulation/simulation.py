import pygame
import numpy as np
from core.em_field import EMField
from type_hints import *
from constants import *


class Simulation:
    def __init__(self, shape: Size) -> None:
        self.shape = shape
        self.em_field = EMField(shape)

    @property
    def width(self) -> int:
        return self.shape[0]

    @property
    def height(self) -> int:
        return self.shape[1]

    def step(self):
        grid_y, grid_x = np.indices(self.shape)
        mouse_pos = pygame.mouse.get_pos()

        dy = mouse_pos[1] / 8 - grid_y
        dx = mouse_pos[0] / 8 - grid_x
        r = np.sqrt(dx * dx + dy * dy)
        r2 = r * r + EPSILON

        self.em_field.electric_field[:, :, 0] = (dy / r2) * -50
        self.em_field.electric_field[:, :, 1] = (dx / r2) * -50
