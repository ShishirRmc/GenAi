import logging
from aiogram import Bot, Dispatcher, html
from dotenv import load_dotenv
import os
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import sys
import asyncio


load_dotenv(dotenv_path="C:\\Users\\rmcsh\\Documents\\GenAi\\LangGraph\\agents\\.env")

# Corrected variable names to match .env keys
google_api_key = os.getenv("GOOGLE_API_KEY")
telegram_api_key = os.getenv("TELEGRAM_API_KEY")

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    try:
        # Initialize Bot instance with default bot properties which will be passed to all API calls
        bot = Bot(token=telegram_api_key, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        # Start polling for events
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user.")