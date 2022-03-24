from rooms import Room, RoomType

class TrapRoom(Room):
    def __init__(self):
        super.__init__(RoomType.CATACOMBS_TRAP)