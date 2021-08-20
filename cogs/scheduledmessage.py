from discord.ext import tasks, commands

class ScheduledMessage(commands.Cog):
    def __init__(self, bot: commands.Bot, message: str, channelID: int, intervalSeconds: int):
        self.bot = bot
        self.message = message
        self.channelID = channelID
        self.intervalSeconds = intervalSeconds
        self.pass_interval(self.intervalSeconds)

    def cog_unload(self):
        self.printer.cancel()

    def pass_interval(self, intervalSeconds):
        @tasks.loop(seconds=intervalSeconds)
        async def printer():
            channel = self.bot.get_channel(self.channelID)
            await channel.send(self.message)

        @printer.before_loop
        async def before_printer():
            await self.bot.wait_until_ready()

        printer.start()
