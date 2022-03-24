from rooms import Room, RoomType

class MinibossRoom(Room):
    def __init__(self):
        super.__init__(RoomType.CATACOMBS_MINIBOSS)