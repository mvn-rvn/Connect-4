#initialize the 2d array
grid = []
while len(grid) != 6:
    grid.append(["#", "#", "#", "#", "#", "#", "#"])

for row in grid:
    for elem in row:
        print(elem, end="")
    print(" ")
