import enum
from rooms import Room, RoomType

class MinibossType(enum.Enum):
    """
    Enum for Miniboss Types
    """
    DRAGON_HEAD = 0
    SHADOW_ASSASSIN = 1
    TWO_WALL_SIDES = 2
    MINI_STADIUM = 3
    CUSTOM = 4

class MinibossRoom(Room):
    def __init__(self, type: MinibossType):
        super.__init__(RoomType.CATACOMBS_MINIBOSS)
        self.miniBossType = type