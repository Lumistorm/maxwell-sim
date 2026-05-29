import pygame


type Position = tuple[float, float] | list[float]
type PositionInt = tuple[int, int] | list[int]

type Size = tuple[int, int]

type RGB = tuple[int, int, int]
type RGBA = tuple[int, int, int, int]
type Color = RGB | RGBA

type Surface = pygame.Surface
