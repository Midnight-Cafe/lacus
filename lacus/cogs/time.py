import discord
from discord.ext import commands
import datetime
import pytz

class TimeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel = None
        self.timezones = ['America/Los_Angeles', 'Canada/Central', 'Asia/Singapore']

    @commands.group()
    async def time(self, ctx: commands.Context):
        pass

    @time.group()
    async def convert(self, ctx: commands.Context, date, time ,tz):
        day, month, year = date.split("/")
        hour, minute = time.split(":")
        timezone = pytz.timezone(tz.strip())

        dt = timezone.localize(datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)))
        date_format = "%d-%b-%Y %H:%M"

        reply_message = f'```{date} {time} in {tz} converted to other timezones:\n'
        for zone in self.timezones:
            localDateTime = dt.astimezone(pytz.timezone(zone))
            reply_message+= f'{zone:20s}: {localDateTime.strftime(date_format)}\n'
        reply_message+='```'
        await ctx.send(reply_message)
        
    @time.group()
    async def add_timezone(self, ctx:commands.Context, timezone):
        if (timezone in self.timezones):
            await ctx.send("Timezone has already been added!")
            return
        
        if (timezone not in pytz.all_timezones):
            await ctx.send("Please enter a valid timezone name.\n A list of timezonen names can be found here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones ")
            return
        
        self.timezones.append(timezone)
        await ctx.send(f'{timezone} has been added!')
