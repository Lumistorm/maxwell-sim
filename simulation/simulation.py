import pygame
import numpy as np
from typehints import *


class Simulation:
    def __init__(self, size: Size) -> None:
        self.size = size

    @property
    def width(self) -> int:
        return self.size[0]

    @property
    def height(self) -> int:
        return self.size[1]
