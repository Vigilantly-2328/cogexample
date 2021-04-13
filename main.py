"""
Copyright Akins M. 2021
M.I.T License

Fair use policy: Any and all modification and copying of this program is allowed. You may not however take this exact code and claim it as your own, nor may you slightly modify^1 it and claim it as your own. 
1 - Slight Modification : Slight modification is defined under this code as at least 2 or more *functioning* commands, and one *functioning * cog. So, for example you may *not*, simply add your token in and claim the bot as your own. You may *not* simply add a command that says hello and claim the code as your own, and you may *not* simply change some variable names and claim the code as your own.
Security policy: If you find any vulnerabilities or issues, please feel free to email me at akins2229@gmail.com, or DM me on discord at Akins#2229

Notes: You may have noticed a few things. 1. I plastered my name everywhere in the code. Yes, I did, and for good reason. I don't want people to just take this code and run with it. I want people to use it as an example in developing their own bots, not to have it *be* their bot. I am well aware that it doesn't completely fix the issue, but it should serve to discourage it. This is an issue for a multitude of reasons, the main one being that you do not benifit yourself, or others by copying my code, or simply having it spoonfed to you. You will not learn from it. 
Notes (continued): 2. I have only added very few commands. I have done this intentionally, I simply added the commands that I did so that I can show that cogs in and of themselves have no real limit to their command capabilities that the discord.ext.commands library doesn't have in general, limitations that are quite rare in general, and also I'm just lazy.
Notes (continued again): 3. I only used 2 libraries. This however does not mean that you can only use that library. Cogs fucntion as any other class would in python. You can use any libraries youd like, so long as they dont clash with asyncio, for example time.sleep() clashes with asyncio, however you can use other parts of the time library, for example how I did when using it in the say command.
 
"""

#imports all essential libraries
import discord
from discord.ext import commands
import asyncio

#defines the bots intents
intents = discord.Intents.all()

#bot decorater, under discord.ext.commands
bot = commands.Bot(intents=intents, command_prefix=']')

#defines the bot token as your inputted token
token = "your token here"

#removes the initial help command
bot.remove_command('help')

#lists the cogs we want to load, from the cog folder
cogs = ['cogs.moderation', 'cogs.fun', 'cogs.setup']

#loads the cogs from the cog folder to the bot
if name __name__ = '__main__':
	for cog in cogs:
		bot.load_extension(cog)

#prints that the bot is online when it is online
@bot.event
async def on_ready():
	print(f"Logged in as {bot.user.name}, ID: {bot.user.id}")

#displays the bot's command categories
@bot.group(invoke_without_command=True)
async def help(ctx):
	embed = discord.Embed(title="Cog Example Help Command", description="Copyright, Akins M. 2021", color=discord.Colour.blurple())
	embed.add_field(name="Categories", value="-", inline=False)
	embed.add_field(name="Fun", value="The Fun Category", inline=False)
	embed.add_field(name="Moderation", value="The Moderation category", inline=False)
	embed.set_footer(text="Use ]help (category name) for more information on a category")
	await ctx.send(embed=embed)

#displays the commands for the fun cog	
@help.command()
async def fun(ctx):
	embed = discord.Embed(title="Cog Example Fun Help Command", description="Copyright, Akins M. 2021", color=discord.Colour.magenta())
	embed.add_field(name="say", value="Makes the bot say a specified message", inline=False)
	embed.add_field(name="github", value="Send a link to the CogExample's github repository", inline=False)
	embed.add_field(name="ping", value="Returns pong", inline=False)
	embed.add_field(name="random", value="Answers the age old question, does random = funny", inline=False)
	embed.add_field(name="help", value="Displays a list of command categories for the bot", inline=False)
	await ctx.send(embed=embed)
	
#displays the commands for the moderation cog
@help.command()
async def moderation(ctx):
	embed = discord.Embed(title="Cog Example Help Command", description="Copyright, Akins M. 2021". color=discord.Colour.green())
	embed.add_field(name="ban", value="Bans a specified user", inline=False)
	embed.add_field(name="kick", description="Kick a specified user", inline=False)
	await ctx.send(embed=embed)

			
#runs the bot
bot.run(token)