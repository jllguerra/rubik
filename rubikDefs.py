from enum import Enum

###############################################################################
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

###############################################################################
class RbMove(Enum):
    MoveUp = 1
    MoveDown = 2
    MoveRight = 3
    MoveLeft = 4
    MoveClock = 5
    MoveClockAnti = 6


###############################################################################
# Faces and Colors
class RbFace(Enum):
    FaceBottom = 1
    FaceTop = 2
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





    
# cube : [(row, col, slice, face, color)]
# cube : [(row, col, slice, Piece)]

###############################################################################
# Cada face es un par (RbFace, RbColor)
class RbPiece:
    ###############################################################################
    # moves : [(CurrFace, Move, NewFace)]
    LmovesFace = [ \
        (RbFace.FaceBottom, RbMove.MoveUp, RbFace.FaceFront),
        (RbFace.FaceBottom, RbMove.MoveDown, RbFace.FaceBack),
        (RbFace.FaceBottom, RbMove.MoveLeft, RbFace.FaceBottom),
        (RbFace.FaceBottom, RbMove.MoveRight, RbFace.FaceBottom),
        (RbFace.FaceBottom, RbMove.MoveClock, RbFace.FaceLeft),
        (RbFace.FaceBottom, RbMove.MoveClockAnti, RbFace.FaceRight),

        (RbFace.FaceTop, RbMove.MoveUp, RbFace.FaceBack),
        (RbFace.FaceTop, RbMove.MoveDown, RbFace.FaceFront),
        (RbFace.FaceTop, RbMove.MoveLeft, RbFace.FaceTop),
        (RbFace.FaceTop, RbMove.MoveRight, RbFace.FaceTop),
        (RbFace.FaceTop, RbMove.MoveClock, RbFace.FaceRight),
        (RbFace.FaceTop, RbMove.MoveClockAnti, RbFace.FaceLeft),

        (RbFace.FaceFront, RbMove.MoveUp, RbFace.FaceTop),
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
        (RbFace.FaceLeft, RbMove.MoveClock, RbFace.FaceTop),
        (RbFace.FaceLeft, RbMove.MoveClockAnti, RbFace.FaceBottom),

        (RbFace.FaceRight, RbMove.MoveUp, RbFace.FaceRight),
        (RbFace.FaceRight, RbMove.MoveDown, RbFace.FaceRight),
        (RbFace.FaceRight, RbMove.MoveLeft, RbFace.FaceFront),
        (RbFace.FaceRight, RbMove.MoveRight, RbFace.FaceBack),
        (RbFace.FaceRight, RbMove.MoveClock, RbFace.FaceBottom),
        (RbFace.FaceRight, RbMove.MoveClockAnti, RbFace.FaceLeft)
    ]


    DfaceMoves = { (face, move) : faceNxt for (face, move, faceNxt) in LmovesFace }

    LfaceMoves = []

    ###########################################################################
    def __init__(self, Lfaces):
        self.Lfaces = Lfaces

    ###########################################################################
    def rotatePieceFaces(self, move):
        LfacesAux = [(self.DfaceMoves[(face, move)], color) for (face, color) in self.Lfaces]
        self.Lfaces = LfacesAux


    ###########################################################################
    def getFaceColor(self, faceId):
        return [c for (f,c) in self.Lfaces if f == faceId]



###############################################################################

class RbCube():
    Lcoords = []
    Lp1coords = []
    Lp2coords = []
    Lp3coords = []

    Dpieces = {}

    ###########################################################################
    def __init__(self):        
        Lcoords = [(x,y,z) for x in RbCol \
                            for y in RbRow \
                            for z in RbSlice\
                            if not (x == RbCol(2) and y == RbRow(2) and z == RbSlice(2))]

        Lp1coords = [
        (RbCol(2), RbRow(2), RbSlice(1)), 
        (RbCol(2), RbRow(2), RbSlice(3)), 
        (RbCol(1), RbRow(2), RbSlice(2)), 
        (RbCol(3), RbRow(2), RbSlice(2)), 
        (RbCol(2), RbRow(1), RbSlice(2)), 
        (RbCol(2), RbRow(3), RbSlice(2)), 
        ]

        Lp3coords = [(x,y,z) for x in RbCol \
                             for y in RbRow \
                             for z in RbSlice\
                             if x != RbCol(2) and y != RbRow(2) and z != RbSlice(2)]

        Lp2coords = [(x,y,z) for (x,y,z) in Lcoords \
                            if not (x,y,z) in Lp1coords and not (x,y,z) in Lp3coords]


        self.Lcoords = Lcoords
        self.Lp1coords = Lp1coords
        self.Lp2coords = Lp2coords
        self.Lp3coords = Lp3coords

        self.Dpieces = { c : RbPiece([]) for c in Lcoords }

        # Inicializamos las caras asociadas a cada pieza
        for (x,y,z) in Lcoords:
            if z == RbSlice(1): self.Dpieces[(x,y,z)].Lfaces.append((RbFace.FaceFront, RbColor.ColorWhite))
            if z == RbSlice(3): self.Dpieces[(x,y,z)].Lfaces.append((RbFace.FaceBack, RbColor.ColorYellow))

            if y == RbRow(1): self.Dpieces[(x,y,z)].Lfaces.append((RbFace.FaceBottom, RbColor.ColorOrange))
            if y == RbRow(3): self.Dpieces[(x,y,z)].Lfaces.append((RbFace.FaceTop, RbColor.ColorRed))

            if x == RbCol(1): self.Dpieces[(x,y,z)].Lfaces.append((RbFace.FaceLeft, RbColor.ColorBlue))
            if x == RbCol(3): self.Dpieces[(x,y,z)].Lfaces.append((RbFace.FaceRight, RbColor.ColorGreen))


    ###########################################################################
    def rotateCol(self,c,r,s,move):
        nxtC = None
        if move == RbMove.MoveUp: nxtC = c
        if move == RbMove.MoveDown: nxtC = c

        if move == RbMove.MoveLeft: nxtC = RbCol(1)
        if move == RbMove.MoveRight: nxtC = RbCol(3)

        if move == RbMove.MoveClockAnti:
            if r == RbRow(1): nxtC = RbCol(3)
            if r == RbRow(2): nxtC = RbCol(2)
            if r == RbRow(3): nxtC = RbCol(1)
        if move == RbMove.MoveClock:
            if r == RbRow(1): nxtC = RbCol(1)
            if r == RbRow(2): nxtC = RbCol(2)
            if r == RbRow(3): nxtC = RbCol(3)
        
        return nxtC


    ###########################################################################
    def rotateRow(self,c,r,s,move):
        nxtR = None
        if move == RbMove.MoveUp: nxtR = RbRow(3)
        if move == RbMove.MoveDown: nxtR = RbRow(1)

        if move == RbMove.MoveLeft: nxtR = r
        if move == RbMove.MoveRight: nxtR = r

        if move == RbMove.MoveClockAnti:
            if c == RbCol(1): nxtR = RbRow(1)
            if c == RbCol(2): nxtR = RbRow(2)
            if c == RbCol(3): nxtR = RbRow(3)
        if move == RbMove.MoveClock:
            if c == RbCol(1): nxtR = RbRow(3)
            if c == RbCol(2): nxtR = RbRow(2)
            if c == RbCol(3): nxtR = RbRow(1)

        return nxtR

    ###########################################################################
    def rotateSlice(self,c,r,s,move):
        nxtS = None
        if move == RbMove.MoveUp: 
            if c == RbRow(1): nxtS = RbSlice(1)
            if c == RbRow(2): nxtS = RbSlice(2)
            if c == RbRow(3): nxtS = RbSlice(3)
        if move == RbMove.MoveDown: 
            if c == RbRow(1): nxtS = RbSlice(3)
            if c == RbRow(2): nxtS = RbSlice(2)
            if c == RbRow(3): nxtS = RbSlice(1)

        if move == RbMove.MoveLeft: 
            if c == RbCol(1): nxtS = RbSlice(3)
            if c == RbCol(2): nxtS = RbSlice(2)
            if c == RbCol(3): nxtS = RbSlice(1)
        if move == RbMove.MoveRight: 
            if c == RbCol(1): nxtS = RbSlice(1)
            if c == RbCol(2): nxtS = RbSlice(2)
            if c == RbCol(3): nxtS = RbSlice(3)

        if move == RbMove.MoveClockAnti: nxtS = s
        if move == RbMove.MoveClock: nxtS = s

        return nxtS

    ###########################################################################
    def rotatePieceCoord(self, c,r,s,move):
        return (self.rotateCol(c,r,s,move), \
                self.rotateRow(c,r,s,move), \
                self.rotateSlice(c,r,s,move))


    ###########################################################################
    def rotateCubeCol(self, c, move):
        assert(c in RbCol) 
        assert(move in [RbMove.MoveUp, RbMove.MoveDown])
        LpiecesAux =  [((c,r,s), self.Dpieces[(c,r,s)]) for r in RbRow for s in RbSlice]
        for ((c,r,s), piece) in LpiecesAux:
            coordNxt = self.rotatePieceCoord(c,r,s,move)
            piece.rotatePieceFaces(move)
            self.Dpieces[coordNxt] = piece

    ###########################################################################
    def rotateCubeRow(self, r, move):
        assert(r in RbRow) 
        assert(move in [RbMove.MoveLeft, RbMove.MoveRight])
        LpiecesAux =  [((c,r,s), self.Dpieces[(c,r,s)]) for c in RbCol for s in RbSlice]
        for (coordAct, piece) in LpiecesAux:
            coordNxt = self.rotatePieceCoord(c,r,s,move)
            piece.rotatePieceFaces(move)
            self.Dpieces[coordNxt] = piece


    ###########################################################################
    def rotateCubeSlice(self, s, move):
        assert(s in RbSlice) 
        assert(move in [RbMove.MoveClock, RbMove.MoveClockAnti])
        LpiecesAux =  [((c,r,s), self.Dpieces[(c,r,s)]) for c in RbCol for r in RbRow]
        for (coordAct, piece) in LpiecesAux:
            coordNxt = self.rotatePieceCoord(c,r,s,move)
            piece.rotatePieceFaces(move)
            self.Dpieces[coordNxt] = piece


    ###########################################################################
    def getFaceColors(self, faceId):
        assert(faceId in RbFace)
        return [ (c,r,s,self.Dpieces[(c,r,s)].getFaceColor(faceId)) 
          for (c,r,s) in self.Lcoords]
        