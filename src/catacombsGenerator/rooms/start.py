from rooms import Room, RoomType

class StartingRoom(Room):
    def __init__(self):
        super.__init__(RoomType.CATACOMBS_START)