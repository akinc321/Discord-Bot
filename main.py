import discord
import os
from random import random
import math

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("$hello"):
        name = str(message.author)[:-5]
        if name.lower() == 'dossekpli':
            await message.channel.send("Hello, loser!")
        else:
            await message.channel.send("Hello, "+name+"!")

    if message.content.lower().startswith("$rolldice"):
        roll = int(random()*6)+1
        await message.channel.send("You rolled a " + str(roll) + "!")

    if message.content.lower().replace(" ","") == message.content.lower().replace(" ","")[::-1]:
        await message.channel.send("That is a palindrome!")
    if "dawici" in message.content.lower() or "dossekpli" in message.content.lower():
        await message.channel.send("Did you mean to say: \""+message.content.replace("dawici", "Supreme Overlord dawici").replace("Dossekpli", "Supreme Overlord Dossekpli")+"\"?")

client.run(os.getenv('TOKEN'))