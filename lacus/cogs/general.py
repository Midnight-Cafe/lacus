import datetime
import hashlib
from typing import TYPE_CHECKING

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from lacus.bot import LacusBot


def _check_hash_is_different(left, right):
    return (
        hashlib.md5(left.strip().encode()).hexdigest()
        != hashlib.md5(right.strip().encode()).hexdigest()
    )


class GeneralCog(commands.Cog):
    WELCOME_MESSAGE_FILE_LOCATION = "./docs/welcome.md"

    def __init__(self, bot: "LacusBot"):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        welcome_channel_id = self.bot.channels["welcome"]
        welcome_channel: discord.TextChannel = self.bot.get_channel(
            welcome_channel_id
        )
        await self.set_welcome_message(welcome_channel)

    async def set_welcome_message(self, channel: discord.TextChannel):
        """
        Creates the welcome message if there is none set in the designated
        Welcome channel, otherwise edit the existing one.
        """
        with open(self.WELCOME_MESSAGE_FILE_LOCATION) as welcome_message_file:
            welcome_message = welcome_message_file.read()
        content = await self._hydrate_welcome_message(welcome_message)
        try:
            message_id = channel.last_message_id
            message: discord.Message = await channel.fetch_message(message_id)
        except discord.errors.HTTPException:
            print(
                "Could not find existing Welcome message. Creating a new one."
            )
            await channel.send(content=content, suppress=True)
        else:
            message: discord.Message = await channel.fetch_message(message_id)

            # Only update if there is any changes otherwise do nothing.
            if _check_hash_is_different(message.content, welcome_message):
                print(
                    "Existing Welcome message found. Updating current message."
                )
                await message.edit(content=content, suppress=True)

    async def _hydrate_welcome_message(self, message_template):
        today = str(datetime.date.today())
        content = message_template.replace("$last_updated", today)
        return content
