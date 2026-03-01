import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER"
WEBAPP_URL = "https://ton-temple.vercel.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="🏮 Открыть TON TEMPLE",
                    web_app=types.WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )

    await message.answer(
        "TON TEMPLE готов.\nНажми кнопку ниже, чтобы открыть Mini App.",
        reply_markup=kb
    )

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
