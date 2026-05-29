import numpy as np
from typehints import *


class EMField:
    def __init__(self, shape: Size) -> None:
        self.electric_field = np.zeros((*shape, 2), np.float32)
