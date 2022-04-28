from datetime import datetime
import discord
import asyncio
from discord.ext import commands, tasks

from aioconsole.stream import ainput

from termcolor import cprint

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

curr_channel = 969266297504428092

@tasks.loop(seconds=2)
async def thr():
    t = await ainput()

    t2 = t.split(" ");

    await client.get_channel(curr_channel).send(t)

@client.event
async def on_ready():

    print("Welcome to IRC-inspired discord bot controlling!")
    cprint("Warning: This may be against TOS but I have no clue. Open an issue if you think it is and i will review. (Me, Kai Gonzalez)", 'yellow')

    if not thr.is_running():
        thr.start() 

@client.event
async def on_message(msg: discord.Message):
    if (msg.channel.id == curr_channel and msg.author.display_name != client.user.display_name):
        
        cprint("[" + msg.author.display_name.lower() + " (" + str(datetime.now().month) + "/" + str(datetime.now().day) + "/" +
         str(datetime.now().year) + ")]: " + msg.content, 'green')

client.run("YOUR_TOKEN")