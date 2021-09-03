import datetime
import hashlib

import discord
from discord.ext import commands


class GeneralCog(commands.Cog):
    def __init__(self, bot: commands.Bot, role_on_join_id: int):
        self.bot = bot
        self.role_on_join_id = role_on_join_id

    @commands.Cog.listener()
    async def on_ready(self):
        await self.set_welcome_message()

    async def add_role(self, member: discord.Member, role_id: int):
        role: discord.Role = member.guild.get_role(self.role_on_join_id)
        await member.add_roles(role)

    async def set_welcome_message(self):
        channel: discord.TextChannel = self.bot.get_channel(876672670903717948)
        message = await channel.fetch_message(880000637998338079)

        with open("./docs/welcome.md") as welcome_message_file:
            welcome_message = welcome_message_file.read()
            current_md5 = hashlib.md5(
                message.content.strip().encode()
            ).hexdigest()
            message_md5 = hashlib.md5(
                welcome_message.strip().encode()
            ).hexdigest()
            if current_md5 != message_md5:
                welcome_message = welcome_message.replace(
                    "$last_updated", str(datetime.date.today())
                )
                await message.edit(content=welcome_message, suppress=True)
