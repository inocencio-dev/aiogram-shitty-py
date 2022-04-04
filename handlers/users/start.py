from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import markup_klasses
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name},"
                         f" я бот, который поможет тебе определится с выбором профессии и местом обучения.",
                        )
    await message.answer("Сколько классов Вы закончили?", reply_markup=markup_klasses)

