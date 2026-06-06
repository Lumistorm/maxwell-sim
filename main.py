import pygame
import sys
from render.renderer import Renderer
from render.window import Window
from simulation.simulation import Simulation


def run():
    rows, columns = 50, 50
    spacing = 16

    renderer = Renderer()
    window = Window((800, 800), "Maxwell's Equations Simulator", max_fps=0)
    sim = Simulation((rows, columns), spacing)

    display = pygame.Surface((800, 800))

    while window.running:
        sim.step()
        sim.draw(renderer)

        renderer.tick(display)
        window.tick(display)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run()
