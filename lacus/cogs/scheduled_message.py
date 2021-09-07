import random

from discord.ext import commands, tasks

from lacus.permissions import is_owner


class ScheduledMessageCog(commands.Cog):
    interval = {
        "seconds": 0,
        "minutes": 0,
        "hours": 24,
    }
    permissions = [is_owner]

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel = None
        self.messages = []

        # Initialize task loop
        loop = tasks.loop(**self.interval)
        self.task_loop = loop(self.task)

    @commands.group()
    @commands.check_any(is_owner())
    async def scheduled_messages(self, ctx: commands.Context):
        pass

    @scheduled_messages.group()
    async def start(self, ctx: commands.Context):
        if not self.channel:
            self.channel = ctx.channel
        if self.messages:
            self.task_loop.start()
            await ctx.send("Scheduled messages have been started.")
        else:
            await ctx.send("No messages!")

    @scheduled_messages.group()
    async def stop(self, ctx: commands.Context):
        if self.task_loop.is_running():
            self.task_loop.stop()
            await ctx.send("Scheduled messages have been stopped.")

    @scheduled_messages.group()
    async def add(self, ctx: commands.Context, scheduled_message):
        self.messages.append(scheduled_message)
        key = len(self.messages) - 1
        message = f"**Scheduled message has been created! Key: [`{key}`]**"
        await ctx.send(message)

    @scheduled_messages.group()
    async def delete(self, ctx: commands.Context, scheduled_message_id):
        id = int(scheduled_message_id)
        message = self.messages[id]
        self.messages.pop(id)
        message = f"**Scheduled message ``` {message} ``` has been deleted!**"
        await ctx.send(message)

    @scheduled_messages.group()
    async def list(self, ctx: commands.Context):
        if not self.messages:
            await ctx.send("There are no scheduled messages on this channel.")
            return
        options = [
            f"[{key}] {option}" for key, option in enumerate(self.messages)
        ]
        options_str = "\n".join(options)
        template = (
            "```These are the scheduled messages for this channel:\n%s```"
        )
        message = template % options_str
        await ctx.send(message)

    @scheduled_messages.group()
    async def frequency(self, ctx: commands.Context, hours):
        self.task_loop.change_interval(hours=int(hours))

    def cog_unload(self):
        self.task_loop.cancel()

    async def task(self):
        random_index = random.randint(0, len(self.messages) - 1)
        template = ":exclamation: **%s**"
        message = template % self.messages[random_index]
        await self.channel.send(message)
