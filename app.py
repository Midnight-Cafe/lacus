import discord
from discord.ext import commands

from lacus.setup import LacusConfig

config = LacusConfig()

bot = commands.Bot(
    intents=config.INTENTS,
    command_prefix=config.BOT_PREFIX
)


@bot.event
async def on_member_join(member: discord.Member):
    guild = await bot.fetch_guild(config.GUILD_ID)
    role: discord.Role = guild.get_role(config.ROLE_ON_JOIN_ID)
    await member.add_roles(role)

bot.run(config.DISCORD_TOKEN)
