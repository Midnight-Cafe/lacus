from lacus.bot import LacusBot
from lacus.cogs.general import GeneralCog
from lacus.cogs.members import MembersCog
from lacus.cogs.scheduled_message import ScheduledMessageCog
from lacus.cogs.time import TimeCog


def main():
    bot = LacusBot()
    bot.add_cog(GeneralCog(bot))
    bot.add_cog(MembersCog(bot))
    bot.add_cog(ScheduledMessageCog(bot))
    bot.add_cog(TimeCog(bot))
    bot.run()


if __name__ == "__main__":
    main()
