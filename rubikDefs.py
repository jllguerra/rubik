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


class RbMove(Enum):
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


class RbColor(Enum):
    ColorOrange = 1
    ColorRed = 2
    ColorWhite = 3
    ColorYellow = 4
    ColorBlue = 5
    ColorGreen = 6



# moves : [(CurrFace, Move, NewFace)]
moves = [ \
    (RbFace.FaceBottom, RbMove.MoveUp, RbFace.FaceFront),
    (RbFace.FaceBottom, RbMove.MoveDown, RbFace.FaceBack),
    (RbFace.FaceBottom, RbMove.MoveLeft, RbFace.FaceBottom),
    (RbFace.FaceBottom, RbMove.MoveRight, RbFace.FaceBottom),
    (RbFace.FaceBottom, RbMove.MoveClock, RbFace.FaceLeft),
    (RbFace.FaceBottom, RbMove.MoveClockAnti, RbFace.FaceRight),

    (RbFace.FaceUp, RbMove.MoveUp, RbFace.FaceBack),
    (RbFace.FaceUp, RbMove.MoveDown, RbFace.FaceFront),
    (RbFace.FaceUp, RbMove.MoveLeft, RbFace.FaceUp),
    (RbFace.FaceUp, RbMove.MoveRight, RbFace.FaceUp),
    (RbFace.FaceUp, RbMove.MoveClock, RbFace.FaceRight),
    (RbFace.FaceUp, RbMove.MoveClockAnti, RbFace.FaceLeft),

    (RbFace.FaceFront, RbMove.MoveUp, RbFace.FaceUp),
    (RbFace.FaceFront, RbMove.MoveDown, RbFace.FaceBottom),
    (RbFace.FaceFront, RbMove.MoveLeft, RbFace.FaceLeft),
    (RbFace.FaceFront, RbMove.MoveRight, RbFace.FaceRight),
    (RbFace.FaceFront, RbMove.MoveClock, RbFace.FaceFront),
    (RbFace.FaceFront, RbMove.MoveClockAnti, RbFace.FaceFront),
   
    (RbFace.FaceBack, RbMove.MoveUp, RbFace.FaceBottom),
    (RbFace.FaceBack, RbMove.MoveDown, RbFace.FaceFront),
    (RbFace.FaceBack, RbMove.MoveLeft, RbFace.FaceRight),
    (RbFace.FaceBack, RbMove.MoveRight, RbFace.FaceLeft),
    (RbFace.FaceBack, RbMove.MoveClock, RbFace.FaceBack),
    (RbFace.FaceBack, RbMove.MoveClockAnti, RbFace.FaceBack),

    (RbFace.FaceLeft, RbMove.MoveUp, RbFace.FaceLeft),
    (RbFace.FaceLeft, RbMove.MoveDown, RbFace.FaceLeft),
    (RbFace.FaceLeft, RbMove.MoveLeft, RbFace.FaceBack),
    (RbFace.FaceLeft, RbMove.MoveRight, RbFace.FaceFront),
    (RbFace.FaceLeft, RbMove.MoveClock, RbFace.FaceUp),
    (RbFace.FaceLeft, RbMove.MoveClockAnti, RbFace.FaceBottom),

    (RbFace.FaceRight, RbMove.MoveUp, RbFace.FaceRight),
    (RbFace.FaceRight, RbMove.MoveDown, RbFace.FaceRight),
    (RbFace.FaceRight, RbMove.MoveLeft, RbFace.FaceFront),
    (RbFace.FaceRight, RbMove.MoveRight, RbFace.FaceBack),
    (RbFace.FaceRight, RbMove.MoveClock, RbFace.FaceBottom),
    (RbFace.FaceRight, RbMove.MoveClockAnti, RbFace.FaceLeft)
]


    
# cube : [(row, col, slice, face, color)]
# cube : [(row, col, slice, Piece)]
