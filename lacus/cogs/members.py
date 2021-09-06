from typing import TYPE_CHECKING

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from lacus.bot import LacusBot


class MembersCog(commands.Cog):
    def __init__(self, bot: "LacusBot"):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        role_on_join_id = self.bot.config.ROLE_ON_JOIN_ID
        await self._add_role(member, role_on_join_id)

    async def _add_role(self, member: discord.Member, role_id: int):
        role: discord.Role = member.guild.get_role(role_id)
        await member.add_roles(role)
