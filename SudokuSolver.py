# Program that solves a 9x9 sudoku board

# initialize empty (0) 2-D array
board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1]] 

# Pre-made board for ease of use
preMadeBoard = [[4,-1,9,-1,-1,-1,1,-1,-1],[7,-1,6,4,8,1,-1,3,9],[8,-1,2,-1,3,6,4,7,5],[1,7,-1,-1,9,3,-1,-1,-1],[3,-1,-1,-1,-1,-1,5,-1,-1],[-1,6,-1,2,4,-1,-1,-1,7],
    [6,-1,-1,-1,-1,-1,-1,2,3],[-1,4,-1,-1,-1,2,-1,-1,-1],[-1,-1,-1,3,1,-1,6,5,-1]]

solve = False

# Sets up the initial board
def start_game():

    # Program will first receive inputs of the initial board 

    answer = input("Would you like to use the pre-made board? (Y/N)")

    if (answer == "Y"):
        for i in range(9):
            for j in range(9):
                board[i][j] = preMadeBoard[i][j]
    else:
        print()
        print("Insert the board (squares 1 to 81)")
        for i in range(0,9):
            for j in range (0,9):
                print(f"Row {i + 1}, Column {j + 1}: ")
                number = int(input("What's the number?"))
                if (number != 0):
                    board[i][j] = number

    print()
    print("Initial board: ")
    print_board()

    # Call main method
    sudoku_solver()

# main method which solves the sudoku board
def sudoku_solver(): 

    solved = False

    # Get the first location that needs to be filled in
    row, column = next_location()
    
    # If the whole puzzle is filled in then we can stop the program since it's finished
    if row is None or column is None:
        return True

    # Will loop over the numbers 1...9 to find the right fit
    for k in range(1,10):
        if check_valid_placement(k,row,column):
            board[row][column] = k
            if sudoku_solver():
                print()
                print("Solved board: ")
                print_board()
                return True
        board[row][column] = -1

    return False

# Finds the next location to fill in
def next_location():
    for i in range(9):
        for j in range(9):
            if board[i][j] == -1:
                return i,j

    # if no locations are still empty
    return None, None
                
# checks if a move is valid or not based on the official sudoku rules
def check_valid_placement(num, row, column):

    # Check the rows 
    for i in range(0,9):
        if num == board[row][i]:
            return False

    # Check the columns
    for i in range(0,9):
        if num == board[i][column]:
            return False
    
    # Check the squares
    # Verify which square the location is in
    if (0 <= row <= 2 and 0 <= column <= 2):
        #print("sq1")
        for i in range(0,3):
            for j in range(0,3):
                if num == board[i][j]:
                    return False

    elif (0 <= row <= 2 and 3 <= column <= 5):
        #print("sq2")
        for i in range(0,3):
            for j in range(3,6):
                if num == board[i][j]:
                    return False

    elif (0 <= row <= 2 and 6 <= column <= 8):
        #print("sq3")
        for i in range(3,5):
            for j in range(6,9):
                if num == board[i][j]:
                    return False

    elif (3 <= row <= 5 and 0 <= column <= 2):
        #print("sq4")
        for i in range(3,6):
            for j in range(0,3):
                if num == board[i][j]:
                    return False
                    
    elif (3 <= row <= 5 and 3 <= column <= 5):
        #print("sq5")
        for i in range(3,6):
            for j in range(3,6):
                if num == board[i][j]:
                    return False

    elif (3 <= row <= 5 and 6 <= column <= 8):
        #print("sq6")
        for i in range(3,6):
            for j in range(6,9):
                if num == board[i][j]:
                    return False

    elif (6 <= row <= 8 and 0 <= column <= 2):
        #print("sq7")
        for i in range(6,9):
            for j in range(0,3):
                if num == board[i][j]:
                    return False

    elif (6 <= row <= 8 and 3 <= column <= 5):
        #print("sq8")
        for i in range(6,9):
            for j in range(3,6):
                if num == board[i][j]:
                    return False

    elif (6 <= row <= 8 and 6 <= column <= 8):
        #print("sq9")
        for i in range(6,9):
            for j in range(6,9):
                if num == board[i][j]:
                    return False

    return True


# prints the sudoku board
def print_board():
    for i in range(0,9):
        if (i % 3 == 0 and i != 0):
                print("---------------------")
        for j in range(0,9):
            if (j % 3 == 0 and j != 0):
                print("|",end= " ")
                
            print(board[i][j], end= " ")
        print()

start_game()
