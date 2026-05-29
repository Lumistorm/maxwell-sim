import pygame

from render.vector_field import draw_vector_field
from render.renderer import Renderer
from render.window import Window
from simulation.simulation import Simulation


def run():

    renderer = Renderer()
    window = Window((800, 800), "Maxwell's Equations Simulator")
    sim = Simulation((25, 25))

    spacing = 32
    display = pygame.Surface((25 * spacing, 25 * spacing))

    while window.running:
        display.fill((0, 0, 0))
        sim.step()
        field_surf = draw_vector_field(display, sim.em_field.electric_field, spacing)
        renderer.blit(field_surf, (0, 0))
        display = renderer.tick(display)
        window.tick(display)

    pygame.quit()


if __name__ == '__main__':
    run()
