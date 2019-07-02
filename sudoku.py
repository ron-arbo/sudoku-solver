board = [[0, 0, 0, 2, 6, 0, 7, 0, 1,],
         [6, 8, 0, 0, 7, 0, 0, 9, 0,], 
         [1, 9, 0, 0, 0, 4, 5, 0, 0,], 
         [8, 2, 0, 1, 0, 0, 0, 4, 0,], 
         [0, 0, 4, 6, 0, 2, 9, 0, 0,], 
         [0, 5, 0, 0, 0, 3, 0, 2, 8,], 
         [0, 0, 9, 3, 0, 0, 0, 7, 4,], 
         [0, 4, 0, 0, 5, 0, 0, 3, 6,], 
         [7, 0, 3, 0, 1, 8, 0, 0, 0,]
]


#Prints the board
def print_board(board):
    for i in range(0, 9):
        for j in range(0, 9):
            #If on third or sixth column, draw border
            if(j == 2 or j == 5):

                print(str(board[i][j]) + " |", end = ' ')
            else:
                print(board[i][j], end = ' ')
        #If on third on sixth row, draw border
        if(i == 2 or i == 5):
            print("")
            print("----------------------")
        else:
            print("")

#Returns an ordered pair of the next empty space on the board, or (-1, -1) otherwise
def find_next_empty(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if(board[i][j] == 0):
                return (i, j)
    return (-1, -1)

#Determines if a certain number in its spot is valid according to sudoku rules
def isValid(board, pair, num):
    rowNum = pair[0]
    colNum = pair[1]
   
    #Check if in row
    row = board[rowNum]
    if num in row:
        return False
    
    #Check if in column
    for i in range(0, 9):
        if(num == board[i][colNum]):
            return False
    
    #Check if in box
    #Find rowNums of other rows in box
    if(rowNum % 3 == 0):
        otherRows = (rowNum+1, rowNum+2)
    if(rowNum % 3 == 1):
        otherRows = (rowNum-1, rowNum+1)
    if(rowNum % 3 == 2):
        otherRows = (rowNum-1, rowNum-2)
    
    #Find colNums of other cols in box
    if(colNum % 3 == 0):
        otherCols = (colNum+1, colNum+2)
    if(colNum % 3 == 1):
        otherCols = (colNum-1, colNum+1)
    if(colNum % 3 == 2):
        otherCols = (colNum-1, colNum-2)

    otherRow1 = otherRows[0]
    otherRow2 = otherRows[1]
    otherCol1 = otherCols[0]
    otherCol2 = otherCols[1]

    otherSpots = (board[otherRow1][otherCol1], board[otherRow1][otherCol2], board[otherRow2][otherCol1], board[otherRow2][otherCol2])
    if num in otherSpots:
        return False
    
    return True

def complete(board):
    next = find_next_empty(board)
    if(next == (-1, -1)):
        return True
    else:
        #Row and Col of position subject to change
        row = next[0]
        col = next[1]
    
    for i in range(1, 10):
        if isValid(board, (row, col), i):
            board[row][col] = i
            if complete(board):
                return True
            board[row][col] = 0
    
    return False


print_board(board)
print("")
print("")
complete(board)
print_board(board)
