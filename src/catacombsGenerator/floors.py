import enum

class FloorType(enum.Enum):
    """
    Enum for floor types.
    """
    CATACOMBS_ENTRANCE = 0
    CATACOMBS_NORMAL_1 = 1
    CATACOMBS_NORMAL_2 = 2
    CATACOMBS_NORMAL_3 = 3
    CATACOMBS_NORMAL_4 = 4
    CATACOMBS_NORMAL_5 = 5
    CATACOMBS_NORMAL_6 = 6
    CATACOMBS_NORMAL_7 = 7
    CATACOMBS_MASTER_1 = 8
    CATACOMBS_MASTER_2 = 9
    CATACOMBS_MASTER_3 = 10
    CATACOMBS_MASTER_4 = 11
    CATACOMBS_MASTER_5 = 12
    CATACOMBS_MASTER_6 = 13
    CATACOMBS_MASTER_7 = 14
    CUSTOM = 15

class Floor:
    def __init__(type: FloorType, rooms: list[Room]):
        self.type = type
        self.rooms = rooms
    
    def getType(self) -> FloorType:
        return self.type
    
    def getAllRooms(self) -> list[Room]:
        return self.rooms

class FloorParams:
    def __init__(self): # TODO: Populate.
        pass

# TODO: Add all FloorType classes.