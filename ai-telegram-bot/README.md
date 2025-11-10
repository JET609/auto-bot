# AI Telegram Bot

A minimal Telegram bot powered by OpenAI (ChatGPT).

## Features

- Reply to any DM using OpenAI API
- Clean and simple codebase
- Secrets stored securely in `.env` file (not pushed to GitHub)
- Easy to deploy locally or on cloud platforms

## Setup

### 1. Create Your Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow the instructions
3. Copy the bot token (looks like `123456789:ABC...`)

### 2. Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create or retrieve your API key

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_token_here
```

### 5. Run the Bot

```bash
python bot.py
```

Your bot should now be running! Open Telegram and send a message to test it.

## Deployment

You can deploy this bot to:
- **Render**: Connect your GitHub repo and deploy
- **Railway**: Similar to Render, easy deployment from GitHub
- **Your own server**: Run the bot.py script with a process manager like PM2

## Project Structure

```
ai-telegram-bot/
├── bot.py              # Main bot code
├── requirements.txt    # Python dependencies
├── .env               # Your API keys (DO NOT COMMIT)
├── .gitignore         # Excludes .env from git
└── README.md          # This file
```

## Notes

- The bot uses the `gpt-4o-mini` model by default
- Responses are limited to 400 tokens
- Make sure to never commit your `.env` file to GitHub
