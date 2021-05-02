import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("I'm up and running!")

@client.event
async def on_member_join(member):
  print(f"{member} has joined Sonder!")

@client.event
async def on_member_remove(member):
  print(f"{member} has left Sonder :(")

client.run('ODM3OTY5MTM4OTE5OTMxOTI0.YI0Rkw.3UoV-KuzrCqurcEFPUtzzCaYpHU')
