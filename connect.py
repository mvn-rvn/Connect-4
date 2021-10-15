import time

# initialize the 2d array
grid = []
while len(grid) != 6:
    grid.append(["-", "-", "-", "-", "-", "-", "-"])

# initialize turn order
turn = "X"
who_won = None

# REMINDER: grid[y][x]. y coordinate goes from top to bottom
def printgrid():
    print("\n0 1 2 3 4 5 6")
    for row in grid:
        for elem in row:
            print(elem + " ", end="")
        print(" ")
    print("----------------------------------------------")

def checkforwin():
    for row in grid:
        for elem in row:
            pass

#main loop
while who_won == None:
    #get input
    printgrid()
    action = int(input(turn + "'s turn. "))
    #place piece
    bottom = False
    row = 0
    while bottom == False:
        if grid[0][action] == "-" and (row + 1 == len(grid) or grid[row + 1][action] != "-"):
            grid[row][action] = turn
            bottom = True
        elif grid[0][action] != "-":
            print("Bruh that column's full")
            time.sleep(1)
            bottom = True
        row += 1
    #advance turn order
    if turn == "X":
        turn = "O"
    else:
        turn = "X"