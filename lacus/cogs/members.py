import discord
from discord.ext import commands


class MembersCog(commands.Cog):
    def __init__(self, bot: commands.Bot, role_on_join_id: int):
        self.bot = bot
        self.role_on_join_id = role_on_join_id

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await self._add_role(member, self.role_on_join_id)

    async def _add_role(self, member: discord.Member, role_id: int):
        role: discord.Role = member.guild.get_role(role_id)
        await member.add_roles(role)
