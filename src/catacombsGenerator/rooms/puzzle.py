import enum
from rooms import Room, RoomType

class PuzzleType(enum.Enum):
    """
    Enum for puzzle types.
    """
    CATACOMBS_CREEPERBEAMS = 0
    CATACOMBS_3WEIRDOS = 1
    CATACOMBS_TICTACTOE = 2
    CATACOMBS_HIGHERLOWER = 3
    CATACOMBS_WATERBOARD = 4
    CATACOMBS_TELEPORTPADS = 5
    CATACOMBS_BOULDER = 6
    CATACOMBS_ICEFILL = 7
    CATACOMBS_ICEPATH = 8
    CATACOMBS_QUIZ = 9
    CATACOMBS_BOMBDEFUSE = 10

class Puzzle(Room):
    def __init__(self, puzzleType: PuzzleType):
        super.__init__(RoomType.CATACOMBS_PUZZLE)
        self.puzzleType = puzzleType
    
    def getPuzzleType(self) -> PuzzleType:
        return self.puzzleType