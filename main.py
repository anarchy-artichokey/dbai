import discord
import matplotlib



client = discord.Client()

myGuild = discord.Object(readConfig("guildID"))

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



client.run('your token here')
