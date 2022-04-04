from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/spec - Список специальностей",
            "/test - Тест на определение профориентации",
            "/result - Показать результаты тестирования",
            "/help - Получить справку")
    await message.answer("\n".join(text))
