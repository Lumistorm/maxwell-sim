import pygame
import sys
from render.renderer import Renderer
from render.window import Window
from simulation.simulation import Simulation


WINDOW_SIZE = (800, 800)
ROWS, COLUMNS = 200, 200
SPACING = 4


def run():
    renderer = Renderer()
    sim = Simulation((ROWS, COLUMNS), SPACING)
    window = Window(WINDOW_SIZE, "Maxwell's Equations Simulator", max_fps=0)
    display = pygame.Surface(WINDOW_SIZE)

    while window.running:
        window.poll_events()

        sim.step()
        sim.draw(renderer)

        renderer.render(display)
        window.tick(display)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run()
