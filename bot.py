import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ @BotFather
TOKEN = "8429740565:AAGORVe9PAPbDjhQcubjijMDoLXs2a3iEBo"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🏮 Открыть TON TEMPLE", url="https://example.com")],
            [InlineKeyboardButton(text="ℹ️ Как это работает", callback_data="how")]
        ]
    )

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    text = (
        "🏮 TON TEMPLE\n"
        "Ритуальный интерфейс удачи.\n\n"
        "Нажми кнопку ниже 👇"
    )
    await message.answer(text, reply_markup=main_kb())

@dp.callback_query(lambda c: c.data == "how")
async def how_handler(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer(
        "Это ритуальный интерфейс: запускаешь ритуал → получаешь знак дня.\n"
        "Не является финансовым советом."
    )

async def main():
    print("Bot started")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
