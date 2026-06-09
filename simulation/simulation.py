import time

import numpy as np
from core.em_field import EMField
from type_hints import *
from constants import *
from render.vector_field import draw_vector_field_array


class Simulation:
    def __init__(self, size: Size, spacing: int) -> None:
        self.size = size
        self.spacing = spacing

        self.em_field = EMField(size)
        self.field_surface = pygame.Surface((self.width * spacing, self.height * spacing))

        self.size = (size[0] - 1, size[1] - 1)

        self.vector_positions = self.generate_grid_positions()

        self.t = 0
        self.vx = None
        self.vy = None

    @property
    def width(self) -> int:
        return self.size[0]

    @property
    def height(self) -> int:
        return self.size[1]

    def generate_grid_positions(self) -> np.ndarray:
        grid = np.empty((*self.size, 2), dtype=np.int32)
        grid[..., 0] = np.arange(self.width)[:, None]
        grid[..., 1] = np.arange(self.height)
        grid *= self.spacing

        return grid.reshape(-1, 2)

    def step(self) -> None:
        mouse_pos = pygame.mouse.get_pos()

        mx = mouse_pos[0] // self.spacing
        my = mouse_pos[1] // self.spacing

        if pygame.key.get_just_pressed()[pygame.K_SPACE]:
            self.em_field.ex[mx, my] += 300
            self.em_field.ey[mx, my] -= 300

        self.em_field.step()
        self.vx = self.em_field.ex[:, :-1].copy()
        self.vy = self.em_field.ey[:-1, :].copy()
        charge = 250

        # # limit vector magnitude to charge strength
        mag = np.sqrt(self.vx * self.vx + self.vy * self.vy)
        mask = mag > abs(charge)

        self.vx[mask] = (self.vx[mask] / mag[mask]) * abs(charge)
        self.vy[mask] = (self.vy[mask] / mag[mask]) * abs(charge)

    def draw(self, renderer) -> None:
        self.field_surface.fill((0, 0, 0))
        draw_vector_field_array(self.field_surface, self.vx, self.vy, self.vector_positions)
        renderer.add(self.field_surface, (0, 0))
