#Left off here(watch it):
#https://www.youtube.com/watch?v=THj99FuPJmI

import discord
from discord.ext import commands
import random #for 8ball

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

@vinny.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(vinny.latency * 1000)}ms")

@vinny.command(aliases=['8ball', 'eightball', 'ateball'])
async def _8ball(ctx, *, question): #The Asterisks allows for multiple arguements and use it as one
    responses = ['No', 'Maybe', 'Go Away',' Why Are You Here', 'Alot', 'Of course', "I'd be surprised if not", "Absolutely"]
    await ctx.send(f"{random.choice(responses)}")

@vinny.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)#+1 was used in order to account for the message which executes the command, otherwise all message deletions are underdeleted by 1

@vinny.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@vinny.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@vinny.command()
async def unban(ctx, *, member : discord.member, )

vinny.run('ODM3OTY5MTM4OTE5OTMxOTI0.YI0Rkw.3UoV-KuzrCqurcEFPUtzzCaYpHU')
