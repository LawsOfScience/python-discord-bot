"""The cog for owner commands"""
import discord
from discord.ext import commands

class OwnerCommands(commands.Cog, command_attrs = dict(hidden=True)):
    """The cog for owner commands. Can't be used if you're not the bot owner."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["rel", "re", "r"])
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Reloads a cog"""
        await ctx.send(f":clock1: Reloading cog {cog}...")
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await ctx.send(f":white_check_mark: Reloaded **{cog}** successfully!")
        except Exception as ex:
            err_embed = discord.Embed(
                title = ":exclamation: Reloading Error :exclamation:",
                color = discord.Color.from_rgb(255, 0, 0),
                description = f"There was an error reloading the cog **{cog}**."
            )
            err_embed.add_field(
                name = "Error Type",
                value = f"{type(ex).__name__}",
                inline = False
            )
            err_embed.add_field(
                name = "Error Message",
                value = f"{ex}",
                inline = False
            )
            await ctx.send(content = None, embed = err_embed)

    @reload.error
    async def reload_err(self, ctx, err: str):
        if isinstance(err, commands.errors.MissingRequiredArgument):
            await ctx.send("Please provide a cog to reload.")
        else:
            await ctx.send(err)

    @commands.command(aliases = ["l"])
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Loads a cog"""
        await ctx.send(f":clock1: Loading cog **{cog}**...")
        try:
            self.bot.load_extension(cog)
            await ctx.send(f":white_check_mark: Loaded **{cog}** successfully!")
        except Exception as ex:
            err_embed = discord.Embed(
                title = ":exclamation: Loading Error :exclamation:",
                color = discord.Color.from_rgb(255, 0, 0),
                description = f"There was an error reloading the cog **{cog}**."
            )
            err_embed.add_field(
                name = "Error Type",
                value = f"{type(ex).__name__}",
                inline = False
            )
            err_embed.add_field(
                name = "Error Message",
                value = f"{ex}",
                inline = False
            )
            await ctx.send(content = None, embed = err_embed)
    
    @load.error
    async def load_err(self, ctx, err: str):
        if isinstance(err, commands.errors.MissingRequiredArgument):
            await ctx.send("Please provide a cog to load.")
        else:
            await ctx.send(err)


    @commands.command(aliases = ["ul"])
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Unloads a cog"""
        print(f":clock1: Unloading cog **{cog}**...")
        try:
            self.bot.unload_extension(cog)
            await ctx.send(f":white_check_mark: Unloaded **{cog}** successfully!")
        except Exception as ex:
            err_embed = discord.Embed(
                title = ":exclamation: Unloading Error :exclamation:",
                color = discord.Color.from_rgb(255, 0, 0),
                description = f"There was an error reloading the cog **{cog}**."
            )
            err_embed.add_field(
                name = "Error Type",
                value = f"{type(ex).__name__}",
                inline = False
            )
            err_embed.add_field(
                name = "Error Message",
                value = f"{ex}",
                inline = False
            )
            await ctx.send(content = None, embed = err_embed)
    
    @unload.error
    async def unload_err(self, ctx, err: str):
        if isinstance(err, commands.errors.MissingRequiredArgument):
            await ctx.send("Please provide a cog to unload.")
        else:
            await ctx.send(err)

def setup(bot):
    """Add the cog to the bot"""
    bot.add_cog(OwnerCommands(bot))