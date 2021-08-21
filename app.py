import discord
import asyncio
import json
import os
from discord.ext import commands, tasks
from cogs.scheduledmessage import ScheduledMessage

from lacus.setup import LacusConfig

config = LacusConfig()

bot = commands.Bot(
    intents=config.INTENTS,
    command_prefix=config.BOT_PREFIX
)


@bot.event
async def on_member_join(member: discord.Member):
    await add_role(member, config.ROLE_ON_JOIN_ID)


async def add_role(member: discord.Member, role_id: int):
    role: discord.Role = member.guild.get_role(config.ROLE_ON_JOIN_ID)
    await member.add_roles(role)

@bot.event
async def on_ready():
    def message_cog_maker(prompt):
        if(prompt['type']=='question'):
            bot.add_cog(ScheduledMessage(bot, prompt['message'], prompt['channelID'], prompt['intervalSeconds']))
    if (os.path.isfile('./messages.json')):
        f = open('./messages.json', 'r')
        messages = json.loads(f.read())
        list(map(message_cog_maker, messages['prompts']))
        f.close()


bot.run(config.DISCORD_TOKEN)
