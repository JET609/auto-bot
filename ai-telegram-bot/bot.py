import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not OPENAI_API_KEY or not TELEGRAM_BOT_TOKEN:
    raise SystemExit("❌ Please set OPENAI_API_KEY and TELEGRAM_BOT_TOKEN in .env")

client = OpenAI(api_key=OPENAI_API_KEY)  # uses new OpenAI SDK

SYSTEM_PROMPT = (
    "You are a friendly helpful AI assistant. "
    "Keep answers short, clear, and practical."
)

async def start(update, context):
    await update.message.reply_text("👋 Hey, I'm your AI bot. Send me anything.")

async def chat(update, context):
    user_text = update.message.text

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text},
            ],
            max_tokens=400,
        )

        reply = completion.choices[0].message.content.strip()
        await update.message.reply_text(reply)

    except Exception as e:
        print("Error:", e)
        await update.message.reply_text("⚠️ Something broke. Try again in a bit.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
