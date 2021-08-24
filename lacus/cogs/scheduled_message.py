import json

from discord.ext import tasks, commands


def build_scheduled_message_cog(bot, prompt):
    if prompt["type"] == "question":
        return ScheduledMessage(
            bot,
            prompt["message"],
            prompt["channel_id"],
            prompt["interval_seconds"],
        )


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

    @staticmethod
    def build_cogs(bot: commands.Bot, messages_file: str):
        with open(messages_file, "r") as messages_file:
            messages_json = json.loads(messages_file.read())
            for prompt in messages_json["prompts"]:
                bot.add_cog(build_scheduled_message_cog(bot, prompt))

    def cog_unload(self):
        self.task_send_message.cancel()

    def initialize_send_message(self):
        loop = tasks.loop(seconds=self.interval_seconds)
        self.task_send_message = loop(self.send_message)
        self.task_send_message.before_loop(self.before_send_message)
        self.task_send_message.start()

    async def send_message(self):
        channel = self.bot.get_channel(self.channel_id)
        await channel.send(self.message)

    async def before_send_message(self):
        await self.bot.wait_until_ready()
