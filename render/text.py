import pygame
from typehints import *

pygame.init()
font = pygame.font.Font(None, 30)

last_text = None
background = None


def draw_text(surface: pygame.Surface, data, positon: Position) -> Surface:
    global last_text, background

    if data != last_text:
        surf_cache = font.render(str(data), True, 'white')
        background = pygame.Surface(surf_cache.get_size())
        background.fill((0, 0, 0))
        background.blit(surf_cache, (0, 0))

        last_text = data

    surface.blit(background, positon)

    return surface
