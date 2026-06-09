from render.text import draw_text
from type_hints import *


class Window:
    def __init__(self, size: Size, caption: str, max_fps: int = 120) -> None:
        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        self.max_fps = max_fps
        self.delta_time = 0
        self.clock = pygame.time.Clock()

        self.fps_timer = 0
        self.fps_text = ''
        self.fps = 0

        self.running = True

    def fps(self) -> float:
        return self.clock.get_fps()

    def tick(self, surface) -> None:
        self.window.blit(surface)
        self.draw_fps()

        pygame.display.flip()
        self.delta_time = self.clock.tick(self.max_fps) * 0.001

    def draw_fps(self) -> None:
        self.fps_timer -= 1

        if self.delta_time > 0:
            fps = 1 / self.delta_time
            self.fps = self.fps * (1 - 0.05) + fps * 0.05

        if self.fps_timer < 0:
            self.fps_text = f"FPS: {round(self.fps)}"
            self.fps_timer = 60

        draw_text(self.window, self.fps_text, (20, 20))

    def poll_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
