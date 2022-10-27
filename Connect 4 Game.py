w, h = 7, 6
Matrix = [["." for x in range(w)] for y in range(h)]
xTurn = True
columns_Status = [0] * 7
gameOver = False


def print_matrix():
    for i in reversed(range(h)):
        str1 = ""
        for j in range(w):
            str1 += Matrix[i][j]
        print(str1)

def isGridFull():
    for col in columns_Status:
        if col!=6:
            return False
    return True

def isWinner(p):
    # Check for a horizontal win
    for i in range(h):
        for j in range(w-3):
            if Matrix[i][j]==p and Matrix[i][j+1]==p and Matrix[i][j+2]==p and Matrix[i][j+3]==p:
                return True
    # Check for a vertical win
    for i in range(h-3):
        for j in range(w):
            if Matrix[i][j]==p and Matrix[i+1][j]==p and Matrix[i+2][j]==p and Matrix[i+3][j]==p:
                return True
    # Check for a diagonal win positive slope
    for i in range(h-3):
        for j in range(w-3):
            if Matrix[i][j]==p and Matrix[i+1][j+1]==p and Matrix[i+2][j+2]==p and Matrix[i+3][j+3]==p:
                return True
    # Check for a diagonal win positive slope
    for i in range(h - 3):
        for j in range(w):
            if j>=3 and Matrix[i][j]==p and Matrix[i+1][j-1]==p and Matrix[i+2][j-2]==p and Matrix[i+3][j-3]==p:
                return True
    return False

def isGameOver():
    if isGridFull():
        print("Grid is Full. Game Over")
        return True
    if gameOver:
        print("Game is Over")
        return True
    return False

while not isGameOver():
    if xTurn:
        posX = int(input("Player 1: Choose where to put your X"))
        # While loop that swallows user till they enter a valid number
        while True:
            if posX > 7 or posX < 1:
                posX = int(input("Enter a number between 1 and 7"))
            elif columns_Status[posX - 1] == 6:
                posX = int(input("This column is full. Choose another one"))
            else:
                break
        Matrix[columns_Status[posX - 1]][posX - 1] = "X"
        columns_Status[posX - 1] += 1
        if isWinner("X"):
            gameOver = True
            print("Player 1 won. Congratulations. Game Over")
        print_matrix()
        xTurn = False
    else:
        posO = int(input("Player 2: Choose where to put your O"))
        # While loop that swallows user till they enter a valid number
        while True:
            if posO > 7 or posO < 1:
                posO = int(input("Enter a number between 1 and 7"))
            elif columns_Status[posO - 1] == 6:
                posO = int(input("This column is full. Choose another one"))
            else:
                break
        Matrix[columns_Status[posO - 1]][posO - 1] = "O"
        columns_Status[posO - 1] += 1
        if isWinner("O"):
            gameOver = True
            print("Player 2 won. Congratulations. Game Over")
        print_matrix()
        xTurn = True