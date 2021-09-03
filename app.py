from lacus.cogs.general import GeneralCog
from discord.ext import commands
from lacus.cogs.scheduled_message import ScheduledMessageCog
from lacus.cogs.members import MembersCog

from lacus.setup import LacusConfig


def main():
    config = LacusConfig()

    bot = commands.Bot(
        intents=config.INTENTS,
        command_prefix=config.BOT_PREFIX,
    )
    bot.add_cog(GeneralCog(bot, role_on_join_id=config.ROLE_ON_JOIN_ID))
    bot.add_cog(MembersCog(bot, role_on_join_id=config.ROLE_ON_JOIN_ID))
    bot.add_cog(ScheduledMessageCog(bot))
    bot.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
