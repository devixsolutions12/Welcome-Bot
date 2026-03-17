# Webivus Discord Welcome Bot

A standalone Python Discord bot that sends rich welcome messages to users in DMs and specific welcome channels when they join the server.

## 🛠️ Setup Instructions

### 1. Prerequisites
- **Python 3.8+**: Ensure Python is installed and added to your system PATH.
- **Discord Bot Account**: You must have a bot created in the [Discord Developer Portal](https://discord.com/developers/applications).

### 2. Configure Environment `.env`
The `.env` file is already created for you in this folder. It contains:
- `DISCORD_TOKEN`: Your bot token.
- `WELCOME_CHANNEL_IDS`: Comma-separated channel IDs where messages will be sent.
- `LOGO_URL`: URL to the logo thumbnail.

### 3. Run the Bot
Double-click `run.bat` (on Windows) or run the following in your terminal:
```bash
pip install -r requirements.txt
python main.py
```

---

## ⚠️ CRITICAL: Enable Server Members Intent

For this bot to detect users joining, you **MUST** enable the **Server Members Intent** in the Discord Developer Portal:

1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Select your Application (`1483554020466364497`).
3. Click on the **Bot** tab on the left sidebar.
4. Scroll down to the **Privileged Gateway Intents** section.
5. Toggle **ON** the **Server Members Intent**.
6. Click **Save Changes**.

If you do not do this, the bot will connected but will **NOT** trigger the welcome message when users join.

---

## 🔗 Invite the Bot

To invite the bot to your server, use the following URL:

`https://discord.com/oauth2/authorize?client_id=1483554020466364497&scope=bot&permissions=84992`

*Permissions included: View Channels, Send Messages, Embed Links, Read Message History.*
