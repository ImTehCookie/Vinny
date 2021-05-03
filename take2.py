#Left off here(watch it):
#https://www.youtube.com/watch?v=THj99FuPJmI

import discord
from discord.ext import commands
import random #for 8ball

intents = discord.Intents(messages = True, guilds = True, reactions = True, members= True, presences = True)

vinny = commands.Bot(command_prefix = '.', intents = intents, case_insensitive= True)

#Shows when bot runs successfully
@vinny.event
async def on_ready():
  print("I'm up and running!")

#Sends message in consol when a member joins
@vinny.event
async def on_member_join(member):
  print(f"{member} has joined Sonder!")

#Sends message in consol when a member leaves
@vinny.event
async def on_member_remove(member):
  print(f"{member} has left Sonder :(")

#Command for latency
@vinny.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(vinny.latency * 1000)}ms")

#8ball command
@vinny.command(aliases=['8ball', 'eightball', 'ateball'])
async def _8ball(ctx, *, question): #The Asterisks allows for multiple arguements and use it as one
    responses = ['No', 'Maybe', 'Go Away',' Why Are You Here', 'Alot', 'Of course', "I'd be surprised if not", "Absolutely"]
    await ctx.send(f"{random.choice(responses)}")

#Purge Command
@vinny.command()
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)#+1 was used in order to account for the message which executes the command, otherwise all message deletions are underdeleted by 1

#Kick Command
@vinny.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

#Ban command
@vinny.command()
async def ban (ctx, member:discord.User=None, *, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "No Reason Given."
    message = f"You have been baned from {ctx.guild.name} for: {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} was banned for {reason}")

#Unban command
@vinny.command()
async def unban (ctx, member:discord.User=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot unban yourself")
        return
    
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:    
        user = ban_entry.user
        if member == user:
            await ctx.guild.unban(user)
            embed = discord.Embed(title="User Unbanned", description = f":white_check_mark: **{user.mention}** has been **Unbanned**", colour = 0x00ff00)
            return await ctx.send(embed=embed)


#Bot Token
vinny.run('ODM3OTY5MTM4OTE5OTMxOTI0.YI0Rkw.3UoV-KuzrCqurcEFPUtzzCaYpHU')
