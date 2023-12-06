from telegram.ext import Application, CommandHandler
import nest_asyncio
nest_asyncio.apply()


async def start(update, context):
    await update.message.reply_text('Hi! I am your bot.')

async def main():
    application = Application.builder().token("ENTER KEY").build()

    application.add_handler(CommandHandler("start", start))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
