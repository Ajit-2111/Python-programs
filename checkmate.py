def Check():
    a = input("Please enter the x coordinate of your piece :")
    b = input("Please enter the y coordinate of your piece :")
    x = input("Please enter the x coordinate of opponent King : ")
    y = input("Please enter the y coordinate of opponent King : ")
    myPiece = input("Please enter the number for your Piece : \n 1 . QUEEN \n 2 . BISHOP \n 3 . ROOK\n")
    if myPiece == 1:
        if (horizontalVerticalCheck(a,b,x,y) or diagonalCheck(a,b,x,y)):
            return  "Check !!! Your King is in Danger!!!"
        return "Your King is SAFE !!!"
    if myPiece == 2:
        if (diagonalCheck(a,b,x,y)):
            return  "Check !!! Your King is in Danger!!!"
        return "Your King is SAFE !!!"
    if myPiece == 3:
        if (horizontalVerticalCheck(a,b,x,y)):
            return  "Check !!! Your King is in Danger!!!"
        return "Your King is SAFE !!!"

def horizontalVerticalCheck(a,b,x,y): # (a,b) position of opponent king (x,y) position of your piece
    if (a==x or b==y):
        return True

def diagonalCheck(a,b,x,y):# (a,b) position of opponent king (x,y) position of your piece
        positionAdd = x + y
        positionSub = x - y
        if (positionAdd == a+b or positionSub == a-b):
           return True

print(Check())
