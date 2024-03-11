import asyncio
from aiogram import Bot ,Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot= Bot(token="6549094895:AAFjrovAT_2FpKGMiyUExBvzczTUh2hExaA")
dp=Dispatcher()
@dp.message(CommandStart())
async def start_cmd(message:types.Message) :
    await message.answer('Привет, студент! Этот бот был создан для того, чтобы облегчить твои поиски в стажировках и вакансий в лучшем банке страны.Кнопка "Стажировка" фильтрует все уведомления и показывает только актуальную информацию по стажировкам. Кнопка "Вакансии" тот же принцип действия ')
async def main() :
    await dp.start_polling(bot)

asyncio.run(main())
