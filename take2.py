import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members= True, presences = True)

vinny = commands.Bot(command_prefix = '.', intents = intents, case_insensitive= True)

@vinny.event
async def on_ready():
  print("I'm up and running!")

@vinny.event
async def on_member_join(member):
  print(f"{member} has joined Sonder!")

@vinny.event
async def on_member_remove(member):
  print(f"{member} has left Sonder :(")

vinny.run('ODM3OTY5MTM4OTE5OTMxOTI0.YI0Rkw.3UoV-KuzrCqurcEFPUtzzCaYpHU')