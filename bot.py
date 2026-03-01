
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, Message

TOKEN = "8429740565:AAGOfmcvzVxZHxWF7Ek3eyYyM9P_9YolC7I"
WEBAPP_URL = "https://ton-temple.vercel.app"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🏮 ENTER TEMPLE",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )

    await message.answer(
        "🏮 TON TEMPLE is ready.\nTap ENTER TEMPLE to open the interface.",
        reply_markup=keyboard
    )

async def main():
    print("Bot started")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
