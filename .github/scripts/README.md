# Auto ASCP Poster Bot

A simple Post Bot rebranded for ASCP.

## Instructions

### 1. Adding secrets

Go to your repo `settings > secrets > new repository secret`, and add these secrets.

- `BOT_TOKEN`: Telegram bot token
- `CHAT_ID`: Telegram group/channel chat ID where the rom needs to be posted
- `PRIV_CHAT_ID`: Telegram group/channel chat ID for logs/status
- `GH_TOKEN`: Github access token to push changes to repo

**Note:** Bot should be added in the group/channel where the rom needs to be posted

### 2. Running the bot

- Actions will automatically run if any changes are committed to `device/**/updater/full.json`.
- You can also run the bot by going to `actions > ASCP Poster Bot > workflow-dispatch`.
