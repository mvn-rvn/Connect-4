import os
global data
global is_playing
is_playing = False
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
    await bot.change_presence(status=nextcord.Status.dnd, activity=nextcord.Game(name="c4 commands"))
    #initialize 2d list and turn order
    global grid
    global data
    grid = []
    while len(grid) != 6:
        grid.append(["-", "-", "-", "-", "-", "-", "-"])
    turn = "X"
    while True:
        #get input
        await discord_channel.send(printgrid())
        await discord_channel.send(turn + "'s turn. ")
        #await bot.wait_for("message", check=check)
        while data == None:
            await asyncio.sleep(0.5)
            pass
        if data == "forfeit":
            await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game(name="c4 commands"))
            data = None
            break
        action = data
        bottom = False
        if action > 6:
            await discord_channel.send("bruh that's not a space you can drop tokens in")
            bottom = True
        #place piece
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
            global is_playing
            is_playing = False
            data = None
            await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game(name="c4 commands"))
            break
        #advance turn order
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        data = None

#-----------------------------------------------------------------

import nextcord
from nextcord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="c4 ")
global discord_channel

@bot.event
async def on_ready():
    print("Connected.")
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game(name="c4 commands"))

@bot.command()
async def play(ctx):
    global is_playing
    if is_playing == False:
        is_playing = True
        global discord_channel
        discord_channel = ctx.channel
        await gameloop()
    else:
        await ctx.channel.send("There's an existing game going on, finish that one first")

@bot.command()
async def forfeit(ctx):
    global is_playing
    if is_playing == True:
        global data
        await ctx.channel.send("Gotcha.")
        is_playing = False
        data = "forfeit"
    else:
        await ctx.channel.send("There isn't a game going on.")

@bot.command()
async def commands(ctx):
    await ctx.channel.send("**\"c4 play\"**\nSets up a game of Connect 4.\n\n**\"c4 forfeit\"**\nPrematurely ends an ongoing game of Connect 4.\n\n**How to play**\nType in the number corresponding to a column on your turn.\n\n*Note: This bot does not keep track of who is playing in the game, meaning anyone can type in a number and the bot will continue the game regardless. Do not abuse this oversight.*")


@bot.event
async def on_message(msg):
    print("I got a message!")
    if msg.content.isdigit():
        global data
        print(int(msg.content))
        data = int(msg.content)
    await bot.process_commands(msg)

bot.run(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "token.txt"), "r").read())