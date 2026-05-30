import pygame
import numpy as np
from render.text import draw_text


class Window:
    def __init__(self, size: list | tuple, caption: str, max_fps=120):
        self.size = size
        self.max_fps = max_fps
        self.delta_time = 0

        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()

        self.running = True
        self.max = []

    def fps(self):
        return self.clock.get_fps()

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def tick(self, surface):
        self.window.fill((0, 0, 0))

        self.handle_events()
        self.window.blit(pygame.transform.scale(surface, self.window.size), (0, 0))
        self.draw_fps()

        pygame.display.flip()
        self.delta_time = self.clock.tick(self.max_fps) * 0.001

    def draw_fps(self):
        fps_round = round(self.fps())
        self.max.append(fps_round)
        fps_text = f"FPS: {np.max(self.max)}"
        draw_text(self.window, fps_text, (20, 20))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
