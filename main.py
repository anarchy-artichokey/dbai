import discord
from discord import app_commands
from matplotlib import axes
import json

def readConfig():
    with open("./config.json") as configFile:
        return json.load(configFile)

myGuild = discord.Object(readConfig()["guild"]["id"])

class myClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents = intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild = myGuild)
        await self.tree.sync(guild = myGuild)

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True
client = myClient(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.tree.command()
async def line_plot(interaction: discord.Interaction, function: str):

    graph = ""

    await interaction.response.send_message(graph)

@client.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")

client.run(readConfig()["discord"]["api_key"])
