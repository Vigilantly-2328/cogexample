
#imports essential libraries
import discord
from discord.ext import commands
from time import localtime, strftime

#defines the Fun class as a cog under discord.ext.commands
class Fun(commands.cog)
	def __init__(self, bot):
		self.bot=bot

	#basic ping command
	@commands.command(name='ping')
	async def _ping(self, ctx):
		await ctx.send("Pong")

	#makes the bot say a user inputted message
	@commands.command(name='say')
	async def _say(self, ctx, *, message=None):
		await ctx.message.delete()
		if message == None:
			await ctx.send("You must include a message", delete_after=3)
		else:
			await ctx.send(message)
			print(message + + strftime("%Y-%m-%d %H:%M:%S", localtime()))

	#links the github repository in the user's direct messages
	@commands.command(name='github')
	async def _github(self, ctx):
		author = ctx.message.author
		embed = discord.Embed(title="Github Repository for Cog Examples", description=f"Requested by {author.name}", color=discord.Colour.magenta(), url='https://github.com/Vigilantly-2328/cogexample', timestamp=message.created_at)
		embed.add_field(name="Made by Akins#2229", value="If you're reading this far, thank you!")
		await author.send(embed=embed)

	#random=funny
	@commands.command(name='random')
	async def _random(self, ctx):
		await ctx.send("random != funny")

#If you haven't yet noticed, self is a necessary argument to assign if your bot is doing anything but just sending messages, this includes banning, kicking, deleting messages and more.

#the code below ensures that out cog can be set up in main.py 
def setup(bot):
	await bot.add_cog(Fun(bot))
