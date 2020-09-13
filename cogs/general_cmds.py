"""The cog for general bot commands"""
import datetime
import discord
from discord.ext import commands

class GeneralCog(commands.Cog):
    """Cog for general commands"""

    def __init__(self, bot):
        self.bot = bot
    
def setup(bot):
    """Add the cog to the bot"""
    bot.add_cog(GeneralCog(bot))
