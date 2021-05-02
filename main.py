#Bot can be invited to a server https://discord.com/developers/applications/837969138919931924/oauth2 at this link. Check "Bot" in the "Scopes" selections, choose the bot permissions and then copy the link from the "Scopes" box that appears
#Help: https://dev.to/mikeywastaken/events-in-discord-py-mk0

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

#Custom Commands
@vinny.command(name="hello", description="Greet the user!")
async def hello(ctx):
  await ctx.send(f"Hiya {ctx.author.name}, I'm Vinny, now get moving bub.") #f-string to make Vinny say hello

#Auto Responder
@vinny.event
async def on_message(message):
  if "Vinny" in message.content:
        await message.channel.send("What")


#------------------Beginning of Auto Moderation Section(Kinda currently only deletes the sent message and pings the user in the sent channel)------------------

#Blocks the user from sending links(https)
@vinny.event
async def on_message_1(message):
  if "https://" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Try that shit again and I'll break your windpipe.")
  else:
        await vinny.process_commands(message)

#Blocks the user from sending links(http)
@vinny.event
async def on_message_2(message):
  if "http://" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Try that shit again and I'll break your windpipe.")
  else:
        await vinny.process_commands(message)

#Shit Broke
#wordBanList= ['poop', 'peepee', 'stupid']
#@vinny.event
#async def on_message(message):
#  for i in wordBanList: #loops through the word ban list
#    if i in message:
#        await message.delete()
#        await message.channel.send(f"{message.author.mention} say that again and I'll feed your balls to my greyhounds")
#        return #stops bot from going sickomode and trying to delete the message again
#  await vinny.process_commands(message)

vinny.run('ODM3OTY5MTM4OTE5OTMxOTI0.YI0Rkw.3UoV-KuzrCqurcEFPUtzzCaYpHU')
