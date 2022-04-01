from enum import Enum


class RbCol(Enum):
    Col1 = 1
    Col2 = 2
    Col3 = 3

class RbRow(Enum):
    Row1 = 1
    Row2 = 2
    Row3 = 3

class RbSlice(Enum):
    Slice1 = 1
    Slice2 = 2
    Slice3 = 3


class RBMove(Enum):
    MoveUp = 1
    MoveDown = 2
    MoveRight = 3
    MoveLeft = 4
    MoveClock = 5
    MoveClockAnti = 6


class RbFace(Enum):
    FaceBottom = 1
    FaceUp = 2
    FaceFront = 3
    FaceBack = 4
    FaceLeft = 5
    FaceRight = 6
    
    
