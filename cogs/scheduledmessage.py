from discord.ext import tasks, commands

class ScheduledMessage(commands.Cog):
    def __init__(self, bot: commands.Bot, message: str, channelID: int):
        self.bot = bot
        self.message = message
        self.channelID = channelID
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=10.0)   # hardcoded time interval :(
    async def printer(self):
        channel = self.bot.get_channel(self.channelID)
        await channel.send(self.message)

    @printer.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()
