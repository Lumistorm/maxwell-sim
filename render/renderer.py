import pygame
import numpy as np
from typehints import *


class Renderer:
    def __init__(self) -> None:
        self.render_queue = []
        self.reset()

    def reset(self) -> None:
        self.render_queue = []

    def blit(self, surface: Surface, position: PositionInt) -> None:
        self.render_queue.append((surface, position))

    def tick(self, dest_surfaces: Surface) -> Surface:
        for surface, position in self.render_queue:
            dest_surfaces.blit(surface, position)

        self.reset()

        return dest_surfaces
