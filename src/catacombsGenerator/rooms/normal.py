from rooms import Room, RoomType

class NormalRoom(Room):
    def __init__(self, *, roomType: RoomType = RoomType.CATACOMBS_NORMAL):
        super().__init__(roomType)

# TODO: Populate
# class OneByOneNormalRoom(Normal)