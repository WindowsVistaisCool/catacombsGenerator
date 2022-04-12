import enum
from typing import Optional

class FloorSize(enum.Enum):
    """
    Enum for general floor sizes
    """
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    HUGE = 3

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

    @classmethod
    def checkMasterMode(cls, floorType: FloorType) -> Optional[bool]:
        """
        Checks if a floor type is a master mode floor type
        @param floorType: The floor type
        :return: True if the floor type is a master mode floor type, False otherwise
        """
        return floorType in [cls.CATACOMBS_MASTER_1, cls.CATACOMBS_MASTER_2, cls.CATACOMBS_MASTER_3, cls.CATACOMBS_MASTER_4, cls.CATACOMBS_MASTER_5, cls.CATACOMBS_MASTER_6, cls.CATACOMBS_MASTER_7]

    @classmethod
    def getFloorSize(cls, floorType: FloorType) -> FloorSize:
        floorConvertMap = {
            cls.CATACOMBS_MASTER_1: cls.CATACOMBS_NORMAL_1,
            cls.CATACOMBS_MASTER_2: cls.CATACOMBS_NORMAL_2,
            cls.CATACOMBS_MASTER_3: cls.CATACOMBS_NORMAL_3,
            cls.CATACOMBS_MASTER_4: cls.CATACOMBS_NORMAL_4,
            cls.CATACOMBS_MASTER_5: cls.CATACOMBS_NORMAL_5,
            cls.CATACOMBS_MASTER_6: cls.CATACOMBS_NORMAL_6,
            cls.CATACOMBS_MASTER_7: cls.CATACOMBS_NORMAL_7,
        }
        floorSizingMap = { # TODO: check these in game later
            cls.CATACOMBS_ENTRANCE: FloorSize.SMALL,
            cls.CATACOMBS_NORMAL_1: FloorSize.SMALL,
            cls.CATACOMBS_NORMAL_2: FloorSize.MEDIUM,
            cls.CATACOMBS_NORMAL_3: FloorSize.MEDIUM,
            cls.CATACOMBS_NORMAL_4: FloorSize.MEDIUM,
            cls.CATACOMBS_NORMAL_5: FloorSize.LARGE,
            cls.CATACOMBS_NORMAL_6: FloorSize.LARGE,
            cls.CATACOMBS_NORMAL_7: FloorSize.HUGE,
        }
        return floorSizingMap[floorConvertMap[floorType] if checkMasterMode(floorType) else floorType]

class Floor:
    def __init__(self, type: FloorType, rooms: list[Room]):
        self.type = type
        self.rooms = rooms
    
    def getType(self) -> FloorType:
        return self.type
    
    def getAllRooms(self) -> list[Room]:
        return self.rooms

class FloorParams:
    def __init__(self): # TODO: Populate.
        pass