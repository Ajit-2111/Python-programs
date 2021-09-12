def Check():
    x = int(input("Please enter the x coordinate of your King : "))
    y = int(input("Please enter the y coordinate of your King : "))
    myPiece = int(input("\n 1 . QUEEN \n 2 . BISHOP \n 3 . KNIGHT\n 4 . ROOK\nPlease enter the number for opponents Piece : "))
    a = int(input("Please enter the x coordinate of opponents piece : "))
    b = int(input("Please enter the y coordinate of opponents piece : "))
    if myPiece == 1:
        return "Check !!! Your King is in Danger!!!" if (horizontalVerticalCheck(a,b,x,y) == True or diagonalCheck(a,b,x,y) == True) else "Your King is SAFE !!!"
    if myPiece == 2:
        return "Check !!! Your King is in Danger!!!" if (diagonalCheck(a,b,x,y) == True) else "Your King is SAFE !!!"
    if myPiece == 3:
        return "Check !!! Your King is in Danger!!!" if (knightcheck(a,b,x,y)) else "Your King is SAFE !!!"
    if myPiece == 4:
        return "Check !!! Your King is in Danger!!!" if (horizontalVerticalCheck(a, b, x, y) == True) else "Your King is SAFE !!!"

def horizontalVerticalCheck(a,b,x,y):
        return True if (a == x or b == y) else False

def diagonalCheck(a,b,x,y):
        positionAdd = x + y
        positionSub = x - y
        return True if (positionAdd == a+b or positionSub == a-b) else False

def knightcheck(a,b,x,y):
    return True if (x == a + 2) and (y == b + 1) else True if (x == a + 1) and (y == b + 2) else True if (x == a-1) and (y == b+2) else True if (x == a-2) and (y == b+1) else True if (x == a+2) and (y == b-1) else True if (x == a+1) and (y == b-2) else True if (x == a-1) and (y == b-2) else True if (x == a-2) and (y == b-1) else False

print(Check())