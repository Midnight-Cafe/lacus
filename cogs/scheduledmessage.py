from discord.ext import tasks, commands

class ScheduledMessage(commands.Cog):
    def __init__(self, bot: commands.Bot, message: str, channel_id: int, interval_seconds: int):
        self.bot = bot
        self.message = message
        self.channel_id = channel_id
        self.interval_seconds = interval_seconds
        # decorate printer and before_printer to allow dynamic interval be passed to tasks.loop
        self.printer = tasks.loop(seconds=self.interval_seconds)(self.printer)
        self.before_printer = self.printer.before_loop(self.before_printer)
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    async def printer(self):
        channel = self.bot.get_channel(self.channel_id)
        await channel.send(self.message)

    async def before_printer(self):
        await self.bot.wait_until_ready()
