# lacus
Moderation bot

# Get Started
Requirements:
- Python 3.9


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

### How to run the bot
1. Make a copy of the `.env.test` and call it `.env`
2. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a bot account.
  - Follow this guide: https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro
  - Setup the `TOKEN` environment variable in `.env` using the Discord bot token
3. Create a test Discord server
4. Invite your bot to your server

#### To run locally:
```bash
python app.py
```
