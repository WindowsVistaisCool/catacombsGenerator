import enum

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

class Room:
    def __init__(self, type: RoomType):
        self.type = type
    
    def getType(self) -> RoomType:
        return self.type
    
    