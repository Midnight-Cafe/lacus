from discord.ext import tasks, commands


class ScheduledMessage(commands.Cog):
    def __init__(
        self,
        bot: commands.Bot,
        message: str,
        channel_id: int,
        interval_seconds: int,
    ):
        self.bot = bot
        self.message = message
        self.channel_id = channel_id
        self.interval_seconds = interval_seconds
        self.initialize_send_message()

    def cog_unload(self):
        self.task_send_message.cancel()

    def initialize_send_message(self):
        self.task_send_message = tasks.loop(seconds=self.interval_seconds)(
            self.send_message
        )
        self.task_send_message.before_loop(self.before_send_message)
        self.task_send_message.start()

    async def send_message(self):
        channel = self.bot.get_channel(self.channel_id)
        await channel.send(self.message)

    async def before_send_message(self):
        await self.bot.wait_until_ready()
