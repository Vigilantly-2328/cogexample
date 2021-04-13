#the following code imports essential libraries
import discord
from discord.ext import commands

#the following code defines our moderation class as a cog under discord.ext.commands
class Moderation(commands.Cog)
	def __init__(self, bot):
		self = self.bot

	#the following code bans a user
	@commands.command(name='ban')
	@commands.has_permissions(ban_members=True)
	async def _ban(self, bot, user: discord.Member, *, reason=None):
		if reason == None:
			reason = "For being very rude"
		await user.ban(reason=reason)
		await ctx.send(f"{user.name} has been banned by {ctx.message.author.name} for {reason}", delete_after=3)
		await user.send(f"You have been banned from {ctx.guild} for {reason}")

	#the following code kicks a user
	@commands.command(name='kick')
	@commands.has_permissions(kick_members=True)
	async def _kick(self, bot, user: discord.Member, *, reason=none):
		if reason == None:
			reason = "For being very rude"
		await user.ban(reason=reason)
		await ctx.send(f"{user.name} has been banned by {ctx.message.author.name} for {reason}", delete_after=3)
		await user.send(f"You have been banned from {ctx.guild} for {reason}")

	#Once again going to reiterate a few things. 1: Self is a necessary argument in any command or event in which you are doing anything but sending messages
	#2: You must specify a user as discord.Member if you want the command to do anything to a specified user
	#3: You shouldn't define your bot under discord.ext.commands in a cog.

def setup(bot):
	await bot.add_cog(Moderation(bot))
