# initialize the 2d array
grid = []
while len(grid) != 6:
    grid.append(["-", "-", "-", "-", "-", "-", "-"])

# initialize turn order
turn = "X"
who_won = None

# REMINDER: grid[y][x]. y coordinate goes from top to bottom
def printgrid(who_won):
    print("\n1 2 3 4 5 6 7")
    for row in grid:
        for elem in row:
            print(elem + " ", end="")
        print(" ")
    if who_won != None:
        print(turn + "'s turn")

while who_won == None:
    pass