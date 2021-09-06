import os

import discord
import yaml
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class LacusBot(commands.Bot):
    def __init__(self):
        with open("config.yml", "r") as file:
            config = yaml.safe_load(file)
            super().__init__(
                intents=self._setup_intents(),
                command_prefix=config["bot_prefix"],
            )
            self.channels = config["channels"]

    def run(self):
        super().run(os.environ.get("DISCORD_TOKEN"))

    def _setup_intents(self) -> discord.Intents:
        intents = discord.Intents.default()
        intents.members = True
        return intents
