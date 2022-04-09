from rubikDefs import RbCube, RbCol, RbRow, RbSlice, RbFace, RbPiece, RbMove, RbColor

#print(rbd.moves)

C = RbCube()
# print('\n\np1Coords:')
# for c in C.Lp1coords: print(C.Dpieces[c].Lfaces)
# print('\n\np2Coords:')
# for c in C.Lp2coords: print(C.Dpieces[c].Lfaces)
# print('\n\np3Coords:')
# for c in C.Lp3coords: print(C.Dpieces[c].Lfaces)


# C.Dpieces[(RbCol(1),RbRow(1),RbSlice(1))]
# C.Dpieces[(RbCol(1),RbRow(1),RbSlice(1))].getFaceColor(RbFace.FaceFront)
#C.rotateCubeCol(RbCol(1), RbMove.MoveUp)

L1 = C.getFaceColors(RbFace.FaceFront)
print(f'{L1}\n' * 2)
L2 = C.getFaceColors(RbFace.FaceTop)
print(f'{L2}\n' * 2)
L3 = C.getFaceColors(RbFace.FaceLeft)
print(f'{L3}\n' * 2)
