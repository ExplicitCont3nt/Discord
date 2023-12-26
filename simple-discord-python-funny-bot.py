# Created by 420

import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = commands.Bot(command_prefix='%', intents=intents)

TOKEN = ''

@client.event
async def on_ready():
    print(f"I'm ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command(name='compliments')
async def compliments(ctx):
    compliments = ["420 is really cool", "420 is the best", "420 my dad", "420 on top", "420 my dev"]
    compliment_selected = random.choice(compliments)
    await ctx.send(compliment_selected)
try:
    client.run(TOKEN)
except discord.errors.LoginFailure:
    print("ERROR: Invalid bot token.")
except Exception as e:
    print(f"ERROR: {e}")