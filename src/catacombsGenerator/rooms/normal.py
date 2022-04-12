import enum
from rooms import Room, RoomType, RoomSize
from typing import Union, Optional

class NormalRoom(Room):
    def __init__(self, roomSize: rooms.RoomSize, roomParams: tuple[Union[NormalParams, SpecialParams, str]]):
        super().__init__(RoomType.CATACOMBS_NORMAL)
        self.roomSize = roomSize
        self.params = None # TODO: implement handler

class NormalParams(enum.Enum):
    REQUIRES_MINIBOSS = 0
    EXTRA_MINIBOSS = 1
    
class SpecialParams(enum.Enum):
    COMBINATION = 0
