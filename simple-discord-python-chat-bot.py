# Created by 420

import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = ''

@client.event
async def on_ready():
    print("I'm ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "hi" in message.content.lower():
        await message.channel.send(f'Hi 420')
    elif 'hru?' in message.content.lower():
        await message.channel.send(f'Im fine u?')

client.run(TOKEN)