import pygame
import numpy as np
import sys
import cProfile
from render.vector_field import draw_vector_field, draw_vector_field_array
from render.renderer import Renderer
from render.window import Window
from simulation.simulation import Simulation
import pstats


def run():

    renderer = Renderer()
    window = Window((800, 800), "Maxwell's Equations Simulator", max_fps=1000)

    rows, columns = 100, 100
    spacing = 8

    sim = Simulation((rows, columns))

    start_position = np.empty((rows, columns, 2))
    start_position[..., 0] = np.arange(columns)
    start_position[..., 1] = np.arange(rows)[:, None]
    start_position *= spacing
    start_position = start_position.reshape(-1, 2).astype(np.int32)

    field_surf = pygame.Surface((rows * spacing, columns * spacing))

    while window.running:
        field_surf.fill((0, 0, 0))
        sim.step()

        field_surf = draw_vector_field_array(field_surf, sim.em_field.electric_field, start_position)

        renderer.blit(field_surf, (0, 0))
        display = renderer.tick(field_surf)
        window.tick(display)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run()
