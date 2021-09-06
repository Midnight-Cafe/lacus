import os

import discord
from dotenv import load_dotenv

from lacus.exceptions import IncorrectConfigurationError

load_dotenv()


class LacusConfig:
    required_env = [
        "DISCORD_TOKEN",
        "GUILD_ID",
        "BOT_PREFIX",
        "ROLE_ON_JOIN_ID",
    ]

    DISCORD_TOKEN: str = ""
    BOT_PREFIX: str = ""
    GUILD_ID: int = 0
    ROLE_ON_JOIN_ID: int = 0

    INTENTS: discord.Intents = None

    def __init__(self):
        self._check_all_required_envs()

        self.DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
        self.BOT_PREFIX = os.environ.get("BOT_PREFIX")
        self.GUILD_ID = int(os.environ.get("GUILD_ID"))
        self.ROLE_ON_JOIN_ID = int(os.environ.get("ROLE_ON_JOIN_ID"))

        self.INTENTS = discord.Intents.default()
        self.INTENTS.members = True

    def _check_all_required_envs(self):
        not_found = set(self.required_env) - set(os.environ)
        if len(not_found) > 0:
            raise IncorrectConfigurationError(", ".join(not_found))
