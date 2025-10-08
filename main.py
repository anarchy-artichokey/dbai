import discord
import matplotlib
import json

def readConfig():
    with open("./config.json") as configFile:
        return json.load(configFile)

client = discord.Client(readConfig())

myGuild = discord.Object()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



client.run('your token here')
