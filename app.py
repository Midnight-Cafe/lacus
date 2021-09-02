import datetime
import hashlib

import discord
from discord.ext import commands

from lacus.setup import LacusConfig

config = LacusConfig()

bot = commands.Bot(intents=config.INTENTS, command_prefix=config.BOT_PREFIX)


@bot.event
async def on_ready():
    await set_welcome_message()


@bot.event
async def on_member_join(member: discord.Member):
    await add_role(member, config.ROLE_ON_JOIN_ID)


async def add_role(member: discord.Member, role_id: int):
    role: discord.Role = member.guild.get_role(config.ROLE_ON_JOIN_ID)
    await member.add_roles(role)


async def set_welcome_message():
    channel: discord.TextChannel = bot.get_channel(876672670903717948)
    message = await channel.fetch_message(880000637998338079)

    with open("./docs/welcome.md") as welcome_message_file:
        welcome_message = welcome_message_file.read()
        current_md5 = hashlib.md5(message.content.strip().encode()).hexdigest()
        message_md5 = hashlib.md5(welcome_message.strip().encode()).hexdigest()
        if current_md5 != message_md5:
            welcome_message = welcome_message.replace(
                "$last_updated", str(datetime.date.today())
            )
            await message.edit(content=welcome_message, suppress=True)


bot.run(config.DISCORD_TOKEN)
