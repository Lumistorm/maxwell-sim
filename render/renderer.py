from type_hints import *


class Renderer:
    def __init__(self) -> None:
        self.queue = []
        self.clear()

    def clear(self) -> None:
        self.queue.clear()

    def add(self, surface: Surface, position: PositionInt) -> None:
        self.queue.append((surface, position))

    def render(self, dest_surface: Surface) -> Surface:
        for surface, position in self.queue:
            dest_surface.blit(surface, position)

        self.clear()

        return dest_surface
