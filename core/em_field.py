import numpy as np
from type_hints import *


class EMField:
    def __init__(self, shape: Size) -> None:
        self.electric_field = np.zeros((*shape, 2), np.float32)
