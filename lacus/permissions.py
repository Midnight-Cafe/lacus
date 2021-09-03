from discord.ext import commands


def is_owner():
    """The user is the owner of the guild."""

    def predicate(ctx: commands.Context):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id

    return commands.check(predicate)
