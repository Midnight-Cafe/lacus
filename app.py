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
    bot.add_cog(MembersCog(bot, role_on_join_id=config.ROLE_ON_JOIN_ID))
    scheduled_messages_cogs = ScheduledMessageCog.build_cogs(bot, "./messages.json")
    for scheduled_messages_cog in scheduled_messages_cogs:
        bot.add_cog(scheduled_messages_cog)
    bot.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
