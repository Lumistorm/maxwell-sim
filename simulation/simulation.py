import numpy as np
from core.em_field import EMField
from type_hints import *
from constants import *
from render.vector_field import draw_vector_field_array


class Simulation:
    def __init__(self, size: Size, spacing: int) -> None:
        self.size = size
        self.spacing = spacing

        self.vector_positions = self.generate_grid_positions()

        self.em_field = EMField(size)
        self.field_surface = pygame.Surface((self.width * spacing, self.height * spacing))

    @property
    def width(self) -> int:
        return self.size[0]

    @property
    def height(self) -> int:
        return self.size[1]

    def generate_grid_positions(self) -> np.ndarray:
        grid = np.empty((*self.size, 2), dtype=np.int32)
        grid[..., 0] = np.arange(self.width)
        grid[..., 1] = np.arange(self.height)[:, None]
        grid *= self.spacing

        return grid.reshape(-1, 2)

    def step(self) -> None:
        charge = -20
        k = 20

        grid_y, grid_x = np.indices(self.size)
        mouse_pos = pygame.mouse.get_pos()

        dx = mouse_pos[0] / self.spacing - grid_x
        dy = mouse_pos[1] / self.spacing - grid_y

        r = np.sqrt(dx * dx + dy * dy)
        r3 = r * r * r + EPSILON

        vx = k * (charge * dx) / r3
        vy = k * (charge * dy) / r3

        # limit vector magnitude to charge strength
        mag = np.sqrt(vx * vx + vy * vy)
        mask = (mag > 0) & (mag < 1)
        vx[mask] = (vx[mask] / mag[mask])
        vy[mask] = (vy[mask] / mag[mask])

        mask = mag > abs(charge)

        vx[mask] = (vx[mask] / mag[mask]) * abs(charge)
        vy[mask] = (vy[mask] / mag[mask]) * abs(charge)

        self.em_field.electric_field[:, :, 0] = vy
        self.em_field.electric_field[:, :, 1] = vx

    def draw(self, renderer) -> None:
        self.field_surface.fill((0, 0, 0))
        draw_vector_field_array(self.field_surface, self.em_field.electric_field, self.vector_positions)
        renderer.blit(self.field_surface, (0, 0))
