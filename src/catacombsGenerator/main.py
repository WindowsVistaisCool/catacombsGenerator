import random
import floors
from rooms import *

class RawGenerator:
    def __init__(xMax: int, yMax: int, floorParams: floors.FloorParams):
        self.xMax = xMax
        self.yMax = yMax
        self.floorParams = floorParams