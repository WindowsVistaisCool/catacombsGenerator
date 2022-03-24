from rooms import Room, RoomType
from normal import NormalRoom

class RareRoom(NormalRoom):
    def __init__(self):
        super().__init__(roomType = RoomType.CATACOMBS_RARE)