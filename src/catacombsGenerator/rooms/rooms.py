import enum
from typing import Optional

class RoomType(enum.Enum):
    """
    Enum for Room Types
    """
    CATACOMBS_NORMAL = 1
    CATACOMBS_START = 2
    CATACOMBS_TRAP = 3
    CATACOMBS_MINIBOSS = 4
    CATACOMBS_PUZZLE = 5
    CATACOMBS_RARE = 6
    CATACOMBS_WATCHER = 7

class RoomSize(enum.Enum):
    """
    Enum for Room Sizes
    """
    # TODO: implement L rooms
    N_1X1 = 1
    N_1X2 = 2
    N_1X3 = 3
    N_1X4 = 4
    N_2X2 = 5
    # N_L = 6
    SPECIAL = 1

    @classmethod
    def getRoomSizeByType(cls, type: RoomType) -> Optional[tuple[int, int, Optional[int]]]:
        """
        Returns the room size of a room type
        @param type: The room type
        :return: The room size
        """
        sizes = {
            cls.N_1X1: (1, 1),
            cls.N_1X2: (1, 2),
            cls.N_1X3: (1, 3),
            cls.N_1X4: (1, 4),
            cls.N_2X2: (2, 2),
            # cls.N_L: (2, 2, 1),
            cls.SPECIAL: (1, 1)
        }
        try:
            return sizes[type]
        except KeyError:
            return None

class Room:
    def __init__(self, type: RoomType, roomSize: RoomSize):
        self.type = type
        self.roomSize = roomSize
    
    def getType(self) -> RoomType:
        return self.type
    
    def getRoomSize(self) -> tuple[int, int]:
        return RoomSize.getRoomSizeByType(self.roomSize)
    