import numpy as np
from core.em_field import EMField
from type_hints import *
from constants import *


class Simulation:
    def __init__(self, shape: Size, spacing) -> None:
        self.shape = shape
        self.spacing = spacing

        grid = np.empty((*self.shape, 2))
        grid[..., 0] = np.arange(self.width)
        grid[..., 1] = np.arange(self.height)[:, None]
        grid *= spacing
        self.grid_positions = grid.reshape(-1, 2).astype(np.int32)

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

        dy = mouse_pos[1] / self.spacing - grid_y
        dx = mouse_pos[0] / self.spacing - grid_x
        r = np.sqrt(dx * dx + dy * dy)
        r2 = r * r + EPSILON

        vy = (dy / r2) * -30
        vx = (dx / r2) * -30

        self.em_field.electric_field[:, :, 0] = vy
        self.em_field.electric_field[:, :, 1] = vx
