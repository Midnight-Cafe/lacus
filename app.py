import datetime
import hashlib
import pytz

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

@bot.command(name="event")
async def add_event(ctx,event_name, date, time, tz):
    day, month, year = date.split("/")
    hour, minute = time.split(":")
    timezone = pytz.timezone(tz.strip())

    dt = timezone.localize(datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)))
    date_format = "%d-%b-%Y %H:%M"
    timezones_list = ['America/Los_Angeles', 'Canada/Central', 'Asia/Singapore']

    if (tz not in timezones_list):
        timezones_list.append(tz)
    reply_message = f'```Event name: {event_name}\nScheduled for:\n'
    for zone in timezones_list:
        localDateTime = dt.astimezone(pytz.timezone(zone))
        reply_message+= f'{zone}: {localDateTime.strftime(date_format)}\n'
    reply_message+='```'
    await ctx.send(reply_message)

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
