import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class LacusBaseException(Exception):
    pass


class IncorrectConfigurationError(LacusBaseException):
    pass


required_env = [
    "DISCORD_TOKEN",
    "GUILD_ID",
    "ROLE_ON_JOIN_ID",
    "ROLE_ON_JOIN_NAME"
]
env_not_found = set(required_env) - set(os.environ)
if len(env_not_found) > 0:
    raise IncorrectConfigurationError(', '.join(env_not_found))

guild_id = os.environ.get("GUILD_ID")
role_on_join_id = os.environ.get("ROLE_ON_JOIN_ID")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix="!")


@bot.event
async def on_member_join(member: discord.Member):
    guild = await bot.fetch_guild(guild_id)
    role: discord.Role = guild.get_role(role_on_join_id)
    await member.add_roles(role)

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)
