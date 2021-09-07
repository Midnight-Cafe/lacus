# lacus

Moderation bot

# Get Started

Requirements:

- Python 3.9

---

## How to install:

```bash
python -m pip install -r requirements.txt
```

### If you are using virtualenv:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

---

## How to run the bot

1. Make a copy of `.env.empty` and call it `.env`.
2. Make a copy of `config.yml.empty` and call it `config.yml`.
3. Create a Discord server to test the bot.
4. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a bot account.

- Follow this guide: https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro
- Setup the `TOKEN` environment variable in `.env` using the Discord bot token

5. Invite the bot to your server.
6. Populate `config.yml` based on your test server.

#### To run locally:

```bash
python app.py
```
