# initialize the 2d array
grid = []
while len(grid) != 6:
    grid.append(["-", "-", "-", "-", "-", "-", "-"])

# initialize turn order
turn = "X"

# REMINDER: grid[y][x]. y coordinate goes from top to bottom
def printgrid():
    print("\n1 2 3 4 5 6 7")
    for row in grid:
        for elem in row:
            print(elem + " ", end="")
        print(" ")
    print(turn + "'s turn")

