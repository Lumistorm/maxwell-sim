import pygame
import sys
from render.vector_field import draw_vector_field, draw_vector_field_array
from render.renderer import Renderer
from render.window import Window
from simulation.simulation import Simulation


def run():
    rows, columns = 25, 25
    spacing = 32

    renderer = Renderer()
    window = Window((800, 800), "Maxwell's Equations Simulator", max_fps=1000)
    sim = Simulation((rows, columns), spacing)

    field_surf = pygame.Surface((rows * spacing, columns * spacing))

    while window.running:
        field_surf.fill((0, 0, 0))
        sim.step()

        field_surf = draw_vector_field_array(field_surf, sim.em_field.electric_field, sim.grid_positions)

        renderer.blit(field_surf, (0, 0))
        display = renderer.tick(field_surf)
        window.tick(display)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run()
