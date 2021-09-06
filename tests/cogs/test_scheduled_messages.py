import discord
import pytest
from discord.ext import commands
from discord.ext import test as dpytest

from lacus.cogs.scheduled_message import ScheduledMessageCog


@pytest.fixture
def config(event_loop):
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(intents=intents, command_prefix="!")
    bot.add_cog(ScheduledMessageCog(bot))

    dpytest.configure(bot)
    config = dpytest.get_config()

    # Make the first member the owner
    member: discord.Member = config.members[0]
    guild: discord.Guild = config.guilds[0]
    guild.owner_id = member.id
    return config


@pytest.mark.asyncio
async def test_add_message(config):
    owner_member = config.members[0]
    message = "!scheduled_messages add 'Hello world'"
    await dpytest.message(message, member=owner_member)
    assert (
        dpytest.verify()
        .message()
        .content("**Scheduled message has been created! Key: [`0`]**")
    )


@pytest.mark.asyncio
async def test_empty_list(config):
    owner_member = config.members[0]
    message = "!scheduled_messages list"
    await dpytest.message(message, member=owner_member)
    assert (
        dpytest.verify()
        .message()
        .content("There are no scheduled messages on this channel.")
    )


@pytest.mark.asyncio
async def test_add_and_list(config):
    owner_member = config.members[0]
    scheduled_message = "Hello world"
    message = f'!scheduled_messages add "{scheduled_message}"'
    await dpytest.message(message, member=owner_member)
    assert dpytest.verify().message().contains().content("Key: [`0`]")

    message = "!scheduled_messages list"
    await dpytest.message(message, member=owner_member)
    assert dpytest.verify().message().contains().content(scheduled_message)
