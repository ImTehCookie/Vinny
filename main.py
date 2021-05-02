#Bot can be invited to a server https://discord.com/developers/applications/837969138919931924/oauth2 at this link. Check "Bot" in the "Scopes" selections, choose the bot permissions and then copy the link from the "Scopes" box that appears

import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members= True, presences = True)

client = commands.Bot(command_prefix = '.', intents = intents, case_insensitive= True)

@client.event
async def on_ready():
  print("I'm up and running!")

@client.event
async def on_member_join(member):
  print(f"{member} has joined Sonder!")

@client.event
async def on_member_remove(member):
  print(f"{member} has left Sonder :(")

@client.command(name="hello", description="Greet the user!")
async def hello(ctx):
  await ctx.send(f"Hiya {ctx.author.name}, I'm Vinny, now get moving bub.") #f-string to make Vinny say hello

client.run('ODM3OTY5MTM4OTE5OTMxOTI0.YI0Rkw.3UoV-KuzrCqurcEFPUtzzCaYpHU')
