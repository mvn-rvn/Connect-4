from nextcord.ext import commands
import connect

bot = commands.Bot(command_prefix="c4!")

@bot.event
async def on_ready():
    print("Connected.")

async def send_msg(channel_id, ):
    channel = await bot.fetch_channel(channel_id)
    await channel.send()

@bot.command()
async def connect(ctx):

bot.run(input("Token: "))