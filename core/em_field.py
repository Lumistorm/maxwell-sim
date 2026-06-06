import numpy as np
from type_hints import *


class EMField:
    def __init__(self, size: Size) -> None:
        self.electric_field = np.zeros((*size, 2), np.float32)
