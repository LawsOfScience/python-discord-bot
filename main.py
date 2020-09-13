"""Main bot file and command handler for my Python Discord bot"""
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="act!")
cogs = ["cogs.general_cmds", "cogs.owner_cmds"]

@bot.event
async def on_ready():
    """Fires when bot is ready"""
    print(f"Bot is ready as {bot.user}!")

def main():
    """Initializes the bot"""
    print("Loading cogs...")
    for cog in cogs:
        bot.load_extension(cog)
    print("Cogs loaded!")

    print("Initializing bot...")
    with open("key.json", "r") as keyfile:
        data = keyfile.read()
        keyfile.close()

    obj = json.loads(data)
    bot.run(obj["key"])

main()
