global data
data = None

#REMINDER: grid[y][x]. y coordinate goes from top to bottom
def printgrid():
    output = "```"
    output += "\n0 1 2 3 4 5 6\n"
    for row in grid:
        for elem in row:
            output += elem + " "
        output += "\n"
    output += "```"
    return output

#check for wins (disgusting code)
def checkforwin():
    #vertical wins
    for y in range(len(grid) - 3):
        for x in range(len(grid[0])):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y+1][x] == piece and grid[y+2][x] == piece and grid[y+3][x] == piece:
                    return True
        #horizontal wins
    for y in range(len(grid)):
        for x in range(len(grid[0]) - 3):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y][x+1] == piece and grid[y][x+2] == piece and grid[y][x+3] == piece:
                    return True
    #diagonal down wins
    for y in range(len(grid) - 3):
        for x in range(len(grid[0]) - 3):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y+1][x+1] == piece and grid[y+2][x+2] == piece and grid[y+3][x+3] == piece:
                    return True
    #diagonal up wins
    for y in range(len(grid) - 4, len(grid)):
        for x in range(len(grid[0]) - 3):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y-1][x+1] == piece and grid[y-2][x+2] == piece and grid[y-3][x+3] == piece:
                    return True

#await wait_for check
def check(m):
    return m.content.isdigit()

#main loop
async def gameloop():
    #initialize 2d list and turn order
    global grid
    global data
    grid = []
    while len(grid) != 7:
        grid.append(["-", "-", "-", "-", "-", "-", "-"])
    turn = "X"
    while True:
        #get input
        await discord_channel.send(printgrid())
        await discord_channel.send(turn + "'s turn. ")
        await bot.wait_for("message", check=check)
        action = data
        if action > 6:
            discord_channel.send("bruh that's not a space you can drop tokens in")
            break
        #place piece
        bottom = False
        row = 0
        while bottom == False:
            if grid[0][action] == "-" and (row + 1 == len(grid) or grid[row + 1][action] != "-"):
                grid[row][action] = turn
                bottom = True
            elif grid[0][action] != "-":
                await discord_channel.send("bruh the column's full")
                bottom = True
            row += 1
        #check for winners
        if checkforwin() == True:
            await discord_channel.send(printgrid())
            await discord_channel.send("WINNER: " + turn)
            break
        #advance turn order
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        data = None

#-----------------------------------------------------------------

from nextcord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="c4!")
global discord_channel

@bot.event
async def on_ready():
    print("Connected.")

@bot.command()
async def normal(ctx):
    global discord_channel
    discord_channel = ctx.channel
    await gameloop()

@bot.event
async def on_message(msg):
    print("I got a message!")
    if msg.content.isdigit():
        global data
        print(int(msg.content))
        data = int(msg.content)
    await bot.process_commands(msg)

bot.run(open("token.txt", "r").read())